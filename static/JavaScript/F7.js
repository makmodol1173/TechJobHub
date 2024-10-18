document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.job-post-form');
    
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const jobTitle = document.getElementById('job-title').value;
        const location = document.getElementById('location').value;
        const category = document.getElementById('category').value;
        const deadline = document.getElementById('deadline').value;
        const modality = document.getElementById('modality').value;
        const jobType = document.getElementById('job-type').value;
        const about = document.getElementById('about').value;
        const overview = document.getElementById('overview').value;
        const responsibilities = document.getElementById('responsibilities').value;
        const qualifications = document.getElementById('qualifications').value;
        const companyName = document.getElementById('company-name').value;

        if (!jobTitle || !location || !category || !deadline || !modality || !jobType || !about || !overview || !responsibilities || !qualifications || !companyName) {
            alert('Please fill out all required fields.');
            return;
        }

        const today = new Date().toISOString().split('T')[0];
        if (deadline < today) {
            alert('Please select a future deadline date.');
            return;
        }

        alert('Job post submitted successfully!');
        form.submit();
    });
});
