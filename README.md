# rpi-relay-control
## Serial communication
USB to Serial communication is used in Python to send required commands to Raspberry PI.

Hardware Required
* RaspberryPi
* Relay control Board
* USB to Serial Interface for COM communication

## Relay Control Board 
Below ports needs to be configured as Output (depends on the Board connected to Relay)

* Port 7  - Relay 1
* Port 3  - Relay 2
* Port 22 - Relay 3
* Port 25 - Relay 4

## Using Python scripts for sending control commands
serialTx.py is an example of sending the Tx commands over UART.  Command processing is handled in serialRx.py accordingly.

Pre-requisties:
* Python installed
* Python Serial package installed
* Script to be run in Administrative console

For windows, identified COM port to be used and in linux identified tty port to be used


## Using Linux Service for serialRx.py in RPI
uartRx.service is used to start the serialRx.py automatically as a Service.  
Copy this file to /usr/systemd/system/ and modify the execution path of python script file.  By Default the service looks for the file in /opt/rpi-relay-control/serialRx.py

This service should be now activated:

```Shell
sudo chmod 644 /lib/systemd/system/uartRx.service
chmod +x /opt/rpi-relay-control/serialRx.py
sudo systemctl daemon-reload
sudo systemctl enable uartRx.service
sudo systemctl start uartRx.service
```
Now the python script is enabled to start receiving the commands during system start automatically.

