/*
 * Copyright (c) 2018, circuits4you.com
 * All rights reserved.
 * Create a TCP Server on ESP8266 NodeMCU. 
 * TCP Socket Server Send Receive Demo
*/

#include <ESP8266WiFi.h>
#include <Keypad_I2C.h> // Keypad_I2C kütüphanesini bağlıyoruz.
#include <Keypad.h> // Keypad kütüphanesini bağlıyoruz.
#include <Wire.h> // Wire kütüphanesini bağlıyoruz.

#define SendKey 0  //Button to send data Flash BTN on NodeMCU
#define I2CADDR 0x20

const byte ROWS = 4; // Tuş takımındaki satır sayısı
const byte COLS = 3; // Tuş takımındaki sütun sayısı
int led_pin1 = 13;
int led_pin2 = 14;
int buzzer_pin = 12;


// Tuş takımı üzerindeki butonları matris şeklinde yazıyoruz.
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {0,1,2,3}; // Satıların konnektördeki pin numaraları
byte colPins[COLS] = {4,5,6}; // Sütunların konnektördeki pin numaraları

// Yeni bir tuş takımı sınıfı oluşturuyoruz.
Keypad_I2C customKeypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS, I2CADDR, PCF8574 ); 


int port = 8888;  //Port number
WiFiServer server(port);

//Server connect to WiFi Network
const char *ssid = "embed_x";  //Enter your wifi SSID
const char *password = "gomulu2022";  //Enter your wifi Password
int toggle=0;
int count=0;
char status_pass = 'x';
//=======================================================================
//                    Power on setup
//=======================================================================
void setup() 
{
  Wire.begin( );
  customKeypad.begin( );
  Serial.begin(115200);
  pinMode(SendKey,INPUT_PULLUP);  //Btn to send data
  Serial.println();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password); //Connect to wifi
  pinMode(led_pin1, OUTPUT);
  pinMode(led_pin2, OUTPUT);
  pinMode(buzzer_pin, OUTPUT);
 
  // Wait for connection  
  Serial.println("Connecting to Wifi");
  while (WiFi.status() != WL_CONNECTED) {   
    delay(500);
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);

  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  
  server.begin();
  Serial.print("Open Telnet and connect to IP:");
  Serial.print(WiFi.localIP());
  Serial.print(" on port ");
  Serial.println(port);
}
//=======================================================================
//                    Loop
//=======================================================================
void update_out(){
  if(status_pass=='0'){
    toggle= !toggle;
    digitalWrite(led_pin2,toggle);
    delay(500);
  }
  else if(status_pass=='1'){
    toggle= !toggle;
    digitalWrite(led_pin1,toggle);
    delay(500);
  }
  else if(status_pass=='2'){
    digitalWrite(led_pin1,HIGH);

  }
  else if(status_pass=='3'){
    digitalWrite(led_pin1,LOW);

  }
  else if(status_pass=='4'){
    digitalWrite(led_pin2,HIGH);

  }
  else if(status_pass=='5'){
    digitalWrite(led_pin2,LOW);

  }
  else if(status_pass=='6'){
    digitalWrite(buzzer_pin,HIGH);

  }
  else if(status_pass=='7'){
    digitalWrite(buzzer_pin,LOW);

  }
}


void loop() 
{
  WiFiClient client = server.available();
  
  if (client) {

      
      while(client.connected())
      {
        update_out();
        if(client.available()>0){
        // read data from the connected client
        status_pass = client.read(); 
       }
          char customKey = customKeypad.getKey();
          client.write(customKey);
        
      }
    }
    status_pass ='x';
    digitalWrite(led_pin1,LOW);
    digitalWrite(led_pin2,LOW);
    digitalWrite(buzzer_pin,LOW);
    client.stop();
    Serial.println("Client disconnected");    
  }

//=======================================================================
