#include <iocontrol.h>
#include <ESP8266WiFi.h>

const char* myPanelName = "******name*******";
const char* key = "********key********";
int status;
const char* VarName_Control = "*******Control********";

const char* ssid = "*******WiFi******";
const char* password = "******WiFi*******";

int boot;
WiFiClient client;

// Создаём объект iocontrol, передавая в конструктор название панели, ключа  и клиента
iocontrol mypanel(myPanelName, key,client);


void setup() {
  Serial.begin(9600);
  delay(10);

  // prepare GPIO2
  pinMode(2, OUTPUT);
  pinMode(5, INPUT_PULLUP);
  pinMode(0, INPUT_PULLUP);
  digitalWrite(2, 0);
  
  WiFi.begin(ssid, password);
 //проверка соединения с сетью
  while (WiFi.status() != WL_CONNECTED) {
     digitalWrite(2, 1 );
     delay(500);
     Serial.print(".");
     digitalWrite(2, 0);
     delay(500);
    }
  Serial.println("WiFi connected");
  digitalWrite(2, 1);
  mypanel.begin();
}
void loop(){
  // ************************ ЧТЕНИЕ ************************
  // Чтение значений переменных из сервиса
   status = mypanel.readUpdate();
    // Если статус равен константе OK...
   if (status == OK) {
        // Выводим текст в последовательный порт
       Serial.println("------- Read OK -------");
        // Записываем считанный из сервиса значения в переменные
       long io_Control = mypanel.readInt(VarName_Control);   // целочисленная переменна
       Serial.println((String)"io_Control = "+io_Control);
       if (io_Control == 1)
       {
          digitalWrite(2, 1); //ставим pin 2 в единицу
       }
       if (io_Control == 2)
       {
          digitalWrite(2, 0); //сбрасываем pin 2 в ноль
       }
       
   //читаем пин 3  почему три а не 5 не понятно
   if (digitalRead(5) == 0 )
   {
        mypanel.write(VarName_Control, 1); 
        status = mypanel.writeUpdate();
        Serial.println("------- Write Start -------"); 
        delay(500);
    }
    //читаем pin 1 почему не pin 0 не понятно  
    if (digitalRead(0) == 0 )
    {
        mypanel.write(VarName_Control, 2); 
        status = mypanel.writeUpdate();
        Serial.println("------- Write Stop -------"); 
        delay(500);    
     }

   }
}
