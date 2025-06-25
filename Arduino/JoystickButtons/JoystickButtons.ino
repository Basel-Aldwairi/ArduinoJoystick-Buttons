const int button1 = 2;
const int button2 = 3;
const int button3 = 4;
const int button4 = 5;
const int maxButtons = 5;

const int JSx = A0;
const int JSy = A1;
const int JSb = 6;
const int lenJSHex = 10;

unsigned long hexCode = 0x0;

void process(){
  
  if(digitalRead(button1) == HIGH){
    hexCode ^= 0x1; // 0000 0001
  }
  if(digitalRead(button2) == HIGH){
    hexCode ^= 0x2; // 0000 0010
  }
  if(digitalRead(button3) == HIGH){
    hexCode ^= 0x4; // 0000 0100
  }
  if(digitalRead(button4) == HIGH){
    hexCode ^= 0x8; // 0000 1000  
  }
  if(digitalRead(JSb) == HIGH){
    hexCode ^= 0x10; // 0001 0000
  }

  unsigned long x_pos = analogRead(JSx);
  unsigned long y_pos = analogRead(JSy);
  // Serial.print("y");
  //Serial.println(y_pos);
  if(x_pos < 712 && x_pos > 312){
    x_pos = 512;
  }
  
  if(y_pos < 712 && y_pos > 312){
    y_pos = 512;
  }

  x_pos = x_pos << maxButtons;
  hexCode ^= x_pos;
  y_pos = y_pos << (maxButtons + lenJSHex);
  hexCode ^= y_pos;
  // Serial.print("y a");
  // Serial.println(y_pos);
  Serial.println(hexCode);

  hexCode = 0;
  // Serial.print("x");
  // Serial.println(x_pos);
  // Serial.print("y");
  // Serial.println(y_pos);
  
}

void setup() {
  Serial.begin(9600);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  pinMode(button4, INPUT);
  pinMode(JSb, INPUT);
   
}

void loop() {
  // delay(1);
  process();

}
