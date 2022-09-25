# rpi-relay-control
## Serial communication
USB to Serial communication is used in Python to send required commands to Raspberry PI.

Hardware Required
1. RaspberryPi
2. Relay control Board
3. USB to Serial Interface for COM communication

## Relay Control Board 
Below ports needs to be configured as Output (depends on the Board connected to Relay)
Port 3  - Relay 1
Port 7  - Relay 2
Port 22 - Relay 3
Port 25 - Relay 4

## Using Python scripts for sending control commands
serialTx.py is an example of sending the Tx commands over UART.  Command processing is handled in serialRx.py accordingly.

Pre-requisties:
1. Python installed
2. Python Serial package installed
3. Script to be run in Administrative console

For windows, identified COM port to be used and in linux identified tty port to be used
