document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(".form");
  const fnameInput = document.getElementById("fname");
  const lnameInput = document.getElementById("lname");
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");
  const roleInput = document.getElementById("role");

  form.addEventListener("submit", (event) => {
    clearErrors();

    const fname = fnameInput.value.trim();
    const lname = lnameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();
    const role = roleInput.value.trim();

    let isValid = true;

    // Validate First Name
    if (fname === "") {
      showError(fnameInput, "First Name is required");
      isValid = false;
    }

    // Validate Last Name
    if (lname === "") {
      showError(lnameInput, "Last Name is required");
      isValid = false;
    }

    // Validate Email
    if (email === "") {
      showError(emailInput, "Email is required");
      isValid = false;
    } else if (!isValidEmail(email)) {
      showError(emailInput, "Enter a valid email address");
      isValid = false;
    }

    // Validate Password
    if (password === "") {
      showError(passwordInput, "Password is required");
      isValid = false;
    } else if (!isValidPassword(password)) {
      showError(passwordInput, "Password must be at least 8 characters long");
      isValid = false;
    }

    // Validate Role
    if (!(role == "Recruiter" || role == "Job Seeker" || role == "Startup")) {
      showError(roleInput, "Role is required");
      isValid = false;
    }

    if (!isValid) {
      alert("Something went wrong");
      event.preventDefault();
    } else {
      console.log(fname, lname, email, password, role);
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
    [fnameInput, lnameInput, emailInput, passwordInput, roleInput].forEach(
      (input) => {
        if (input) {
          input.classList.remove("error");
        }
      }
    );
  }

  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function isValidPassword(password) {
    return password.length >= 8;
  }
});
