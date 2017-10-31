// Document Hooks
var canvases = $(".card");
var texts = $(".card-text");
var textboxes = $(".dynamic-textarea");

var width = canvases[0].width;
var height = canvases[0].height;

for (c = 0; c < canvases.length; c ++)
{
	renderCanvas(canvases[c].getContext("2d"),texts[c].value,textboxes[c]);
}

function renderCanvas(ctx,text,textarea)
{
	// Set the styles
	ctx.strokeStyle = '#000000';
	ctx.lineWidth = 2;

	// Setup the main display
	ctx.fillStyle = '#0EC482';
	ctx.fillRect(0, 0, width, height);
	ctx.strokeRect(0, 0, width, height);

	textarea.value = text;
}