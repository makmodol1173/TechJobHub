document.addEventListener('DOMContentLoaded', function () {
    function toggleEdit(sectionId) {
        const section = document.getElementById(sectionId);
        if (section.style.display === 'none' || section.style.display === '') {
            section.style.display = 'block';
        } else {
            section.style.display = 'none';
        }
    }

    const profilePictureUpload = document.getElementById('profile-picture-upload');
    const profilePictureContainer = document.querySelector('.profile-picture-container');

    profilePictureUpload.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (event) {
                profilePictureContainer.querySelector('.profile-picture').setAttribute('src', event.target.result);
            };
            reader.readAsDataURL(file);
        }
    });
});
