#include<Wire.h>

//------------------------------------------------------------------------//
#define IGT1 7
#define IGT2 6
#define IGT3 5
#define IGT4 4
//------------------------------------------------------------------------//
String data = "IGNITE";
uint8_t dem = 0;
uint8_t tanso;
uint16_t rpms;
uint32_t thoigian;
uint32_t hientai = 0;
uint32_t thoigiancho = 10;
//------------------------------------------------------------------------//
void dem_xung(){
  dem++;
}
//------------------------------------------------------------------------//

void setup() {
  Serial.begin(9600);
  Wire.begin(0x01);
  Wire.onReceive(receiveEvent);
  attachInterrupt(0, dem_xung, RISING);
  pinMode(IGT1,OUTPUT);
  pinMode(IGT2,OUTPUT);
  pinMode(IGT3,OUTPUT);
  pinMode(IGT4,OUTPUT);

}
//------------------------------------------------------------------------//

void receiveEvent(){ // receive data from master
  data = "";
  while(Wire.available()){
    data += (char)Wire.read();
  }
}
//------------------------------------------------------------------------//
void loop() {
  thoigian = millis();
  if(thoigian - hientai >= thoigiancho){
    hientai = thoigiancho;
    rpms = (unsigned long int)dem*10/20;// đơn vị 0.1 vòng/10ms
    if(rpms == 15){
      dem = 0;
      if(data =="IGNITE"){
        //----bugi 1-------
        digitalWrite(IGT1,HIGH);
        digitalWrite(IGT1,LOW);
        //----bugi 2-------
        digitalWrite(IGT3,HIGH);
        digitalWrite(IGT3,LOW);
        //----bugi 3-------
        digitalWrite(IGT4,HIGH);
        digitalWrite(IGT4,LOW);
        //----bugi 4-------
        digitalWrite(IGT2,HIGH);
        digitalWrite(IGT2,LOW);
      }
    }
    // lock engine 
    else if(data == "STOP TO IGNITE"){
      for(uint8_t i=3; i>0; i--){
       Serial.print("Car will stop in: ");Serial.print(i);Serial.println(" s");
       delay(1000);
      }
      digitalWrite(IGT1,LOW);
      digitalWrite(IGT3,LOW);
      digitalWrite(IGT4,LOW);
      digitalWrite(IGT2,LOW);
    }
  }  
}
