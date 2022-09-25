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
    
    
