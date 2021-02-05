// HANDLE ANIMATION
const signUpButtonAnimate = document.getElementById('signUp');
const signInButtonAnimate = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButtonAnimate.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButtonAnimate.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
