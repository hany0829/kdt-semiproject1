document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
  
    // Perform your login logic here
    console.log('Username:', username, 'Password:', password);
  });
  