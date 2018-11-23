#include <SPI.h>
/* Include the RFID library */
#include <RFID.h>

/* Define the DIO used for the SDA (SS) and RST (reset) pins. */
#define SDA_DIO 9
#define RESET_DIO 8
/* Create an instance of the RFID library */
RFID RC522(SDA_DIO, RESET_DIO); 
char c;
String leer;
void setup()
{ 
  Serial.begin(115200);
  /* Enable the SPI interface */
  SPI.begin(); 
  /* Initialise the RFID reader */
  RC522.init();

  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(27, OUTPUT);
  pinMode(28, OUTPUT);
  pinMode(29, OUTPUT);
  
  pinMode(30, OUTPUT);
  pinMode(31, OUTPUT);
  pinMode(32, OUTPUT);
  pinMode(33, OUTPUT);
  pinMode(34, OUTPUT);
  pinMode(35, OUTPUT);
  pinMode(36, OUTPUT);
  pinMode(37, OUTPUT);
}

void loop()
{
  digitalWrite(22,HIGH);   
  digitalWrite(23,HIGH);   
  digitalWrite(24,HIGH);   
  
  digitalWrite(25,HIGH);   
  digitalWrite(26,HIGH);   
  digitalWrite(27,HIGH);   
  
  digitalWrite(28,HIGH);   
  digitalWrite(29,HIGH);
  
  digitalWrite(30,HIGH);    
  digitalWrite(31,HIGH);   
  digitalWrite(32,HIGH);    
  
  digitalWrite(33,HIGH);    
  digitalWrite(34,HIGH);   
  digitalWrite(35,HIGH);   
  
  digitalWrite(36,HIGH);   
  digitalWrite(37,HIGH);
  
  leer = "";
  while(Serial.available()>0){
    
    c = Serial.read();
    delay(1000);
    if(c == 'c'){
        break;
      }else{
        leer += c;
      }
  }
  
  /* Has a card been detected? */
   
    if(c == 'c'){/*Si se va a leer el carnet*/
      if (RC522.isCard())
      {
        /* If so then get its serial number */
        RC522.readCardSerial();
        for(int i=0;i<5;i++)
        {
          Serial.print(RC522.serNum[i],DEC);
          //Serial.print(RC522.serNum[i],HEX); //to print card detail in Hexa Decimal format
        }
      }
    }else{/*Si se manda cualquier cosa*/
          
          switch (leer.toInt()){
    case 1:
      digitalWrite(22,LOW);
      digitalWrite(23,LOW);
      digitalWrite(24,LOW);
      delay (5000);
      break;
    case 2:
      digitalWrite(23,LOW);
      digitalWrite(24,LOW);
      delay (5000);
      break;
    case 3:
      digitalWrite(22,LOW);
      digitalWrite(24,LOW);
      delay (5000);
      break;
    case 4:
      digitalWrite(24,LOW);
      delay (5000);
      break;
    case 5:
      digitalWrite(22,LOW);
      digitalWrite(23,LOW);
      delay (5000);
      break;
    case 6:   
      digitalWrite(23,LOW);
      delay (5000);
      break;
    case 7:
      digitalWrite(22,LOW);
      delay (5000);
      break;
    case 8:
      digitalWrite(25,LOW);
      digitalWrite(26,LOW);
      digitalWrite(27,LOW);
      delay (5000);
      break;
    case 9:
      digitalWrite(26,LOW);
      digitalWrite(27,LOW);
      delay (5000);
      break;
    case 10:
      digitalWrite(25,LOW);
      digitalWrite(27,LOW);
      delay (5000);
      break;
    case 11:
      digitalWrite(27,LOW);
      delay (5000);
      break;
    case 12:
      digitalWrite(25,LOW);
      digitalWrite(26,LOW);
      delay (5000);
      break;
    case 13:
      digitalWrite(26,LOW);
      delay (5000);
      break;
    case 14:
      digitalWrite(25,LOW);
      delay (5000);
      break;   
    case 15:
      digitalWrite(30,LOW);
      digitalWrite(31,LOW);
      digitalWrite(32,LOW);
      delay (5000);
      break;
    case 16:
      digitalWrite(31,LOW);
      digitalWrite(32,LOW);
      delay (5000);
      break;
    case 17:
      digitalWrite(30,LOW);
      digitalWrite(32,LOW);
      delay (5000);
      break;
    case 18:
      digitalWrite(32,LOW);
      delay (5000);
      break;
    case 19:
      digitalWrite(30,LOW);
      digitalWrite(31,LOW);
      delay (5000);
      break;
    case 20:
      digitalWrite(31,LOW);
      delay (5000);
      break;
    case 21:
      digitalWrite(30,LOW);
      delay (5000);
      break;  
    case 22:
      digitalWrite(33,LOW);
      digitalWrite(34,LOW);
      digitalWrite(35,LOW);
      delay (5000);
      break;
    case 23:
      digitalWrite(34,LOW);
      digitalWrite(35,LOW);
      delay (5000);
      break;
    case 24:
      digitalWrite(33,LOW);
      digitalWrite(35,LOW);
      delay (5000);
      break;
    default:
      break;
    }
    delay(1000);
  }
}
