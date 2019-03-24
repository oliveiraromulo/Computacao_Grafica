void setup(){
  size(800, 800);
}

void draw(){
  float raio = 0.47*width/2;
  int n = 12;
  int i;
  translate(width/2, height/2);
  background(0);
  fill(255);
  ellipse(0, 0, width/2, width/2);
  //fill(0, 255, 0);
  beginShape(POINTS);
    for(i = 0; i<=60; i++){
      vertex(raio*cos((i*TWO_PI)/n), raio*sin((i*TWO_PI)/n));
      stroke(255, 0, 0);
      point(raio*cos((i*TWO_PI)/n), raio*sin((i*TWO_PI)/n));
    }
  endShape();
  int s = second();
  float angSec = s*TWO_PI/60 - HALF_PI;
  line(0, 0, raio*cos(angSec), raio*sin(angSec));
  int m = minute();
  float angMin = m*TWO_PI/60 - HALF_PI;
  line(0, 0, raio*cos(angMin), raio*sin(angMin));
  int h = hour()%12;
  float angHora = (TWO_PI/12)*(h+(m/60.0));
  line(0, 0, raio*cos(angHora), raio*sin(angHora));
}
