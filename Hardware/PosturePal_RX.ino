/*NOTE this program is designed for the Arduino IDE
that contain libraries not available here:
- RF24
- nRF24L01
- SPI
their implementations are show below
*/

#include <RF24.h>
#include <RF24_config.h>
#include <nRF24L01.h>
#include <printf.h>
#include <SPI.h>



byte buffer[13];


RF24 radio (10,9);

const byte address[6] = "00001";
byte positionData[13];

void setup() {
  Serial.begin(115200);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
  //Serial.println("Begin!");
}


void loop() {
  if(radio.available()){
    radio.read(buffer,sizeof(buffer));
    
    //start byte has been found, proper package confirmed
    if((char) buffer[0]== '@'){
      positionData[0] = buffer[0];
      memcpy(positionData+1, buffer+1, sizeof(positionData)-1);
      //after ensuring integrity of package, it gets passed on to computer
      Serial.write(positionData, sizeof(positionData));
    }
    else {
      Serial.println("Invalid package");
    }
  }
  delay(100);
}

//debugging function to visualize data a few steps early
void printData (byte data []){
  float package[3];
  memcpy(package, data+1, 12);
  Serial.print("X: ");
  Serial.println(package[0]);
  Serial.print("Y: ");
  Serial.println(package[1]);
  Serial.print("Z: ");
  Serial.println(package[2]);
  
}




