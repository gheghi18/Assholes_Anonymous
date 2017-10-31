// Document Hooks
var canvas = $("#dynamic-creator")[0];
var textarea = $(".card-text-area");
var dynamicText = $("#dynamic-textarea")[0];
var ctx = canvas.getContext("2d");

// Image dimensions
var width = canvas.width;
var height = canvas.height;
var x = 0;
var y = 0;

// Text variables
dynamicText.value = textarea.attr("placeholder");
textarea.keyup(getText);

// Set the styles
ctx.strokeStyle = '#000000';
ctx.lineWidth = 2;

// Setup the main display
ctx.fillStyle = '#0EC482';
ctx.fillRect(x, y, width, height);
ctx.strokeRect(x, y, width, height);

function getText()
{
	text = textarea.val();
	dynamicText.value = textarea.val();
}