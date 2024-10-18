const assessifyMenu = document.querySelector('.nav-links li a[href="#"]');
assessifyMenu.addEventListener('click', function(event) {
    event.preventDefault();
    const subMenu = assessifyMenu.nextElementSibling;
    subMenu.classList.toggle('show');
});

const menuIcon = document.querySelector('.menu-icon');
menuIcon.addEventListener('click', function() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('active');
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
    alert("You have new notifications.");
});

const profileIcon = document.querySelector('.profile-icon');
profileIcon.addEventListener('click', function() {
    window.location.href = '../HTML/Profile.html';
});

const companyRatings = document.querySelectorAll('.company');
companyRatings.forEach(function(company) {
    company.addEventListener('click', function() {
        const rating = company.querySelector('.score').textContent;
        alert(`You clicked on ${company.querySelector('b').textContent}, with a rating of ${rating}`);
    });
});
