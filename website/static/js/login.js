document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('loginForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var formData = new FormData(form);

        fetch('/login', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                window.location.href = '/home'; // Redirect to the home page after successful login
            } else {
                console.error('Login failed');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});