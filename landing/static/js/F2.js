document.addEventListener('DOMContentLoaded', (event) => {
    const signInBtn = document.querySelector('.sign-in-btn');
    const form = document.querySelector('.form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
 
        window.location.href = '../HTML/F6.html';
    });
});
