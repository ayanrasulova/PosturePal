  /*NOTE this program is designed for the Arduino IDE
that contain libraries not available here:
- RF24
- nRF24L01
- Adafruit_ICM20X
- Adafruit_ICM20649
- Wire 
their implementations are show below
*/
  #include <Adafruit_ICM20649.h>
  #include <Adafruit_Sensor.h>
  #include <Wire.h>
  #include <RF24.h>
  #include <nRF24L01.h>

  RF24 radio(10,9);

  const byte address[6] = "00001";



  //This is our IMU
  Adafruit_ICM20649 icy;

  void setup() {
    radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
  Serial.begin(115200);
  while(!Serial)
    delay(10);

  Serial.println("Let's fix that posture of yours!");

  if(!icy.begin_I2C()){
    Serial.println("Icy is missing!");
      
  }  
  Serial.println("Welcome back Icy!");
  Serial.print("Accelerometer range: ");
  switch(icy.getAccelRange()){
    case ICM20649_ACCEL_RANGE_4_G:
      Serial.println("+-4G");
      break;
    case ICM20649_ACCEL_RANGE_8_G:
      Serial.println("+-8G");
      break;
    case ICM20649_ACCEL_RANGE_16_G:
      Serial.println("+-16G");
      break;
    case ICM20649_ACCEL_RANGE_30_G:
      Serial.println("+-30G");
      break;
    }
  

  uint16_t accel_divisor = icy.getAccelRateDivisor();
  float accel_rate = 1125 / (1.0 + accel_divisor);

  Serial.print("Accelerometer data rate divisor: ");
  Serial.println(accel_divisor);
  Serial.print("Accelerometer data rate (Hz) approx: ");
  Serial.println(accel_rate);

  }
  
  

  void loop(){
    // sensor events:
    sensors_event_t accel;
    sensors_event_t gyro;
    sensors_event_t temp;
    icy.getEvent(&accel, &gyro, &temp);
    byte  package [1+(3*sizeof(accel.acceleration.x))];
    package[0] = (byte)'@';
    float x = accel.acceleration.x;
    float y = accel.acceleration.y;
    float z = accel.acceleration.z;

    memcpy(package+1,&x,4);
    memcpy(package+5,&y,4);
    memcpy(package+9,&z,4);

    Serial.println("\nPackage: ");
    printPack(package);

    Serial.print("\t\tAccel X: ");
    Serial.print(accel.acceleration.x);
    Serial.print(" \tY: ");
    Serial.print(accel.acceleration.y);
    Serial.print(" \tZ: ");
    Serial.print(accel.acceleration.z);
    Serial.println(" m/s^2 ");

    radio.write(package, sizeof(package));

    delay(100);

  }

  void printPack(byte pack[]){
    Serial.print((char)pack[0]);
    float x;
    float y;
    float z;
    memcpy(&x, pack+1, 4);
    memcpy(&y, pack+5, 4);
    memcpy(&z, pack+9, 4);
    Serial.print(", ");
    Serial.print(x);
    Serial.print(", ");
    Serial.print(y);
    Serial.print(", ");
    Serial.println(z);
  }
    

