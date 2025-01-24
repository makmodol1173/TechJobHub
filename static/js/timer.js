const timerDuration = 1800;

  let remainingTime = timerDuration;
  const timerElement = document.getElementById("timer");
  const assessmentForm = document.getElementById("assessment-form");
  const timeoutMessage = document.getElementById("timeoutMessage");

  function startTimer() {
    const timerInterval = setInterval(() => {
      if (remainingTime > 0) {
        remainingTime--;
        updateTimerDisplay();
      } else {
        clearInterval(timerInterval);
        handleTimeout();
      }
    }, 1000);
  }

  function updateTimerDisplay() {
    const minutes = Math.floor(remainingTime / 60).toString().padStart(2, "0");
    const seconds = (remainingTime % 60).toString().padStart(2, "0");
    timerElement.textContent = `Time Remaining: ${minutes}:${seconds}`;
  }

  function handleTimeout() {
    assessmentForm.style.display = "none";
    timeoutMessage.style.display = "block";

  }

  window.onload = startTimer;