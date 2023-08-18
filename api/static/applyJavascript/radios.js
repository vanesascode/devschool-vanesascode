
// Store the elements outside of the functions
const otherRadio = document.getElementById("other-radio-input");
const otherRadioTextarea = document.getElementById("other-radio-textarea");
const socialmediaRadio = document.getElementById("socialmedia");
const googleRadio = document.getElementById("google");
const friendsRadio = document.getElementById("friends");

// To make the textarea appear if the "other" radio is checked and make it red while empty:
function appearOtherRadioTextarea() {
  if (otherRadio.checked) {
    otherRadioTextarea.style.display = "block";
    otherRadioTextarea.required = true;
    otherRadioTextarea.style.border = "solid 1px red";
    otherRadioTextarea.addEventListener("input", handleRadioTextareaInput);
  } else {
    otherRadioTextarea.style.display = "none";
    otherRadioTextarea.required = false;
    otherRadioTextarea.value = "";
    otherRadioTextarea.style.border = "";
    otherRadioTextarea.removeEventListener("input", handleRadioTextareaInput);
  }
}

function handleRadioTextareaInput() {
  if (otherRadioTextarea.value) {
    otherRadioTextarea.style.border = "";
  } else {
    otherRadioTextarea.style.border = "solid 1px red";
  }
}


// To make the textarea disappear if one of the other radios is checked:
function removeOtherRadioTextarea() {
  if (socialmediaRadio.checked || googleRadio.checked || friendsRadio.checked) {
    otherRadioTextarea.style.display = "none";
    otherRadioTextarea.required = false;
    otherRadioTextarea.value = "";
  } else {
    otherRadioTextarea.style.display = "block";
    otherRadioTextarea.required = true;
  }
}


// To make the red message appear if no radios are checked:
document.getElementById("student-form").addEventListener("submit", (event) => {
  const radioOptions = document.getElementsByName("learnaboutus");
  const isChecked = Array.from(radioOptions).some((option) => option.checked);

  if (!isChecked) {
    event.preventDefault(); // Prevent form submission
    const selectRadioDiv = document.getElementById("alert-radios");
    selectRadioDiv.textContent =
      "Please tell us how you learned about us before submitting the form.";
    selectRadioDiv.style.color = "red";
    const inputElement = document.getElementById("level");
    inputElement.scrollIntoView({ behavior: "smooth", block: "end" });
  }
});

// To make the red message disappear:
document.getElementById("student-form").addEventListener("change", (event) => {
  const radioOptions = document.getElementsByName("learnaboutus");
  const isChecked = Array.from(radioOptions).some((option) => option.checked);

  if (isChecked) {
    const messageDiv = document.getElementById("alert-radios");
    messageDiv.textContent = "";
  }
});



