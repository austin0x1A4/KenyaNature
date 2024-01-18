// Page transitions
const transitions = document.querySelectorAll('.intro-transition');

transitions.forEach(trans => {
  // Remove 'hide' class to make elements visible
  trans.classList.remove('hide');
  // Set opacity to 1 for a smooth transition
  trans.style.opacity = 1;
});

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Set the text content of the website description
  const websiteDescription = document.getElementById('website-description');
  if (websiteDescription) {
    websiteDescription.textContent = 'This is a website designed to showcase the natural endowment including forestry and energy sources within Kenya.';
  }
});

