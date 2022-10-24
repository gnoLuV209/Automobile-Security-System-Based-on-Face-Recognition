#include <Wire.h>
#include<LiquidCrystal.h>


#define encoder 2
#define trans 9
#define led_warning 8

uint8_t dem = 0;
uint8_t tan_so;
uint16_t rps;
uint16_t rpm;
uint32_t thoigian;
uint32_t hientai = 0;
uint32_t thoigiancho = 1000;
String data_control;

LiquidCrystal lcd(12, 11, 7, 6, 5, 4);

void dem_xung(){
  dem++;
}

void setup() { 
  Wire.begin();
  Serial.begin(115200);
  Serial.setTimeout(1);
  lcd.begin(16,2);
  attachInterrupt(0, dem_xung, RISING);
  pinMode(encoder,INPUT_PULLUP);
  pinMode(trans, OUTPUT);
  pinMode(led_warning, OUTPUT);
}

void loop() {
  data_control = Serial.readString();
  if (data_control == "Owner"){
    analogWrite(trans,51);
  }
  else if (data_control == "Stranger"){
    digitalWrite(led_warning,HIGH);
    delay(5000);
    digitalWrite(led_warning,LOW);
  }
  else if (data_control == "Complete Engine Start"){
    digitalWrite(trans,0);
  }
  //lcd.noDisplay();
  thoigian = millis();
  //Serial.print("Time: "); Serial.print(thoigian); Serial.print(" ");
  //Serial.print("Hiện tại: "); Serial.println(hientai);
  if (thoigian - hientai >= thoigiancho){
    hientai = thoigiancho;
    tan_so = dem; // xung/giây
    lcd.setCursor(0,0);
    lcd.print("Tan so: "); lcd.print(tan_so); lcd.print(" Hz");
    
    rps = tan_so/20; // vòng/giây
    rpm = rps*60; // vòng/phút
    if ( rpm >=300 ){
      Serial.println("Complete Engine Start");
    }
    lcd.setCursor(0,1);
    lcd.print("RPM: "); lcd.print(rpm); lcd.print(" v/p");
    dem = 0;
  }
  
  if (data_control == "Detect Stranger driving car"){
      Wire.beginTransmission(0x01); 
      Wire.write("STOP TO IGNITE"); 
      Wire.endTransmission(); 
  }
  
}
