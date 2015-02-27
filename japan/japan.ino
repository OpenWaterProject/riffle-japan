
char msg = ' ';


void setup(void)
{
  Serial.begin(9600);
 
}


void loop(void)
{
  
  // listen on serial port
 msg = ' ';
 
  while (Serial.available()>0){ 
		msg=Serial.read();
	}

  if (msg=='y') {
  
    double temp=50.3;
    
    Serial.print(F("temp: "));
    Serial.println(temp);
  }
  
  delay(1000);
  
 
}
