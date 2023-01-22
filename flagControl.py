import RPi.GPIO as GPIO
import Status
from RpiMotorLib import RpiMotorLib


class Flag:
    # Number of steps in a full revolution of the motor
    REVOLUTION = 512
    GPIOPINS = [18, 23, 24, 25]

    def __init__(self):
        # Instantiate a motor instance with the motor type
        self.motor = RpiMotorLib.BYJMotor("FlagMotor", "28BYJ")

    def __del__(self):
        # good practise to clean up GPIO at some point before exit
        GPIO.cleanup()
        print("GPIO.cleanup() called.")

    def move(self, clockwise=True, dist=0.25):
        self.motor.motor_run(self.GPIOPINS, 0.0018, int(dist * self.REVOLUTION), clockwise, False, "full", .005)


class FlagController:
    def __init__(self):
        self.flag = Flag()

    def setFlagUp(self):
        if Status.getStatus() == Status.DOWN:
            self.flag.move(False)
            Status.setStatus(Status.UP)

    def setFlagDown(self):
        if Status.getStatus() == Status.UP:
            self.flag.move(True)
            Status.setStatus(Status.DOWN)
