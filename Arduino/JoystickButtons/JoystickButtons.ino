const int button1 = 2;
const int button2 = 3;
const int button3 = 4;
const int button4 = 5;

const int JSx = A0;
const int JSy = A1;
const int JSb = 6;

void process(){
  
  if(digitalRead(button1) == HIGH){
    Serial.println(1);
  }
  if(digitalRead(button2) == HIGH){
    Serial.println(2);
  }
  if(digitalRead(button3) == HIGH){
    Serial.println(3);
  }
  if(digitalRead(button4) == HIGH){
    Serial.println(4);
  }
  if(digitalRead(JSb) == HIGH){
    Serial.println(5);
  }

  int x_pos = analogRead(JSx);
  int y_pos = analogRead(JSy);

  Serial.print("x");
  Serial.println(x_pos);
  Serial.print("y");
  Serial.println(y_pos);
  
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
  delay(120);
  process();

}
