# Setup

## I2C

- To enable I2C, run the command   sudo raspi-config    then select Interfacing Options>I2C and select yes when prompted. select finish and then yes when     prompted to reboot.

## Folder formatting
  
- Create a folder called "sensorProject" in the home/pi/Documents folder on the Rasperry Pi and move all the files from this github into the folder. 

## MatPlotLib

- in order to install MatPlotLib, run the following commands in terminal. 

    sudo apt update
    sudo apt install python3-matplotlib
    
    

## Wiring

- Connect the terminals of the sensor to the appropriate GPIO pins on the Raspberry Pi. (see image below)

<img width="310" alt="Screen Shot 2022-05-25 at 5 18 48 PM" src="https://user-images.githubusercontent.com/23064318/170384798-d7cf2a9e-475d-414a-a4a1-48725a483299.png">


## Running code

- in order to run the program, open the 'Main.py' with any python interpreter and run it inside the interpeter
- Alternativley, run the following command in the command line:

    python3 /home/pi/Documents/sensorProject/main.py
    
## Successful Run

- A successful run should generate a graph like this:

<img width="544" alt="Screen Shot 2022-05-11 at 7 54 53 PM" src="https://user-images.githubusercontent.com/23064318/170384678-3b3e6bb6-c74b-4041-b3cf-706fb15a5675.png">



    
