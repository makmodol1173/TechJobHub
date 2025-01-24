from django.shortcuts import render
from django.conf import settings
import os
from pdfminer.high_level import extract_text

# from langchain_community.llms import HuggingFaceHub
# from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field 
from langchain_core.output_parsers import JsonOutputParser
from langchain.chains import LLMChain
from typing import List
from langchain_huggingface import HuggingFaceEndpoint
import json
from decouple import config



prompt_template = """
            Analyze the following resume text and provide insights:

            1. Overall Resume Score: Provide a score out of 10 based on readability, structure, clarity, and relevance.
            2. Introduction Section Score: Evaluate the introduction section (summary, objective, or personal statement) and rate it out of 10.
            3. Skills Section Score: Assess the skills section and rate it out of 10.
            4. Projects Section Score: Analyze the projects section and rate it out of 10 based on:
            - Proper description of projects
            - Presence of a live URL (if applicable)
            - Clear mention of features
            - Technologies used
            5. Suggestions for Improvement: Provide up to 10 actionable bullet points for improving the resume.

            Resume Text:
            {resume_text}

            Provide the scores and suggestions in a structured JSON format: {format_instructions}
            """

class ResumeEvaluation(BaseModel):
    overall_resume_score: int = Field(description="Overall resume score")
    introduction_score: int = Field(description="Score for the introduction section")
    skills_score: int = Field(description="Score for the skills section")
    projects_score: int = Field(description="Score for the projects section")
    suggestions: List[str] = Field(description="List of suggestions for resume improvement")

    
def extractify(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['resume']

        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        extracted_text = extract_text(file_path)
    
        repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
        huggingfacehub_api_token = config("HUGGINGFACE_API_KEY")
        llm = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = huggingfacehub_api_token)
        
        parser = JsonOutputParser(pydantic_object=ResumeEvaluation)
        
        resume_analysis_prompt = PromptTemplate(
        input_variables=["resume_text"],
        template=prompt_template,
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
    
        chain = LLMChain(prompt=resume_analysis_prompt, llm=llm)
        response = chain.invoke({"resume_text": extracted_text})
        template = """
            Take the following output and ensure it is formatted correctly as valid JSON, including appropriate indentation. 
            Do not modify the content, only format it properly. Here's the output:

            {output}

            Return the formatted JSON:
            """

        prompt = PromptTemplate(
            input_variables=["output"],
            template=template,
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        formatted_json = chain.run(output=response["text"])
        cleaned_json = formatted_json.replace("```json", "").replace("```", "").strip()
        resume_response = json.loads(cleaned_json)
        print(resume_response)
        
        for key, value in resume_response.items():
            if isinstance(value, int): 
                resume_response[key] = value * 10
            elif isinstance(value, list): 
                resume_response[key] = [item for item in value]

        return render(request, 'extractify.html', {"resume_data": resume_response})

    return render(request, 'extractify.html')
    
