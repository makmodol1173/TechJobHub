document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("assessment-form");

  form.addEventListener("submit", function (event) {
      event.preventDefault();

      const marks = [
          document.getElementById("mark-1"),
          document.getElementById("mark-2"),
          document.getElementById("mark-3"),
          document.getElementById("mark-4"),
          document.getElementById("mark-5"),
          document.getElementById("mark-6"),
          document.getElementById("mark-7"),
          document.getElementById("mark-8"),
          document.getElementById("mark-9"),
          document.getElementById("mark-10")
      ];

      let allValid = true;
      marks.forEach(function (markInput) {
          const markValue = markInput.value.trim();

          if (isNaN(markValue) || markValue < 0 || markValue > 10) {
              markInput.style.borderColor = "#FF0000";
              allValid = false;
          } else {
              markInput.style.borderColor = "#ccc";
          }
      });

      if (allValid) {
          alert("Marks submitted successfully!");
          form.submit();
      } else {
          alert("Please enter valid marks between 0 and 10 for all questions.");
      }
  });
});
