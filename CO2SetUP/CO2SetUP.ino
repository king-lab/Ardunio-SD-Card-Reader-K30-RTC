#include "kSeries.h" //include kSeries Library
#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include <TimeLib.h>
#include <DS1307RTC.h>

const int chipSelect = 4;
kSeries K_30(12,13); //Initialize a kSeries Sensor with pin 12 as Rx and 13 as Tx
String datalogfilename = ""; //Initialize the file name
tmElements_t tm;

String print2digits(int number) {
  String buffer = "";
  if (number >= 0 && number < 10) {
    buffer += "0";
    buffer += number;
  }else{
    buffer += number;
  }
  return buffer;
}
void setup()
{
 Serial.begin(9600); //start a serial port to communicate with the computer
 //Serial.println("   AN-216  Example 2:  uses the kSeries.h library");
 Serial.print("Initializing SD card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    while (1);
  }
  Serial.println("card initialized.");
    if (RTC.read(tm)) {
  //datalogfilename += tmYearToCalendar(tm.Year);
  String Year = "";
  Year += tmYearToCalendar(tm.Year);
  String shortYear = "";
  shortYear += Year[2];
  shortYear += Year[3];
  //datalogfilename += shortYear;
  //datalogfilename += print2digits(tm.Month);
  datalogfilename += print2digits(tm.Day);
  datalogfilename += print2digits(tm.Hour);
  datalogfilename += print2digits(tm.Minute);
  datalogfilename += ".txt";
  Serial.println(datalogfilename);
    } else {
    if (RTC.chipPresent()) {
      Serial.println("The DS1307 is stopped.  Please run the SetTime");
      Serial.println("example to initialize the time and begin running.");
      Serial.println();
    } else {
      Serial.println("DS1307 read error!  Please check the circuitry.");
      Serial.println();
    }
    delay(9000);
  }
}

void loop()
{
 double co2 = K_30.getCO2('p'); //returns co2 value in ppm ('p') or percent ('%')
 String data = "";
  if (RTC.read(tm)) 
  {
    data += tmYearToCalendar(tm.Year);
    data += '\t';
    data += tm.Month;
    data += '\t';
    data += tm.Day;
    data += '\t';
    data += tm.Hour;
    data += '\t';
    data += tm.Minute;
    } else {
    if (RTC.chipPresent()) 
      {
      Serial.println("The DS1307 is stopped.  Please run the SetTime");
      Serial.println("example to initialize the time and begin running.");
      Serial.println();
      } else 
      {
      Serial.println("DS1307 read error!  Please check the circuitry.");
      Serial.println();
      }
  }
 //Serial.print("Co2 ppm = ");
//Serial.println(co2); //print value
data += "\t";
data += co2;
 //dataString += "\n";
 File dataFile = SD.open(datalogfilename, FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    dataFile.println(data);
    dataFile.close();
    // print to the serial port too:
    Serial.println(data);
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
  }
 delay(1500); //wait 1.5 seconds
}