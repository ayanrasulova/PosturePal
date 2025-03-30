document.addEventListener("DOMContentLoaded", function () {
    const elements = document.querySelectorAll(".fade-and-scroll");
  
    function checkVisibility() {
      const triggerBottom = window.innerHeight * 0.8;
  
      elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementBottom = element.getBoundingClientRect().bottom;
  
        // Fade in when the element is in the viewport
        if (elementTop < triggerBottom && elementBottom >= 0) {
          element.classList.add("visible");
        } 
        // Fade out when the element is out of the viewport
        else if (elementBottom < 0 || elementTop > window.innerHeight) {
          element.classList.remove("visible");
        }
      });
    }
  
    window.addEventListener("scroll", checkVisibility);
    checkVisibility();  // Check initial visibility on page load
  });
  