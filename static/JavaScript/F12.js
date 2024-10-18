document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.querySelector('.menu-icon');
    const sidebar = document.querySelector('.sidebar');

    menuIcon.addEventListener('click', function () {
        sidebar.classList.toggle('active');
        menuIcon.classList.toggle('highlighted');
    });

    const assessifyLink = document.querySelector('.nav-links li a[href="#"]');
    const assessifyDropdown = assessifyLink.nextElementSibling;

    assessifyLink.addEventListener('click', function (e) {
        e.preventDefault();
        assessifyDropdown.classList.toggle('show');
    });

    const searchIcon = document.querySelector('.search-icon');
    searchIcon.addEventListener('click', function () {
        alert("Search functionality is under development!");
    });

    const notificationIcon = document.querySelector('.notification-icon');
    notificationIcon.addEventListener('click', function () {
        alert("No new notifications.");
    });

    const uploadBtn = document.querySelector('.upload-btn');
    uploadBtn.addEventListener('click', function () {
        alert("CV upload functionality is under development!");
    });

    const applicantListBtn = document.querySelector('.applicant-list');
    applicantListBtn.addEventListener('click', function () {
        alert("Redirecting to the applicant list.");
    });
});
