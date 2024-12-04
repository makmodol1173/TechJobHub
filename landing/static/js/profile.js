// // document.addEventListener('DOMContentLoaded', function () {
//     function toggleEdit(sectionId) {
//         const section = document.getElementById(sectionId);
//         if (section.style.display === 'none' || section.style.display === '') {
//             section.style.display = 'block';
//         } else {
//             section.style.display = 'none';
//         }
//     }

//     const profilePictureUpload = document.getElementById('profile-picture-upload');
//     const profilePictureContainer = document.querySelector('.profile-picture-container');
//     const profilePicture = profilePictureContainer.querySelector('.profile-picture');
//     const editIcon = profilePictureContainer.querySelector('.edit-icon');

//     profilePictureUpload.addEventListener('change', function () {
//         const file = this.files[0];
//         if (file) {
//             const reader = new FileReader();
//             reader.onload = function (event) {
//                 profilePicture.setAttribute('src', event.target.result);
//             };
//             reader.readAsDataURL(file);
//         }
//     });

//     editIcon.addEventListener('click', function () {
//         profilePictureUpload.click();
//     });

//     const saveButtons = document.querySelectorAll('.save-button');
//     saveButtons.forEach(button => {
//         button.addEventListener('click', function () {
//             const parentSection = this.closest('.profile-edit-section');
//             if (parentSection) {
//                 parentSection.style.display = 'none';
//             }
//         });
//     });
// // });
