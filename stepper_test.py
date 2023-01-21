import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

class Status: 
    UP = 'up'
    DOWN = 'down'
    def get(self):
        with open('flag.txt', 'r') as file:
            data = file.readlines()
        
        if len(data) < 1:
            data.append('')
            
        return data[0]

    def set(self, status):
        if status not in [Status.UP, Status.DOWN]:
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
        print("GPIO.cleanup() called.")

    def move(self, clockwise = True, dist = 0.25):
        self.motor.motor_run(self.GPIOPINS , 0.0018, int(dist * self.REVOLUTION), clockwise, False, "full", .005)

class FlagController:
    def __init__(self):
        self.flag = Flag()
        self.status = Status()

    def setFlagUp(self):
        if self.status.get() == Status.DOWN:
            self.flag.move(False)
            self.status.set(Status.UP)

    def setFlagDown(self):
        if self.status.get() == Status.UP:
            self.flag.move(True)
            self.status.set(Status.DOWN)

controller = FlagController()

controller.setFlagUp()
controller.setFlagDown()