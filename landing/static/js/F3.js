document.addEventListener('DOMContentLoaded', (event) => {
    const signUpBtn = document.querySelector('.sign-up-btn');
    const form = document.querySelector('.form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const first_name = document.getElementById('first_name').value;
        const last_name = document.getElementById('last_name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const role = document.getElementById('role').value;
 
        window.location.href = '../HTML/F6.html';
    });
});