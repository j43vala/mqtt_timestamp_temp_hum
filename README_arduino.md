# ``ESP32 MQTT Sensor Data Publisher``

This Arduino code is designed for an ESP32 microcontroller to publish sensor data (temperature and humidity) along with a timestamp to an MQTT broker over a Wi-Fi connection. Below is an overview of how the code works:

## ``Required Libraries``

To use the ESP32 MQTT Sensor Data Publisher code, you will need to include the following libraries in your Arduino IDE:

1. **``WiFi Library``**: This library allows the ESP32 to connect to a Wi-Fi network.
   - Library Name: `WiFi`
   - Installation: You can install this library via the Arduino Library Manager.

2. **``PubSubClient Library``**: PubSubClient is an MQTT client library that enables communication with MQTT brokers.
   - Library Name: `PubSubClient`
   - Installation: You can install this library via the Arduino Library Manager.

3. **``Time Library``**: The Time library is used for time-related functions and is used for obtaining accurate timestamps.
   - Library Name: `time.h`
   - Installation: This library is typically included in the Arduino IDE by default and does not require additional installation.

# note
*Ensure that you have these libraries installed in your Arduino IDE before working with the ESP32 MQTT Sensor Data Publisher code.*


## ``Main Functionality``

The main functionality of this code includes:

1. **``Wi-Fi Connection``**: The ESP32 connects to a Wi-Fi network using the provided SSID and password.

    > ``SSID`` - your connected network naame

    > ``PASSWORD`` - password of connected network

2. **``MQTT Broker Connection``**: It establishes a connection to an MQTT broker using the specified MQTT server address, port, MQTT username, and password.

    > ``mqttServer`` - IP address or domain name of your MQTT broker

    > ``mqttPort`` = 1883

    > ``mqttUser`` = "YOUR_MQTT_USERNAME" ``(up to the individual)``

    > ``mqttPassword`` = "YOUR_MQTT_PASSWORD" ``(up to the individual)``

3. **``NTP Time Synchronization``**: The code synchronizes the ESP32's internal clock with a Network Time Protocol (NTP) server to obtain accurate timestamps.

    >``ntpServer1`` = "pool.ntp.org"      /get more info- https://www.ntppool.org/en/

4. **``Data Publication``**: The code publishes the following data to MQTT topics:
   - ``Timestamp (Unix timestamp)``
        > ``topic name`` - sensor/timestamp1 
   - ``Temperature (in °C)``
        > ``topic name`` - sensor/temperature1
   - ``Humidity (in %)``
        > ``topic name`` - sensor/humidity1

# note
   *make sure publisher and subscriber both have same topic name **(You can customize the MQTT topics according to your specific needs.)***


## ``How It Works``

1. The ESP32 starts by initializing serial communication for debugging purposes.

2. It attempts to connect to the specified Wi-Fi network. During this process, it prints status messages until a successful connection is established.

3. Once connected to Wi-Fi, it establishes a connection to the MQTT broker using the provided credentials. If the connection attempt fails, it retries after a delay.

4. NTP time synchronization is configured using a designated NTP server.

5. The `printAndPublishData` function is called, which does the following:
   - Retrieves the current local time and Unix timestamp.
   - Generates random temperature and humidity values (you can replace these with actual sensor data for that need to import library and function for sensor).
   - Formats the data and publishes it to MQTT topics.
   - Prints the published data to the serial monitor for debugging.

6. The main loop continues to execute the `printAndPublishData` function at regular intervals (defined by the delay) to continuously publish sensor data.

7. The ESP32 will keep publishing data until you manually stop the program.

# note
This code provides a basic framework for publishing sensor data over MQTT using an ESP32. To adapt it for your specific application, you should replace the simulated data with actual sensor readings as per mentioned above and customize MQTT topics and credentials as needed.