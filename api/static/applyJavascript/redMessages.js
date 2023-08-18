

//validating when the form is submitted:


function validateInput(inputName, alertName) {
  const inputElements = Array.from(document.getElementsByName(inputName));
  const alertDiv = document.getElementById(alertName);
  const isEmpty = inputElements.some((element) => element.value.trim() === "");


  inputElements.forEach((element) => {
    element.style.border = isEmpty ? "solid 1px red" : "solid 1px rgb(214, 212, 212)";
    element.scrollIntoView({ behavior: "smooth", block: "end" });
    element.action = isEmpty ? event.preventDefault() : "";
  });
  alertDiv.style.display = isEmpty ? "block" : "none";
}

document.getElementById("student-form").addEventListener("submit", (event) => {
  validateInput("name", "alert-name");
  validateInput("surname", "alert-surname");
  validateInput("telephone", "alert-telephone");
  validateInput("email", "alert-email");
  validateInput("password", "alert-password");
  validateInput("passwordconfirmation", "alert-passwordconfirmation");
  validateInput("comments", "alert-comments");
});



// Validating when the inputs are changed: 

function removeInputErrors(input, alert, regex) {
  const value = input.value.trim();
  const isValid = regex.test(value);

  input.style.border = isValid ? "solid 1px rgb(214, 212, 212)" : "solid 1px red";
  alert.style.visibility = isValid ? "hidden" : "visible";
}

const nameInput = document.getElementById("name");
const nameAlert = document.getElementById("alert-name");
const nameRegex = /^[A-Za-z]+$/;
nameInput.addEventListener("input", function (e) {
  removeInputErrors(nameInput, nameAlert, nameRegex);
});

const surnameInput = document.getElementById("surname");
const surnameAlert = document.getElementById("alert-surname");
const surnameRegex = /^[A-Za-z]+$/;
surnameInput.addEventListener("input", function (e) {
  removeInputErrors(surnameInput, surnameAlert, surnameRegex);
});

const telephoneInput = document.getElementById("telephone");
const telephoneAlert = document.getElementById("alert-telephone");
const telephoneRegex = /^[0-9]+$/;
telephoneInput.addEventListener("input", function (e) {

  removeInputErrors(telephoneInput, telephoneAlert, telephoneRegex);
});

const emailInput = document.getElementById("email");
const emailAlert = document.getElementById("alert-email");
const emailRegex = /\S+@\S+\.\S+/;
emailInput.addEventListener("input", function (e) {
  removeInputErrors(emailInput, emailAlert, emailRegex);
});

const passwordInput = document.getElementById("password");
const passwordAlert = document.getElementById("alert-password");
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
passwordInput.addEventListener("input", function (e) {
  removeInputErrors(passwordInput, passwordAlert, passwordRegex);
});

const commentsInput = document.getElementById("comments");
const commentsAlert = document.getElementById("alert-comments");
const commentsRegex = /^[A-Za-z0-9]+$/;
commentsInput.addEventListener("input", function (e) {
  removeInputErrors(commentsInput, commentsAlert, commentsRegex);
});


//Confirmation password:

function removeInputErrorsConfirmationPassword(input, alert, matchInput) {
  const value = input.value.trim();
  const isValid = value === matchInput.value.trim();

  input.style.border = isValid ? "solid 1px rgb(214, 212, 212)" : "solid 1px red";
  alert.style.visibility = isValid ? "hidden" : "visible";
}

const passwordconfirmationInput = document.getElementById("passwordconfirmation");
const passwordconfirmationAlert = document.getElementById("alert-passwordconfirmation");
passwordconfirmationInput.addEventListener("input", function (e) {
  removeInputErrorsConfirmationPassword(passwordconfirmationInput, passwordconfirmationAlert, passwordInput);
});











