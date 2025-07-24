<img alt="PiStation logo" src="static/PiStation.png">

# What is PiStation?
PiStation is a local weather station hosted on a Raspberry Pi. It retrieves weather data over HTTP via an ESP32, which is then stored in a sqlite database.
- WebUI: Built with Flask and Tailwind
- Data Visualisation: Charts.JS for weather change visualisation
- Server Handling: Nginx and Systemd. 
# What is used?
## Sensors:
- DHT22: Used for temperature and humidity
- BMP280: Used for Air Pressure
- Water Level Sensor: Primative rain detection
## Devices:
- Raspberry Pi
- ESP32 Wroom DevKit
## Technologies
- Nginx: Serving website
- Systemd: Autostarting/handling important services
- Flask: Backend Routing/Logic of website
- Tailwind: Frontend styling
- Chart.js: Dynamic Data visualisation
- Sqlite: Lightweight database

# Could I build/host this myself?
Absolutely! However the services will need to be manually setup.

# ESP32 Code:
https://github.com/darrkenn/PiStation-Esp32

[![HackaTime Badge](https://hackatime-badge.hackclub.com/U092R8UPA6L/PiStation)](https://hackatime.hackclub.com)
