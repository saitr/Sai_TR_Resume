// Animations
AOS.init({
  anchorPlacement: 'top-left',
  duration: 1000
});

// Add your javascript here
 // Add this JavaScript to your page or in an external script
 document.querySelector("form").addEventListener("submit", function () {
  document.getElementById("loader-container").style.display = "block"; // Show the loader container
});


  // Assuming you're using the fetch API to submit the form
document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault(); // Prevent the default form submission behavior

  document.getElementById("loader-container").style.display = "block"; // Show the loader

  // Submit the form data to your server using the fetch API
  fetch("http://127.0.0.1:8000/submit_form/", {
    method: "POST",
    body: new FormData(e.target), // Assuming 'e.target' is your form element
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the response data
      document.getElementById("loader-container").style.display = "none"; // Hide the loader
      alert('Submitted Form Successfully.')
      window.location.reload()
    })
    .catch((error) => {
      // Handle errors and hide the loader if necessary
      document.getElementById("loader-container").style.display = "none"; // Hide the loader on error
      alert('Form submission failed. Please try again.');
    });
});