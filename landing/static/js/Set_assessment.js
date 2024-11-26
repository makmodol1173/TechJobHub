document.addEventListener('DOMContentLoaded', function () {
  const textareas = document.querySelectorAll('textarea');

  textareas.forEach((textarea) => {
      const maxLength = parseInt(textarea.getAttribute('maxlength'), 10);
      const charCounter = document.createElement('div');
      // charCounter.classList.add('char-counter');
      // charCounter.textContent = `0 / ${maxLength}`;
      // textarea.parentNode.appendChild(charCounter);

      textarea.addEventListener('input', () => {
          const currentLength = textarea.value.length;
          charCounter.textContent = `${currentLength} / ${maxLength}`;
      });
  });

  const form = document.querySelector('form');
  form.addEventListener('submit', (e) => {
      let isValid = true;
      textareas.forEach((textarea) => {
          if (textarea.value.trim() === '') {
              isValid = false;
              textarea.style.border = '2px solid red';
          } else {
              textarea.style.border = '1px solid #ccc';
          }
      });

      if (!isValid) {
          e.preventDefault();
          alert('Please fill out all the questions before submitting.');
      }
  });
});
