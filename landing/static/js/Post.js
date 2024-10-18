const menuIcon = document.querySelector('.menu-icon');
menuIcon.addEventListener('click', function() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
});

const searchIcon = document.querySelector('.search-icon');
searchIcon.addEventListener('click', function() {
    const searchTerm = prompt("Enter your search query:");
    if (searchTerm) {
        alert(`You searched for: ${searchTerm}`);
    }
});

const notificationIcon = document.querySelector('.notification-icon');
notificationIcon.addEventListener('click', function() {
    alert("You have 5 new notifications.");
});

const profileIcon = document.querySelector('.profile-icon');
profileIcon.addEventListener('click', function() {
    alert("Redirecting to your profile page.");
});

const applyButton = document.querySelector('.job-card a');
applyButton.addEventListener('click', function(event) {
    event.preventDefault();
    alert("Redirecting to the job application page.");
});
