#include <WiFi.h>
#include <PubSubClient.h>
#include "time.h"

// WiFi credentials
const char* ssid = "WZERO";
const char* password = "mnn12345";
// MQTT broker configuration
const char* mqttServer = "192.168.1.10";
const int mqttPort = 1883;
const char* mqttUser = "YOUR_MQTT_USERNAME";
const char* mqttPassword = "YOUR_MQTT_PASSWORD";
// NTP configuration
const char* ntpServer1 = "pool.ntp.org";
// const long gmtOffset_sec = 19800;  // GMT offset in seconds (IST in this case)
const int daylightOffset_sec = 0;  // No daylight saving time
// Create an instance of the MQTT client
WiFiClient espClient;
PubSubClient client(espClient);
void printAndPublishData() {
  struct tm timeinfo;
  if (!getLocalTime(&timeinfo)) {
    Serial.println("No time available (yet)");
    return;
  }
// Get the Unix timestamp
  time_t unixTime = time(NULL);
  // Generate random temperature and humidity values
  float temperature = random(20, 30); // Replace with your desired temperature range
  float humidity = random(40, 60);    // Replace with your desired humidity range
  char timeStr[40];
  strftime(timeStr, sizeof(timeStr), "%A, %B %d %Y %H:%M:%S", &timeinfo);
  char tempStr[6];
  dtostrf(temperature, 4, 1, tempStr);
  char humStr[6];
  dtostrf(humidity, 4, 1, humStr);
  // Publish time, temperature, and humidity to MQTT topics
  // client.publish("sensor/time1", timeStr);
  client.publish("sensor/timestamp1", String(unixTime).c_str());
  client.publish("sensor/temperature1", tempStr);
  client.publish("sensor/humidity1", humStr);
  Serial.print("Published Timestamp 1: ");
  Serial.println(unixTime);
  Serial.print("Published Temperature 1: ");
  Serial.print(temperature);
  Serial.println("°C");
  Serial.print("Published Humidity 1: ");
  Serial.print(humidity);
  Serial.println("%");
}
void setup() {
  // Initialize serial communication for debugging
  Serial.begin(115200);
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  // Connect to MQTT broker
  client.setServer(mqttServer, mqttPort);
  while (!client.connected()) {
    if (client.connect("ESP32Client1", mqttUser, mqttPassword)) {
      Serial.println("Connected to MQTT broker");
    } else {
      Serial.println("Failed to connect to MQTT broker, retrying...");
      delay(5000);
    }
  }
 // Configure NTP
  // configTime(gmtOffset_sec, daylightOffset_sec, ntpServer1);
  configTime(0, 0, ntpServer1);
  Serial.println("Setup completed.");
}
//   // Configure NTP
//   configTime(gmtOffset_sec, daylightOffset_sec, ntpServer1);
//   Serial.println("Setup completed.");
// }
void loop() {
  printAndPublishData(); // Print and publish time, temperature, and humidity
  delay(1000); // Wait for 5 seconds before printing and publishing again
  Serial.println("Loop executed.");
}