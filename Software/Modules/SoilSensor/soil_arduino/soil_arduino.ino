#include <SoftwareSerial.h>
/* ModbusMaster For communication with RS485+MODBUS sensors */
#include <ModbusMaster.h>

#define RE 7
#define DE 6

SoftwareSerial Serial1(8, 9);

/* Setup the Modbus transmission basics */

void PreTransmission() {
  // Set transmit mode
  digitalWrite(RE, HIGH);
  digitalWrite(DE, HIGH);
}

void PostTransmission() {
  // Set receive mode
  digitalWrite(RE, LOW);
  digitalWrite(DE, LOW);
}

// instantiate ModbusMaster object
ModbusMaster node;

/* END - Setup the Modbus transmission basics */
void setup() {
  pinMode(RE, OUTPUT);
  pinMode(DE, OUTPUT);
  digitalWrite(RE, HIGH);  // Set transmit mode
  Serial.begin(115200);
  Serial1.begin(4800);
  node.begin(1, Serial1);
  node.preTransmission(PreTransmission);
  node.postTransmission(PostTransmission);
}

void print_rs485_modbus_npk(float temperature, float sm, int ec, float ph, int nitrogen, int phosphorus, int potassium, int salinity, int tds) {

  //temp 34.0, sm 80.2, ph 8.4, N:2, P:51, K: 44107, salinity98, tds: 1539.0
  Serial.print(temperature, 1);
  Serial.print(',');
  Serial.print(sm, 1);
  Serial.print(',');
  Serial.print(ph, 1);
  Serial.print(',');
  Serial.print(nitrogen);
  Serial.print(',');
  Serial.print(phosphorus);
  Serial.print(',');
  Serial.print(potassium);
  Serial.print(',');
  Serial.print(salinity);
  Serial.print(',');
  Serial.print(tds);

  Serial.print("\n");
}

void full_print_rs485_modbus_npkphcth(float temperature, float sm, int ec, float ph, int nitrogen, int phosphorus, int potassium, int salinity, int tds) {

  Serial.print("Temperature: ");
  Serial.print(temperature, 1);
  Serial.print(" Cº");
  Serial.print(", SM: ");
  Serial.print(sm, 1);
  Serial.print(" %");
  Serial.print(", EC: ");
  Serial.print(ec, 1);
  Serial.print(" uS/cm");
  Serial.print(", pH: ");
  Serial.print(ph, 1);
  Serial.println();

  Serial.print("N: ");
  Serial.print(nitrogen);
  Serial.print(" mg/kg");
  Serial.print(", P: ");
  Serial.print(phosphorus);
  Serial.print(" mg/kg");
  Serial.print(", K: ");
  Serial.print(potassium);
  Serial.print(" mg/kg");
  Serial.println();

  Serial.print("Salinity: ");
  Serial.print(salinity);
  Serial.print(" mg/L");
  Serial.print(", TDS: ");
  Serial.print(tds);
  Serial.print(" mg/L");
  Serial.println();

  Serial.print("\n");
}

void rs485_modbus_npkphcth() {

  uint8_t resultMain;
  float sm = -999.0;
  float temperature = -999.0;
  int ec = -999;
  float ph = -999;
  int nitrogen = -999;
  int phosphorus = -999;
  int potassium = -999;
  int salinity = -999;
  int tds = -999;

delay(5000);
  // 0x0000 = Moisture (%) (0-100%) (<4s)
  /*
  delay(5000);
  resultMain = node.readInputRegisters(0x0000, 1);
  if (resultMain == node.ku8MBSuccess) {
    sm = float(node.getResponseBuffer(0x00)) / 10;
  }
  // 0x0001 = Temperature (C) (-40-80Cº) (<15s)
  delay(5000);
  resultMain = node.readInputRegisters(0x0001, 1); //TEMP -> 1 4 0 1 0 1 96 10
  if (resultMain == node.ku8MBSuccess) {
    temperature = float(node.getResponseBuffer(0x00)) / 10;
  }
  // 0x0002 = ec (uS/cm) (0-20000 uS/cm) (<1s)
  delay(5);
  resultMain = node.readInputRegisters(0x0002, 1); //EC -> 1 4 0 2 0 1 144 10
  if (resultMain == node.ku8MBSuccess) {
    ec = float(node.getResponseBuffer(0x00)) / 10;
  }
  // 0x0003 = ph (3-9PH) (<1s)
  delay(5);
  resultMain = node.readInputRegisters(0x0003, 1);  // PH -> 1 4 0 3 0 1 193 202
  if (resultMain == node.ku8MBSuccess) {
    ph = float(node.getResponseBuffer(0x00)) / 10;
  }

  // 0x0004 = nitrogen (mg/kg) (1-2999 mg/kg) (<1s)
  delay(5);
  resultMain = node.readInputRegisters(0x0004, 1);
  if (resultMain == node.ku8MBSuccess) {
    nitrogen = node.getResponseBuffer(0x00); //NITRO -> 1 4 0 4 0 1 112 11
  }

  // 0x0005 = phosphorus (mg/kg) (1-2999 mg/kg) (<1s)
  delay(5);
  resultMain = node.readInputRegisters(0x0005, 1);
  if (resultMain == node.ku8MBSuccess) {
    phosphorus = node.getResponseBuffer(0x00); // PHOSPHO -> 1 4 0 5 0 1 33 203
  }
*/
  // 0x0006 = potassium (mg/kg) (1-2999 mg/kg) (<1s)
  delay(5);
  resultMain = node.readInputRegisters(0x0006, 1); //POTASUYM -> 1 4 0 6 0 1 209 203
  if (resultMain == node.ku8MBSuccess) {
    potassium = node.getResponseBuffer(0x00);
  }
/*

  // 0x0007 = salinity (ppm)
  delay(500);
  resultMain = node.readInputRegisters(0x0007, 1);
  if (resultMain == node.ku8MBSuccess) {
    salinity = node.getResponseBuffer(0x00);
  }

  // 0x0008 = tds (ppm)
  delay(500);
  resultMain = node.readInputRegisters(0x0008, 1);
  if (resultMain == node.ku8MBSuccess) {
    tds = node.getResponseBuffer(0x00);
  }
  */
  full_print_rs485_modbus_npkphcth(temperature, sm, ec, ph, nitrogen, phosphorus, potassium, salinity, tds);
}

void loop() {
  Serial1.flush();
  rs485_modbus_npkphcth();
}