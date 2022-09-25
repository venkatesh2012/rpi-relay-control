from time import sleep
import serial
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
    GPIO.output(rChannel, rChannelValue)
