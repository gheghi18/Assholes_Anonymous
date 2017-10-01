//Variables

// The avaliable modes
var modes = ["#masthead","#overview"]

// This is the current mode that the website is in and controls what is being displayed
var currentMode = 0;

// The logo
var logo = $("#logo");

// Buttons
var backButton = $(".back");
var overviewButton = $("#overviewButton");
var learnMoreButton = $("#learnmore")

// The time it takes to complete an animation
var animationTiming = 500;

// Add an event listener to buttons
logo.on("click",function()
{
	transitionTo(0);
});

backButton.on("click",function()
	{
		transitionTo(0);
	});

overviewButton.on("click",function()
	{
		transitionTo(1);
	});

learnMoreButton.on("click",function()
	{
		transitionTo(1);
	});


// Transition to a particular state
function transitionTo(mode)
{
	if (mode != currentMode)
	{
		$(modes[currentMode]).slideToggle(animationTiming,function()
		{
			$(modes[mode]).slideToggle(animationTiming);
		});
		$(modes[currentMode] + "Button").removeClass("active");
		$(modes[mode]+"Button").addClass("active");

		currentMode = mode;
	}
}


