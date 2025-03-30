document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".card");
  
    function checkVisibility() {
      const triggerBottom = window.innerHeight * 0.8;
  
      cards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top;
        const cardBottom = card.getBoundingClientRect().bottom;
  
        // Fade in when the card is in the viewport
        if (cardTop < triggerBottom && cardBottom >= 0) {
          card.classList.add("visible");
        } 
        // Fade out when the card is out of the viewport
        else if (cardBottom < 0 || cardTop > window.innerHeight) {
          card.classList.remove("visible");
        }
      });
    }
  
    window.addEventListener("scroll", checkVisibility);
    checkVisibility();  // Check initial visibility on page load
  });
  