class Status: 
    UP = 'up'
    DOWN = 'down'

    @staticmethod
    def get():
        with open('flag.txt', 'r') as file:
            data = file.readlines()
        
        if len(data) < 1:
            data.append('')
            
        return data[0]

    @staticmethod
    def set(status):
        if status not in [UP, DOWN]:
            raise Exeption("Only 'up' and 'down' are valid statuses")
        with open('flag.txt', 'w') as file:
            file.writelines(status)

class Flag:
    import RPi.GPIO as GPIO
    from RpiMotorLib import RpiMotorLib

    def __init__():
        GpioPins = [18, 23, 24, 25]

        # Declare an named instance of class pass a name and motor type
        self.motor = RpiMotorLib.BYJMotor("FlagMotor", "28BYJ")
        

    def __del__(self):
        # good practise to cleanup GPIO at some point before exit
        GPIO.cleanup()

    # Number of steps in a full revolution of the motor
    REVOLUTION = 512
    def move(clockwise = True, dist = 0.25):
        self.motor.motor_run(GpioPins , 0.0018, int(dist * REVOLUTION), not clockwise, False, "full", .005)

flag = Flag()
status = Status.get()

flag.move(status == Status.UP)
Status.set(Status.UP if status == Status.DOWN else Status.DOWN)
del flag