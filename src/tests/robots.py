class Robot:
    def introduce_self(self):
        print("My name is " + self.name + "and I am a " + self.machine)

r1 = Robot()
r1.name = "Tom"
r1.machine = "robot"

r2 = Robot()
r2.name = "Jerry"
r2.machine = "robot"

r1.introduce_self()
r2.introduce_self()