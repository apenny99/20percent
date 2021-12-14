Raspberry Pi python sensor project.

In order to use program:
- Put all the files contained in Final/sensorProject/ into a project folder on a raspberry 	pi running raspbian OS
- enable i2c interface on the raspberry pi (Figure 1)
- Correctly wire the Adafruit BME280 sensor to the raspberry p1 (Figure 2)
- Run the following command:
	
	chmod +x (file path of run.sh)

- open run.sh in order to run the program. Currently the only way to change the number of 	observations taken and the delay between observations is changing the values on 	lines 12 and 13 of main.py. I plan on changing this in the future.

In order to run the program from a command line:
	
	Option 1:   python3 /home/pi/Documents/sensorProject/main.py

	Option 2:   (run the file path of your run.sh file as a command)
 





Figure 1: https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/

Figure 2: https://i.stack.imgur.com/r5oq3.png