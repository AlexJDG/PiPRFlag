import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

class Status: 
    @staticmethod
    def get():
        with open('flag.txt', 'r') as file:
            data = file.readlines()
        
        if len(data) < 1:
            data.append('')
            
        return data[0]

    @staticmethod
    def set(self, status):
        UP = 'up'
        DOWN = 'down'
        if status not in [UP, DOWN]:
            raise Exeption("Only 'up' and 'down' are valid statuses")
        with open('flag.txt', 'w') as file:
            file.writelines(status)

class Flag:
    # Number of steps in a full revolution of the motor
    REVOLUTION = 512
    GPIOPINS = [18, 23, 24, 25]

    def __init__(self):

        # Declare an named instance of class pass a name and motor type
        self.motor = RpiMotorLib.BYJMotor("FlagMotor", "28BYJ")
        

    def __del__(self):
        # good practise to cleanup GPIO at some point before exit
        GPIO.cleanup()

    def move(self, clockwise = True, dist = 0.25):
        self.motor.motor_run(self.GPIOPINS , 0.0018, int(dist * self.REVOLUTION), not clockwise, False, "full", .005)

flag = Flag()
status = Status.get()

flag.move(status == Status.UP)
Status.set(Status.UP if status == Status.DOWN else Status.DOWN)
del flag