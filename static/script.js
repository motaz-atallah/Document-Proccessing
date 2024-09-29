document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault(); // Prevent default form submission
    const form = document.getElementById('uploadForm');
    const formData = new FormData(form);

    // Show loader and hide result
    document.getElementById('loader').style.display = 'block';
    document.getElementById('result-container').style.display = 'none';
    document.getElementById('result').textContent = ''; // Clear previous results

    try {
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData,
        });

        document.getElementById('loader').style.display = 'none'; // Hide loader

        const data = await response.json();
        if (response.ok) {
            // Show the result and display it
            document.getElementById('result-container').style.display = 'block';
            document.getElementById('result').innerHTML = data.result;
        } else {
            alert(data.error); // Show error message
        }
    } catch (error) {
        document.getElementById('loader').style.display = 'none'; // Hide loader
        alert('An error occurred while uploading the file.');
    }
};
