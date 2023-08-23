// Store the elements outside of the functions
const studentForm = document.getElementById("student-form");

const datalistOptions = document.getElementById("browser");
const datalistMessageDiv = document.getElementById("alert-browser");
const selectOptions = document.getElementById("classes");
const selectMessageDiv = document.getElementById("alert-classes");
const datestartOptions = document.getElementById("datestart");
const datestartMessageDiv = document.getElementById("alert-datestart");
const quantityclassesOptions = document.getElementById("quantityclasses");
const quantityclassesMessageDiv = document.getElementById("alert-quantityclasses");
const preferedtimeOptions = document.getElementById("preferedtime");
const preferedtimeMessageDiv = document.getElementById("alert-preferedtime");
const interviewdayOptions = document.getElementById("interviewday");
const interviewdayMessageDiv = document.getElementById("alert-interviewday");
const birthdayOptions = document.getElementById("birthday");
const birthdayMessageDiv = document.getElementById("alert-birthday");



// To make the red alert appear and make the border red if no select option is selected:
studentForm.addEventListener("submit", (event) => {


  if (datalistOptions.value === "") {
    datalistOptions.style.border = "solid 1px red";
    datalistMessageDiv.style.display = "block";
    event.preventDefault();
  }

  if (selectOptions.value === "") {
    selectOptions.style.border = "solid 1px red";
    selectMessageDiv.style.display = "block";
    event.preventDefault();
  }

  if (datestartOptions.value === "") {
    datestartOptions.style.border = "solid 1px red";
    datestartMessageDiv.style.display = "block";
    event.preventDefault();
  }

  if (quantityclassesOptions.value === "") {
    quantityclassesOptions.style.border = "solid 1px red";
    quantityclassesMessageDiv.style.display = "block";
    quantityclassesOptions.scrollIntoView({ behavior: "smooth", block: "end" });
    event.preventDefault();
  }

  if (preferedtimeOptions.value === "") {
    preferedtimeOptions.style.border = "solid 1px red";
    preferedtimeMessageDiv.style.display = "block";
    preferedtimeOptions.scrollIntoView({ behavior: "smooth", block: "end" });
    event.preventDefault();
  }

  if (interviewdayOptions.value === "") {
    interviewdayOptions.style.border = "solid 1px red";
    interviewdayMessageDiv.style.display = "block";
    interviewdayOptions.scrollIntoView({ behavior: "smooth", block: "end" });
    event.preventDefault();
  }

  if (birthdayOptions.value === "") {
    birthdayOptions.style.border = "solid 1px red";
    birthdayMessageDiv.style.display = "block";
    birthdayOptions.scrollIntoView({ behavior: "smooth", block: "end" });
    event.preventDefault();
  }
});

// Add change event listener to the form elements
datalistOptions.addEventListener("change", () => handleFormElementChange(datalistOptions, datalistMessageDiv));
selectOptions.addEventListener("change", () => handleFormElementChange(selectOptions, selectMessageDiv));
datestartOptions.addEventListener("change", () => handleFormElementChange(datestartOptions, datestartMessageDiv));
quantityclassesOptions.addEventListener("change", () => handleFormElementChange(quantityclassesOptions, quantityclassesMessageDiv));
preferedtimeOptions.addEventListener("change", () => handleFormElementChange(preferedtimeOptions, preferedtimeMessageDiv));
interviewdayOptions.addEventListener("change", () => handleFormElementChange(interviewdayOptions, interviewdayMessageDiv));
birthdayOptions.addEventListener("change", () => handleFormElementChange(birthdayOptions, birthdayMessageDiv));

// Function to handle the change event
function handleFormElementChange(element, messageDiv) {
  if (element.value !== "") {
    element.style.border = "";
    messageDiv.style.display = "none";
  }
}