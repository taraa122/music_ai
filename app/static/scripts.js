// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {

    // Handle form submission
    const form = document.getElementById('music-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Create FormData object
            const formData = new FormData(form);

            // Show loading spinner or message
            document.getElementById('loading').style.display = 'block';

            // Send the form data using fetch API
            fetch('/generate_music', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Hide loading spinner
                document.getElementById('loading').style.display = 'none';

                // Display the generated music or results
                const resultContainer = document.getElementById('result');
                if (resultContainer) {
                    resultContainer.innerHTML = `
                        <h3>Generated Music</h3>
                        <audio controls>
                            <source src="${data.music_url}" type="audio/mpeg">
                            Your browser does not support the audio element.
                        </audio>
                    `;
                }
            })
            .catch(error => {
                // Hide loading spinner
                document.getElementById('loading').style.display = 'none';

                // Display an error message
                const resultContainer = document.getElementById('result');
                if (resultContainer) {
                    resultContainer.innerHTML = `
                        <p>Error generating music. Please try again.</p>
                    `;
                }
                console.error('Error:', error);
            });
        });
    }
});
