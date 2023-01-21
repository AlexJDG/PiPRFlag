import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib
    
GpioPins = [18, 23, 24, 25]

# Declare an named instance of class pass a name and motor type
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

flagUp = True

with open('flag.txt', 'r') as file:
    data = file.readlines()
    
if len(data) < 1:
    data.append('')
    
flagUp = data[0] == 'up'
data[0] = 'down' if flagUp else 'up'

with open('flag.txt', 'w') as file:
    file.writelines(data)
    
# call the function pass the parameters
mymotortest.motor_run(GpioPins , 0.0018, 128, not flagUp, False, "full", .005)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
