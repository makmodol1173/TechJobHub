const assessifyBtn = document.getElementById("assessifyBtn");
assessifyBtn.addEventListener("click",()=>{
  const assessifyDec = document.getElementById("assessifyDec");
  console.log(assessifyDec)
  if(assessifyDec.style.display==="none"){
    assessifyDec.style.display="block";
  }else{
    assessifyDec.style.display="none";
  }
});

document.addEventListener('contextmenu', function(e) {
  e.preventDefault();
});

document.addEventListener('keydown', function(e) {
  if (e.ctrlKey && (e.key === 'v' || e.key === 'c' || e.key === 'x')) {
      e.preventDefault();
  }
});