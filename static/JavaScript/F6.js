document.addEventListener('DOMContentLoaded', function () {
    
    const enterButton = document.querySelector('.enter-button');
    enterButton.addEventListener('click', function () {
        window.location.href = 'job-listings.html'; // Redirect to a job listings page
    });

    const categories = document.querySelectorAll('.category');
    
    categories.forEach(function (category) {
        category.addEventListener('mouseenter', function () {
            category.style.transform = 'scale(1.05)';
            category.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
        });
        
        category.addEventListener('mouseleave', function () {
            category.style.transform = 'scale(1)';
            category.style.boxShadow = 'none';
        });
    });

    const searchIcon = document.querySelector('.search-icon');
    searchIcon.addEventListener('click', function () {
        const searchQuery = prompt('Enter a job title or keyword to search:');
        if (searchQuery) {
            window.location.href = `search-results.html?query=${encodeURIComponent(searchQuery)}`;
        }
    });

    const notificationIcon = document.querySelector('.notification-icon');
    notificationIcon.addEventListener('click', function () {
        alert('You have no new notifications!');
    });

    const profileIcon = document.querySelector('.profile-icon');
    profileIcon.addEventListener('click', function () {
        window.location.href = 'profile.html'; 
    });

    const menuIcon = document.querySelector('.menu-icon');
    menuIcon.addEventListener('click', function () {
        alert('Menu button clicked! Implement your menu logic here.');
    });
});
