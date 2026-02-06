const int BUTTON_PIN = 16; // The ESP8266 pin D7 connected to button

int prev_button_state = HIGH; // the previous state from the input pin
int button_state;    // the current reading from the input pin
int tiempo;

void setup() {
  // Initialize the Serial to communicate with the Serial Monitor.
  Serial.begin(115200);
  // initialize the pushbutton pin as an pull-up input
  // the pull-up input pin will be HIGH when the switch is open and LOW when the switch is closed.
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
    
    if(!digitalRead(BUTTON_PIN))
    {
      tiempo++;
    }
    else{
      if(tiempo > 0 && tiempo <= 250)
        Serial.print("P");
      else if(tiempo > 250)
        Serial.print("L");
      tiempo = 0;
    }
    delay(1);
}
