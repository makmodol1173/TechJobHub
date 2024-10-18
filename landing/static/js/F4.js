document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.form');
    const emailInput = document.getElementById('email');
    const newPasswordInput = document.getElementById('new-password');
    const confirmPasswordInput = document.getElementById('cur-password');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const email = emailInput.value.trim();
        const newPassword = newPasswordInput.value.trim();
        const confirmPassword = confirmPasswordInput.value.trim();

        // Validate email
        if (!validateEmail(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        // Validate password match
        if (newPassword !== confirmPassword) {
            alert('Passwords do not match. Please try again.');
            return;
        }

        // Simulate form submission (replace this with actual submission logic)
        alert('Form submitted successfully!');

        // You can now send the data to your server or perform other actions
    });

    // Email validation function
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});
