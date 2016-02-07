#!/usr/bin/python
#
# Based on
# https://github.com/joshhyman/beer-fridge-monitor/blob/master/controller/temperature_controller.py
# for reading a DS18B20 temperature sensor

import os

_LIVE_SENSOR_FILE = "/sys/bus/w1/devices/28-000007600a7d/w1_slave"
_TEST_SENSOR_FILE = "controllers/test_data/w1_slave"

class TempSensorReader(object):
  def __init__(self, use_test_data):
    self.use_test_data = use_test_data

  def _ConvertCelsiusToFahrenheit(self, temp_celsius):
    """Converts the provided temperature in celsius to fahrenheit."""
    return (temp_celsius * 1.8) + 32

  def Read(self):
    """Reads the measured temperature from the DS18B20 sensor."""
    if self.use_test_data:
      sensor_file = os.path.join(os.getcwd(), _TEST_SENSOR_FILE)
    else:
      sensor_file = _LIVE_SENSOR_FILE

    with open(sensor_file) as sensor_file:
      sensor_file_contents = sensor_file.read()
    sensor_data = sensor_file_contents.split("\n")[1].split(" ")[9]

    # temp is stored as celsius * 1000
    curr_temp = float(sensor_data[2:]) / 1000

    return self._ConvertCelsiusToFahrenheit(curr_temp)

if __name__ == '__main__':
  temp_sensor_reader = TempSensorReader(True)
  print temp_sensor_reader.Read()
