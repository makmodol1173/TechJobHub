document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const companyName = document.getElementById("company-name").value.trim();
        const year = document.getElementById("year").value.trim();
        const address = document.getElementById("address").value.trim();
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();
        const confirmPassword = document.getElementById("confirm-password").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const designation = document.getElementById("designation").value.trim();

        if (!companyName || !year || !address || !name || !email || !password || !confirmPassword || !phone || !designation) {
            alert("Please fill in all required fields.");
            return;
        }

        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailPattern.test(email)) {
            alert("Please enter a valid email address.");
            return;
        }

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return;
        }

        alert("Form submitted successfully!");
    });
});
