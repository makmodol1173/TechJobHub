document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".form");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
  
    form.addEventListener("submit", (event) => {
      clearErrors();
  
      const email = emailInput.value.trim();
      const password = passwordInput.value.trim();
  
      let isValid = true;
  
      if (email === "") {
        showError(emailInput, "Email is required");
        isValid = false;
      } else if (!isValidEmail(email)) {
        showError(emailInput, "Enter a valid email address");
        isValid = false;
      }
  
      if (password === "") {
        showError(passwordInput, "Password is required");
        isValid = false;
      }
  
      if (!isValid) {
        alert("Something went wrong");
        event.preventDefault();
      } else {
        console.log(email, password);
      }

    });
  
    function showError(input, message) {
      const error = document.createElement("small");
      error.classList.add("error-message");
      error.innerText = message;
      input.classList.add("error");
      input.parentNode.insertBefore(error, input.nextSibling);
    }
  
    function clearErrors() {
      const errors = document.querySelectorAll(".error-message");
      errors.forEach((error) => error.remove());
      [emailInput, passwordInput].forEach((input) =>
        input.classList.remove("error")
      );
    }
  
    function isValidEmail(email) {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }
  });
  