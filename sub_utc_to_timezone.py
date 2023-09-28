# # receive timestamp, temprature and humidity converted into utc time **********************************

# import paho.mqtt.client as mqtt
# import datetime

# # MQTT broker configuration
# mqtt_broker = "192.168.1.10"
# mqtt_port = 1883
# mqtt_user = "YOUR_MQTT_USERNAME"
# mqtt_password = "YOUR_MQTT_PASSWORD"

# # Callback when the client connects to the MQTT broker
# def on_connect(client, userdata, flags, rc):
#     print("Connected to MQTT broker with result code " + str(rc))
#     # Subscribe to the desired topics
#     client.subscribe("sensor/temperature1")
#     client.subscribe("sensor/humidity1")
#     client.subscribe("sensor/timestamp1")

# #Function to convert timestamp to UTC time
# def timestamp_to_utc(timestamp):
#     try:
#         timestamp = float(timestamp)
#         utc_time = datetime.datetime.utcfromtimestamp(timestamp)
#         return utc_time.strftime('%Y-%m-%d %H:%M:%S UTC')
#     except ValueError as e:
#         return f"Invalid timestamp format: {e}"

# # Callback when a message is received from the MQTT broker
# def on_message(client, userdata, msg):
#     if msg.topic == "sensor/timestamp1":
#         timestamp = msg.payload.decode()
#         utc_time = timestamp_to_utc(timestamp)
#         print(f"Received timestamp on topic {msg.topic}: {timestamp}")
#         print(f"Converted to UTC: {utc_time}")
#     else:
#         print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

# # Create an MQTT client
# client = mqtt.Client()

# # Set the username and password for the MQTT client (if required)
# client.username_pw_set(mqtt_user, mqtt_password)

# # Set the callback functions
# client.on_connect = on_connect
# client.on_message = on_message

# # Connect to the MQTT broker
# client.connect(mqtt_broker, mqtt_port, 60)

# # Start the MQTT client loop
# client.loop_forever()



# converted into utc to indian timezone ***************************************************************



import paho.mqtt.client as mqtt
import datetime
import pytz  # Import the pytz library

# MQTT broker configuration
mqtt_broker = "192.168.1.10"
mqtt_port = 1883
mqtt_user = "YOUR_MQTT_USERNAME"
mqtt_password = "YOUR_MQTT_PASSWORD"

# Define the IST timezone
ist_timezone = pytz.timezone('Asia/Kolkata')

# Callback when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    # Subscribe to the desired topics
    client.subscribe("sensor/temperature1")
    client.subscribe("sensor/humidity1")
    client.subscribe("sensor/timestamp1")

# Function to convert timestamp to UTC time
def timestamp_to_utc(timestamp):
    try:
        timestamp = float(timestamp)
        utc_time = datetime.datetime.utcfromtimestamp(timestamp)
        return utc_time.strftime('%Y-%m-%d %H:%M:%S UTC')
    except ValueError as e:
        return f"Invalid timestamp format: {e}"

# Callback when a message is received from the MQTT broker
def on_message(client, userdata, msg):
    if msg.topic == "sensor/timestamp1":
        timestamp = msg.payload.decode()
        utc_time = timestamp_to_utc(timestamp)
        
        # Convert UTC time to IST
        utc_time = datetime.datetime.strptime(utc_time, '%Y-%m-%d %H:%M:%S UTC')
        utc_time = pytz.utc.localize(utc_time)
        ist_time = utc_time.astimezone(ist_timezone)
        ist_time_str = ist_time.strftime('%Y-%m-%d %H:%M:%S IST')
        
        print(f"Received timestamp on topic {msg.topic}: {timestamp}")
        print(f"Universal Time : {utc_time}")
        print(f"Indian Standard Time: {ist_time_str}")
    elif msg.topic == "sensor/temperature1":
        temperature = msg.payload.decode()
        print(f"Received temperature on topic {msg.topic}: {temperature} °C")
    elif msg.topic == "sensor/humidity1":
        humidity = msg.payload.decode()
        print(f"Received humidity on topic {msg.topic}: {humidity}%")
    else:
        print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")


# Create an MQTT client
client = mqtt.Client()

# Set the username and password for the MQTT client (if required)
client.username_pw_set(mqtt_user, mqtt_password)

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT client loop
client.loop_forever()



