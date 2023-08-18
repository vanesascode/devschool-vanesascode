const inputMockElement = document.getElementById('mockinput');
const messageMockElement = document.getElementById('alert-mockinput');
const inputHoursElement = document.getElementById('quantityhours');
const messageHoursElement = document.getElementById('alert-quantityhours');
const inputfileElement = document.getElementById('file');
const messagefileElement = document.getElementById('alert-file');
const inputLinkedinElement = document.getElementById('linkedin');
const messageLinkedinElement = document.getElementById('alert-linkedin');
const inputfavcolorElement = document.getElementById('favcolor');
const messagefavcolorElement = document.getElementById('alert-favcolor');
const inputfavmonthElement = document.getElementById('favmonth');
const messagefavmonthElement = document.getElementById('alert-favmonth');

function handleMockInputFocus() {
  messageMockElement.style.display = 'block';
}

function handleMockInputBlur() {
  messageMockElement.style.display = 'none';
}

function handleHoursInputFocus() {
  messageHoursElement.style.display = 'block';
}

function handleHoursInputBlur() {
  messageHoursElement.style.display = 'none';
}

function handleFileInputFocus() {
  messagefileElement.style.display = 'block';
}

function handleFileInputBlur() {
  messagefileElement.style.display = 'none';
}

function handleLinkedinInputFocus() {
  messageLinkedinElement.style.display = 'block';
}

function handleLinkedinInputBlur() {
  messageLinkedinElement.style.display = 'none';
}

function handleFavcolorInputFocus() {
  messagefavcolorElement.style.display = 'block';
}

function handleFavmonthInputFocus() {
  messagefavmonthElement.style.display = 'block';
}

function handleFavmonthInputBlur() {
  messagefavmonthElement.style.display = 'none';
}

inputMockElement.addEventListener('focus', handleMockInputFocus);
inputMockElement.addEventListener('blur', handleMockInputBlur);
inputHoursElement.addEventListener('focus', handleHoursInputFocus);
inputHoursElement.addEventListener('blur', handleHoursInputBlur);
inputfileElement.addEventListener('focus', handleFileInputFocus);
inputfileElement.addEventListener('blur', handleFileInputBlur);
inputLinkedinElement.addEventListener('focus', handleLinkedinInputFocus);
inputLinkedinElement.addEventListener('blur', handleLinkedinInputBlur);
inputfavcolorElement.addEventListener('focus', handleFavcolorInputFocus);
//it's on purpose that the blue message for the color input stays ;) 
inputfavmonthElement.addEventListener('focus', handleFavmonthInputFocus);
inputfavmonthElement.addEventListener('blur', handleFavmonthInputBlur);
