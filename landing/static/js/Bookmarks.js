document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.querySelector('.bookmark-search input');
    const bookmarkItems = document.querySelectorAll('.bookmark-item');

    searchInput.addEventListener('input', function () {
        const filter = searchInput.value.toLowerCase();
        bookmarkItems.forEach(item => {
            const title = item.querySelector('.bookmark-details h3').innerText.toLowerCase();
            const website = item.querySelector('.bookmark-details p').innerText.toLowerCase();
            if (title.includes(filter) || website.includes(filter)) {
                item.style.display = 'flex';
            } else {
                item.style.display = 'none';
            }
        });
    });

    const navLinks = document.querySelectorAll('.nav-links li a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function () {
            navLinks.forEach(link => link.classList.remove('active1'));
            this.classList.add('active1');
        });
    });
});
