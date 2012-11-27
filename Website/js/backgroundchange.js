// JavaScript Document

function changeImg(imgNumber) {
	var myImages = ["file:///Macintosh HD/Users/jamiejane/Desktop/protype design/Pitt Meadows Museum - WORKING PROTOTYPE/objects/backgrounds/geometric patterns/Geometrics-by-drgirlfriend-patterns1/pattern1.jpg", "file:///Macintosh HD/Users/jamiejane/Desktop/protype design/Pitt Meadows Museum - WORKING PROTOTYPE/objects/backgrounds/geometric patterns/Geometrics-by-drgirlfriend-patterns4/pattern9.jpg", "../objects/backgrounds/geometric patterns/Geometrics-by-drgirlfriend-patterns5/pattern6.jpg", "../objects/backgrounds/geometric patterns/Geometrics-by-drgirlfriend-patterns6/pattern5.jpg"]; 
	var imgShown = document.body.style.backgroundImage;
	var newImgNumber =Math.floor(Math.random()*myImages.length);
	document.body.style.backgroundImage = 'url('+myImages[newImgNumber]+')';
}
window.onload=changeImg;