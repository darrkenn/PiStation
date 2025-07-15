<img alt="PiStation logo" src="static/PiStation.png">

# What is PiStation?
PiStation is a local weather station hosted on a Raspberry Pi. It retrieves weather data over HTTP via an ESP32, which is then stored in a sqlite database.
- WebUI: Built with Flask and Tailwind
- Data Visualisation: Charts.JS for weather change visualisation
- Server Handling: Nginx and SystemD. 
# What is used?
## Sensors:
- DHT22: Used for temperature and humidity
- BMP280: Used for Air Pressure
- Water Level Sensor: Does the job well enough for rain detection
## Devices:
- Raspberry Pi
- ESP32 Wroom DevKit
## Technologies
- Nginx: Serving website
- SystemD: Autostarting/handling important services
- Flask: Backend Routing/Logic of website
- Tailwind: Frontend styling
- Chart.js: Dynamic Data visualisation
- Sqlite: Lightweight database

# Could I build this myself?
Absolutely! Although some minor code changes and manual setup of services/nginx.

# ESP32 Code/Wiring:
https://github.com/darrkenn/PiStation-Esp32

[![HackaTime Badge](https://hackatime-badge.hackclub.com/U092R8UPA6L/PiStation)](https://hackatime.hackclub.com)
