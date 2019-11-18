#include <Servo.h> //include Servo library
Servo myServo; // create servo object


void setup() { //setup
  Serial.begin(9600);  //activate Serial Monitor
  myServo.attach(9); //attach servo to pin 9
  
 
  
}

void loop() //loop section
{
  
  
  char val = Serial.read();
      if (val == '1') { // moves servo to the left if 1 is called. Stops after being turned on
         Serial.write("Left\n");
         for(int i = 0; i < 90; i++){
         myServo.write(5);
         delay(15);
         }
         
      }
      else if(val == '0'){
         Serial.write("Right\n");
         for(int i = 0; i < 90; i++){ // moves servo to the right stops after being turned off
         myServo.write(180);
         delay(15);
         }
      } 
      else{
         myServo.write(90); // turns the servo off if nothing is immediatly called
      }
    

  
}




