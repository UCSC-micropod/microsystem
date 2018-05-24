// NOTE: Must have Arduino library RF24 (by TMRh20) installed

#include "SPI.h"
#include "RF24.h"
#include "nRF24L01.h"

//CE & CSN pins (will use later for changing operating mode)
RF24 radio(9,10);

void setup(void) {
  Serial.begin(9600);
  Serial.println("Tx Starting");
  
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.setDataRate(RF24_1MBPS);
 // radio.setRetries(3,5);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
  radio.enableDynamicPayloads();
  radio.powerUp();
  radio.printDetails();

}

void loop() {

 const char text[] = "/ Hello Raspberry Pi / ";
 bool result;
 result = radio.write(&text, sizeof(text));
 Serial.print("Data Sent: ");
 Serial.print(text);
 if (result) {
  Serial.println("Tx success");
 }
 else {
  Serial.println("Tx failed");
 }
 //make sure to use millis() later
 delay(1000);

}
