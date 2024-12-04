// document.addEventListener('DOMContentLoaded', function () {
//     const form = document.querySelector('.job-post-form');
    
//     form.addEventListener('submit', function (event) {
//         event.preventDefault();

//         const jobTitle = document.getElementById('job-title').value.trim();
//         const about = document.getElementById('about').value.trim();
//         const location = document.getElementById('location').value.trim();
//         const responsibilities = document.getElementById('responsibilities').value.trim();
//         const education = document.getElementById('education').value.trim();
//         const qualifications = document.getElementById('qualifications').value.trim();
//         const deadline = document.getElementById('deadline').value.trim();
//         const jobType = document.getElementById('job-type').value.trim();

//         if (!jobTitle || !about || !location || !responsibilities || !qualifications || !deadline || !jobType) {
//             alert('Please fill out all required fields.');
//             return;
//         }

//         const today = new Date().toISOString().split('T')[0];
//         if (deadline < today) {
//             alert('Please select a future deadline date.');
//             return;
//         }

        // alert('Job post submitted successfully!');
    // });
// });
//         alert('Job post submitted successfully!');
//     });
// });
