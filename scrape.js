

var casper = require('casper').create();
var x = require('casper').selectXPath;
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
casper.start('http://twitter.com/login');

casper.then(function success() {
           this.sendKeys(x('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input'), "brooklyyounce@gmail.com");
		   this.echo('--> Entering email...');
       });
	   
casper.then(function success() {
           this.sendKeys(x('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input'), "llamas92");
		   this.echo('--> Entering password...');
       });
	   
casper.then(function success() {
           this.click(x('//*[@id="page-container"]/div/div[1]/form/div[2]/button'));
		   this.echo('--> Clicking login...');
       });

casper.then(function scrollyScroll(){
	//this.scrollToBottom();
	this.wait(3000);
	this.captureSelector("tweets.jpg", "html");
});

casper.then(function() { 
	var tweets1 = this.evaluate(getTweets);
	var tweeters1 = this.evaluate(getTweeters);
	
	//start new file with overwrite
	fs.write('tweets.csv', "Tweeter,Tweet\n", "w");
	
	this.echo("\n\n" + tweets1.length + " Tweets found...");
	
	//writing csv doesn't work correctly
	//who cares
	for(i=0; i < tweets1.length; i++){
		this.echo("\n\nTweeter: " + tweeters1[i] + "\nTweet: " + tweets1[i]);
		fs.write('tweets.csv', tweeters1[i].trim() + "," + tweets1[i].trim()+ "\n", "a");
	}
});

casper.run();