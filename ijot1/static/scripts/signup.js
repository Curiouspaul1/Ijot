//SignUp Page
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

// Add event listeners to add and remove class from elements
signUpButton.addEventListener('click',() => 
container.classList.add('right-panel-active'));

signInButton.addEventListener('click',() => 
container.classList.remove('right-panel-active'));



