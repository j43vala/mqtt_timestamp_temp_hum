# MQTT timestamp convert & Data Receiver

This Python script connects to an MQTT broker, subscribes to specific topics, and processes incoming sensor data. It also converts timestamps from UTC to Indian Standard Time (IST).

## ``Prerequisites``

Before running the script, ensure you have the following:

- **Required Python Libraries**:
  - **Paho MQTT Client**: This library provides MQTT support for Python. You can install it using `pip`:

        pip install paho-mqtt
    

  - **Pytz**: Pytz is used for timezone conversion. Install it with `pip`:

        pip install pytz
    

- **Access to an MQTT Broker**: You should have access to an MQTT broker (e.g., Mosquitto) with the necessary credentials (broker IP, port, username, and password).

## ``Configuration``

1. Open the script `mqtt_sensor_receiver.py` in your preferred code editor.

2. Modify the following variables in the script to match your MQTT broker setup:

        - `mqtt_broker`: Replace with the IP address or hostname of your MQTT broker.
        - `mqtt_port`: Replace with the MQTT broker port (default is 1883).
        - `mqtt_user`: Replace with your MQTT broker username.
        - `mqtt_password`: Replace with your MQTT broker password.

## ``Usage``

1. Ensure you have configured the script with the correct MQTT broker information.

2. Run the script using the following command:


# python mqtt_sensor_receiver.py


The script will connect to the MQTT broker and start listening for messages.

3. The script subscribes to the following topics by default:
    - `sensor/temperature1`: Receives temperature data in Celsius.
    - `sensor/humidity1`: Receives humidity data in percentage.
    - `sensor/timestamp1`: Receives timestamp data in UTC.

4. When messages are received on these topics, the script will display the data along with the timestamp converted to Indian Standard Time (IST).

## ``Customization``

You can customize the script to subscribe to different MQTT topics or modify the message handling logic by editing the `on_message` function in the script.

# Essential information about Datetime format

<font size="5.5">``%Y-%m-%d %H:%M:%S``</font>

| ``Format`` | ``Description``                                                |
|--------|------------------------------------------------------------|
| ``%a``     | Abbreviated weekday name                                   |
| ``%A``     | Full weekday name                                          |
| ``%b``     | Abbreviated month name                                     |
| ``%B``     | Full month name                                            |
| ``%c``     | Date and time representation for your locale              |
| ``%d  ``   | Day of the month as a decimal number (01-31)              |
| ``%H ``    | Hour in 24-hour format (00-23)                            |
| ``%I``     | Hour in 12-hour format (01-12)                            |
| ``%j``   | Day of the year as a decimal number (001-366)             |
| ``%m`` | Month as a decimal number (01-12)                         |
|`` %M ``    | Minute as a decimal number (00-59)                        |
|`` %p``     | Current locale’s A.M./P.M. indicator for 12-hour clock     |
|`` %S``     | Second as a decimal number (00-59)                        |
|`` %U``     | Week of the year as a decimal number, Sunday as first day of the week (00-51) |
| ``%w``     | Weekday as a decimal number (0-6; Sunday is 0)            |
|`` %W``     | Week of the year as a decimal number, Monday as first day of the week (00-51) |
|`` %x``     | Date representation for the current locale                 |
|`` %X``     | Time representation for the current locale                 |
|`` %y``     | Year without century, as a decimal number (00-99)         |
|`` %Y``     | Year with century, as a decimal number                     |
|`` %z``     | Time-zone name or abbreviation (no characters if time zone is unknown) |
|`` %Z``    | Time-zone name or abbreviation (no characters if time zone is unknown) |
|`` %%``     | Percent sign                                               |

For more information - [Datetime format](https://forum.arduino.cc/t/esp32-time-library-formatting-date-and-writing-it-to-char-array/520346/7)

# Information Regarding Timezone
## ``UTC (Coordinated Universal Time)``

- **``UTC (Coordinated Universal Time)``** is the primary time standard worldwide.
- Serves as a reference time for global timekeeping.

## ``Time Zones in Different Countries``

Time zones are regions with the same standard time. They are defined by their offset from UTC.

**``Exemplification``**
 >   - **``EST (Eastern Standard Time)``**: UTC-5 (USA - Eastern Time Zone)
 >   - **``CST (Central Standard Time)``**: UTC-6 (USA - Central Time Zone)
 >   - **``PST (Pacific Standard Time)``**: UTC-7 (USA - Pacific Time Zone)
 >   - **``GMT (Greenwich Mean Time)``**: UTC+0 (UK and Ireland)
 >   - **``CET (Central European Time)``**: UTC+1 (Central Europe)
 >   - **``IST (Indian Standard Time)``**: UTC+5:30 (India)
 >   - **``JST (Japan Standard Time)``**: UTC+9 (Japan)

Some regions and countries may observe Daylight Saving Time, adjusting their clocks forward or backward by one hour during certain periods of the year.

- In the month of ``winter/spring`` forverded by 1 hour

- In the month of ``fall`` backwarded by 1 hour 
