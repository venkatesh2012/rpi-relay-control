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

import time
import serial
ser = serial.Serial("COM4", baudrate = 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
relay=0
relaystatus=[0,0,0,0]
while True:
  if relaystatus[relay] == 0:
    relaystatus[relay] = 1
  else:
    relaystatus[relay] = 0

  ser.write(b'Relay: %d-%d\n'%(relay,relaystatus[relay]))
  print("Sent: Relay: ",relay,relaystatus[relay])
  time.sleep(1)
  if relay >= 3 :
    relay = 0;
  else:
    relay += 1
    
    
