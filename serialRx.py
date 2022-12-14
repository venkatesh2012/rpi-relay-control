# Venkatesh Srinivasan - Serial Receiver
# Copyright (C) 2022 Venkatesh Srinivasan
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

from time import sleep
import logging
# from systemd.journal import JournalHandler
import serial
import RPi.GPIO as GPIO
log = logging.getLogger('uartRx')
#log.addHandler(JournalHandler())
log.setLevel(logging.INFO)
ser = serial.Serial("/dev/ttyS0", baudrate = 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
rChannel0=7
rChannel1=3
rChannel2=22
rChannel3=25
GPIO.setup(rChannel0,GPIO.OUT)
GPIO.setup(rChannel1,GPIO.OUT)
GPIO.setup(rChannel2,GPIO.OUT)
GPIO.setup(rChannel3,GPIO.OUT)
rChannel=0
rChannelValue=GPIO.LOW
try:
  while 1:
    rx_data = ser.read()
    sleep(0.03)
    data_left = ser.inWaiting()
    rx_data += ser.read(data_left)
    rxString=rx_data.decode().strip()
    if rxString :
      relay=rxString.split("Relay: ")[1].split("-")
      if relay[1]=="0":
        rChannelValue=GPIO.LOW
      else:
        rChannelValue=GPIO.HIGH
      if relay[0]=="0":
        rChannel=rChannel0
      elif relay[0]=="1":
        rChannel=rChannel1
      elif relay[0]=="2":
        rChannel=rChannel2
      elif relay[0]=="3":
        rChannel=rChannel3;
      print(rChannel,rChannelValue)
      log.info(rChannel, rChannelValue)
      GPIO.output(rChannel,rChannelValue)
except KeyboardInterrupt:
    print("Stopping serialRx")
    log.info("Stopping SerialRx")
    ser.close()
    GPIO.cleanup()
