// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the registration form
    var form = document.getElementById('registrationForm');

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Create a FormData object to collect form data
        var formData = new FormData(form);

        // Send a POST request to the registration endpoint
        fetch('/register', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            // Check if the response is successful
            if (response.ok) {
                // Redirect to a success page or display a success message
                window.location.href = '/home'; // Change '/success' to the URL of your success page
            } else {
                // Display an error message
                console.error('Registration failed');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
