
var twitterServices = angular.module("twitter.services",[]);

twitterServices.factory("tweetData",function(){
	
	this.dataset =  [
	                 {
	                     "author": "Bill Gates",
	                     "quote": "Success is a lousy teacher. It seduces smart people into thinking they can't lose.",
	                     "image": "static/img/gates.jpg"
	                 },
	                 {
	                     "author": "Steve Jobs",
	                     "quote": "Technology is nothing. What's important is that you have a faith in people," +
	                     		" that they're basically good and smart, and if you give them tools, they'll do wonderful things with them",
	                     "image": "static/img/st.jpg"
	                 },
	                 {
	                     "author": "Steve Jobs",
	                     "quote": "If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know " +
	                     		"when you find it. And, like any great relationship, it just gets better and better as the years roll on.",
	                     "image": "static/img/st.jpg"
	                 },
	                 {
	                     "author": "Bill Gates",
	                     "quote": "The first rule of any technology used in a business is that automation applied to" +
	                     		" an efficient operation will magnify the efficiency. The second is that automation applied " +
	                     		"to an inefficient operation will magnify the inefficiency.",
	                     "image": "static/img/gates.jpg"
	                 },
	                 {
	                     "author": "mark zuckerberg",
	                     "quote": "The biggest risk is not taking any risk... In a world that changing really quickly, " +
	                     		"the only strategy that is guaranteed to fail is not taking risks.",
	                     "image": "static/img/mark.jpg"
	                 },
	                 {
	                     "author": "Steve Jobs",
	                     "quote": "Creativity is just connecting things. When you ask creative people how they did something, " +
	                     		"they feel a little guilty because they didn't really do it, they just saw something. It seemed obvious " +
	                     		"to them after a while. That's because they were able to connect experiences they've had and synthesize new things.",
	                     "image": "static/img/st.jpg"
	                 },
	                 {
	                     "author": "Bill Gates",
	                     "quote": "I think it's fair to say that personal computers have become the most empowering tool " +
	                     		"we've ever created. They're tools of communication, they're tools of creativity, and they can be shaped by their user.",
	                     "image": "static/img/gates.jpg"
	                 },
	                 {
	                     "author": "mark zuckerberg",
	                     "quote": "Think about what people are doing on Facebook today. They're keeping up with their friends " +
	                     		"and family, but they're also building an image and identity for themselves, which in a sense is " +
	                     		"their brand. They're connecting with the audience that they want to connect to." +
	                     		" It's almost a disadvantage if you're not on it now.",
	                     "image": "static/img/mark.jpg"
	                 },
	                 {
	                     "author": "mark zuckerberg",
	                     "quote": "Facebook was not originally created to be a company. It was built to accomplish a social mission -" +
	                     		" to make the world more open and connected.",
	                     "image": "static/img/mark.jpg"
	                 },
	                 {
	                     "author": "Steve Jobs",
	                     "quote": "Everyone here has the sense that right now is one of those moments when we are influencing the future.",
	                     "image": "static/img/st.jpg"
	                 }
	             ];
	
	
	return{
		dataset : this.dataset
	}
	                         
	});