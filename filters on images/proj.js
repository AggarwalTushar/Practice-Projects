var image=null;
var img=null;
var img1=null;
var img2=null;
var img3=null;
var img4=null;
var pixel;
var can;
var avg;
var c;
function upload(){
	var input=document.getElementById("fg");
	image=new SimpleImage(input);
	img=new SimpleImage(input);
	img1=new SimpleImage(input);
	img2=new SimpleImage(input);
	img3=new SimpleImage(input);
	img4=new SimpleImage(input);
	can=document.getElementById("f");
	image.drawTo(can);
}
function dim(){
	var c1=document.getElementById("dim");
	var ct=c1.getContext("2d");
	ct.fillStyle="black";
	ct.font = "40px Georgia";
	ct.fillText(image.getWidth().toString()+"x"+image.getWidth().toString(),30,30);
}
function clearcanvas(){
	c=can.getContext("2d");
	c.clearRect(0,0,can.width,can.height);
}
function grayscale(){
  if(img==null || !img.complete()){
  	alert("Image not Loaded");
  	return;
  }
  clearcanvas();
  for(var pixel of img.values()){
    var n=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
    pixel.setRed(n);
    pixel.setBlue(n);
    pixel.setGreen(n);
  }
  img.drawTo(can);
}
function red1(){
  if(img1==null || !img1.complete()){
  	alert("Image not Loaded");
  	return;
  }
  clearcanvas();
  for(var pixel of img1.values()){
    var avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue())/3;
    if (avg < 128) {
      pixel.setRed(avg*2);
      pixel.setGreen(0);
      pixel.setBlue(0);
        }
    else {
      pixel.setRed(255);
      pixel.setGreen((avg*2)-255);
      pixel.setBlue((avg*2)-255);
    	}
    }
    img1.drawTo(can);
}
function reset(){
	clearcanvas();
	if(image!=null)image.drawTo(can);
}
function rainbow() {
	if(img2==null || !img2.complete()){
  	alert("Image not Loaded");
  	return;
  }
  var Height = img2.getHeight();
  var h = parseInt(Height) / 7;
  var Y;
  var X;
  var red;
  var blue;
  var green;
  for (pixel of img2.values()) {
    X = pixel.getX();
    Y = pixel.getY();
	avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
    if (Y >= 6 * h) {
      doRed();
    } else if (Y >= (5 * h)) {
      doOrange();
    } else if (Y >= (4 * h)) {
      doYellow();
    } else if (Y >= (3 * h)) {
      doGreen();
    } else if (Y >= (2 * h)) {
      doBlue();
    } else if (Y >= h) {
      doIndigo();
    } else {
      doViolet();
    }
  }
  img2.drawTo(can);
}

function doViolet() {
  if (avg < 128) {
    red = 1.6 * avg;
    green = 0;
    blue = 1.6 * avg;
  } else {
    red = 0.4 * avg + 153 ;
    green = 2 * avg - 255;
    blue = 0.4 * avg + 153 ;
  }
  pixel.setRed(red);
  pixel.setGreen(green);
  pixel.setBlue(blue);
}

function doIndigo() {
  if (avg < 128) {
    red = .8 * avg;
    green = 0;
    blue = 2 * avg;
  } else {
    red = 1.2 * avg - 51;
    green = 2*avg - 255;
    blue = 255;
  }
  pixel.setRed(red);
  pixel.setGreen(green);
  pixel.setBlue(blue);
}

function doBlue() {
 if (avg < 128) {
    red = 0;
    green = 0;
    blue = 2*avg;
  } else {
    red = 2*avg-255;
    green =2*avg-255;
    blue = 255;
  }
  pixel.setRed(red);
  pixel.setGreen(green);
  pixel.setBlue(blue);
}
function doGreen() {
  if (avg < 128) {
    red = 0;
    green = 2*avg;
    blue = 0;
  } else {
    red = 2*avg-255;
    green = 255;
    blue = 2*avg-255;
  }
  pixel.setRed(red);
  pixel.setGreen(green);
  pixel.setBlue(blue);
}

function doYellow() {
  if (avg < 128) {
    red = 2 * avg;
    green = 2 * avg;
    blue = 0;
  } else {
    red = 255;
    green = 255;
    blue = 2 * avg - 255;
  }
  pixel.setRed(red);
  pixel.setGreen(green);
  pixel.setBlue(blue);
}

function doOrange() {
   if (avg < 128) {
    red = 2 * avg;
    green = .8 * avg;
    blue = 0;
  } else {
    red = 255;
    green = 1.2 * avg - 51;
    blue =  2 * avg - 255;
  }
  pixel.setRed(red);
  pixel.setGreen(green);
  pixel.setBlue(blue);
}

function doRed() {
  if (avg < 128) {
    red = 2*avg;
    green = 0;
    blue = 0;
  } else {
    red = 255;
    green = 2*avg-255;
    blue = 2*avg-255;
  }
  pixel.setRed(red);
  pixel.setGreen(green);
  pixel.setBlue(blue);
}
function makeblur(){
  	if(img3==null || !img3.complete()){
  	alert("Image not Loaded");
  	return;
  }
  for(var pixel of image.values()) {
    var x = pixel.getX();
    var y = pixel.getY();
    if(isBlur()) {
      img3.setPixel(x, y, getNearbyPxl(image.getPixel(x, y)));
    }
    else {
      img3.setPixel(x, y, image.getPixel(x, y));
    }
  }
  img3.drawTo(can);
}


function isBlur() {
  if(Math.random() < 0.5) {
    return false;
  }
  else {
    return true;
  }
}
function getNearbyPxl(aPixel) {
  // untrimmed x component of aPixel's nearby pixel
  var x = aPixel.getX() + Math.floor(Math.random() * 41) - 20;
  // untrimmed y component of aPixel's nearby pixel
  var y = aPixel.getY() + Math.floor(Math.random() * 41) - 20;
  var Xmax = image.getWidth();
  var Ymax = image.getHeight();
  
  if(x > Xmax - 1) {
    x = 2 * Xmax - x - 1;
  }
  
  if(x < 0) {
    x = Math.abs(x);
  }
  
  if(y > Ymax - 1) {
    y = 2 * Ymax - y - 1;
  }
  
  if(y < 0 ) {
    y = Math.abs(y);
  }
  var pxl = image.getPixel(x, y);
  return pxl;
}