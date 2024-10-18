const textarea = document.getElementById('solution');
const charCount = document.getElementById('char-count');

textarea.addEventListener('input', function () {
    const currentLength = textarea.value.length;
    charCount.textContent = currentLength;
});

const sidebar = document.querySelector('.sidebar');
const menuIcon = document.querySelector('.menu-icon');

menuIcon.addEventListener('click', function () {
    sidebar.classList.toggle('active');
});

const submenu = document.querySelector('.nav-links li a[href="#"]');
submenu.addEventListener('click', function (e) {
    e.preventDefault(); 
    this.nextElementSibling.classList.toggle('show');
});
