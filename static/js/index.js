const assessifyBtn = document.getElementById("assessifyBtn");
assessifyBtn.addEventListener("click",()=>{
  const assessifyDec = document.getElementById("assessifyDec");
  console.log(assessifyDec)
  if(assessifyDec.style.display==="none"){
    assessifyDec.style.display="block";
  }else{
    assessifyDec.style.display="none";
  }
});
