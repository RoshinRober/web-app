document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting the default way

    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    // Simple validation
    if (name === '' || email === '') {
        alert('Please fill in both fields.');
        return;
    }

    // Log values to console (or send them to backend in future steps)
    console.log('Name:', name);
    console.log('Email:', email);

    // Simulate successful form submission
    alert('Form submitted successfully!');
});
