
var casper = require('casper').create();
var x = require('casper').selectXPath;

//file writer?
var fs = require('fs');

function getTweets(){
	var tweets = document.getElementsByClassName('js-tweet-text');
	return Array.prototype.map.call(tweets, function(e){
			return e.innerText;
	});
}

function getTweeters(){
	var tweeters = document.getElementsByClassName('fullname show-popup-with-id');
	return Array.prototype.map.call(tweeters, function(e){
			return e.innerText;
	});
}
casper.start('https://twitter.com/realDonaldTrump');
//try to grab more than 3 tweets --> doesn't work?? Got 10 tweets once.

casper.then(function scrollyScroll(){
	//this.scrollToBottom();
	this.wait(3000);
	this.captureSelector("trump.jpg", "html");
});

casper.then(function() { 
	var tweets1 = this.evaluate(getTweets);
	var tweeters1 = this.evaluate(getTweeters);
	
	//start new file with overwrite
	fs.write('trump.csv', "Tweeter,Tweet\n", "w");
	
	this.echo("\n\n" + tweets1.length + " Tweets found...");
	
	for(i=0; i < tweets1.length; i++){
		this.echo("\n\nTweeter: " + tweeters1[i] + "\nTweet: " + tweets1[i]);
		fs.write('trump.csv', tweeters1[i].trim() + "," + tweets1[i].trim()+ "\n", "a");
	}
	
	fs.write('trump.html', '<div style="background-color: #f9caf9; display: inline-block;"><h1> Latest <span style="color: blue;">Donald</span> <span style="color: red;">Trump</span> Tweets <h1><table style="border: 1px solid black; border-collapse: collapse; "><tr><th>Tweeter</th><th>Tweet</th></tr>', 'w');
	for(i=0; i < tweets1.length; i++){
		fs.write('trump.html', '<tr><td style="font-weight: bold;>'+tweeters1[i].trim() + "</td>" + "<td>" + tweets1[i].trim()+ '</td></tr>', "a");
	}
	fs.write('trump.html', '</table></div>', "a");
});

casper.run();