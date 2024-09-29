// Wait for the DOM to fully load before running the script
document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("file");
  const fileLabel = document.querySelector(".custom-file-label");

  fileInput.addEventListener("change", function () {
    // Check if any files are selected
    if (fileInput.files.length > 0) {
        const fileName = fileInput.files[0].name; // Get the name of the first selected file
      fileLabel.textContent = fileName; // Update the label text to show the selected file name
    } else {
      fileLabel.textContent = "Choose file..."; // Reset to default if no file is selected
    }
  });
});

document.getElementById("uploadForm").onsubmit = async function (event) {
  event.preventDefault(); // Prevent default form submission
  const form = document.getElementById("uploadForm");
  const formData = new FormData(form);

  // Show loader and hide result
  document.getElementById("loader").style.display = "block";
  document.getElementById("result-container").style.display = "none";
  document.getElementById("result").textContent = ""; // Clear previous results

  try {
    const response = await fetch(form.action, {
      method: "POST",
      body: formData,
    });

    document.getElementById("loader").style.display = "none"; // Hide loader

    const data = await response.json();
    if (response.ok) {
      // Show the result and display it
      document.getElementById("result-container").style.display = "block";
      document.getElementById("result").innerHTML = data.result;
    } else {
      alert(data.error); // Show error message
    }
  } catch (error) {
    document.getElementById("loader").style.display = "none"; // Hide loader
    alert("An error occurred while uploading the file.");
  }
};
