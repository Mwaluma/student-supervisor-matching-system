// // HANDLE SUBMIT
// const formToJSON = elements => [].reduce.call(elements, (data, element) => {
//   data[element.name] = element.value;
//   return data;
// }, {});
//
// const handleFormSubmit = event => {
//   event.preventDefault();
//   const data = formToJSON(form.elements);
//   const dataContainer = document.getElementsByClassName('display')[0]; //TESTER
//   dataContainer.textContent = JSON.stringify(data, null, " ");
//   //console.log(JSON.stringify(form.elements));
// };
//
// const form = document.getElementsByClassName('form-container sign-up-container')[0];
// form.addEventListener('submit', handleFormSubmit);


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
