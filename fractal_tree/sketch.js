var angle1 = 0;
var angle2 = 0;
var branchdiv = 0;

function setup() {
  createCanvas(windowWidth, windowHeight);
  sliderangle1 = createSlider(0, TWO_PI, PI/4, 0.01);
  sliderangle2 = createSlider(0, TWO_PI, PI/4, 0.01);
  sliderbranchdiv = createSlider(0, 0.67, 0.67, 0.01);
}

function draw() {
  background(0);
  stroke(255, 255, 0);
  angle1 = sliderangle1.value();
  angle2 = sliderangle2.value();
  branchdiv = sliderbranchdiv.value();
  translate(windowWidth/2, height);
  branch(200);
}
function move(num) {
  return random(noise(-1,1))+num;
}
function branch(len){
  line(0, 0, 0, -move(len));
  translate(0, -move(len));
    if (len>4){
    push();
    rotate(angle1);
    branch(len*branchdiv);
    pop();
    rotate(-angle2);
    branch(len*branchdiv);
  }
}
