#include <Servo.h>

Servo myServo;


void setup() {
  Serial.begin(9600); 
  myServo.attach(9);
  
 
  
}

void loop()
{
  
  
  char val = Serial.read();
      if (val == '1') {
         Serial.write("Left\n");
         for(int i = 0; i < 90; i++){
         myServo.write(5);
         delay(15);
         }
         
      }
      else if(val == '0'){
         Serial.write("Right\n");
         for(int i = 0; i < 90; i++){
         myServo.write(180);
         delay(15);
         }
      } 
      else{
         myServo.write(90);
      }
    

  
}




