document.addEventListener('contextmenu', function(e) {
  e.preventDefault();
});

document.addEventListener('keydown', function(e) {
  if (e.ctrlKey && (e.key === 'v' || e.key === 'c' || e.key === 'x' || e.key === 'V' || e.key === 'C' || e.key === 'X')) {
      e.preventDefault();
  }
});