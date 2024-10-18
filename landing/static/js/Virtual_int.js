const searchIcon = document.querySelector('.search-icon');
searchIcon.addEventListener('click', function() {
    const searchTerm = prompt("Enter your search query:");
    if (searchTerm) {
        alert(`You searched for: ${searchTerm}`);
    }
});

const notificationIcon = document.querySelector('.notification-icon');
notificationIcon.addEventListener('click', function() {
    alert("You have new notifications.");
});

const profileIcon = document.querySelector('.profile-icon');
profileIcon.addEventListener('click', function() {
    window.location.href = '../HTML/Profile.html';
});

const menuIcon = document.querySelector('.menu-icon');
menuIcon.addEventListener('click', function() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('active');
});

const interviewButtons = document.querySelectorAll('.interview-button');
interviewButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        const applicantName = button.previousElementSibling.textContent;
        alert(`Interview set for ${applicantName}.`);
    });
});
