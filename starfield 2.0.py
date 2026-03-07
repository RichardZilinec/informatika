import py5
import random

stars = []
speed = 0

class Star:
    def __init__(self):
        self.x = random.uniform(-py5.width, py5.width)
        self.y = random.uniform(-py5.height, py5.height)
        self.z = random.uniform(0, py5.width)
        self.pz = self.z

    def update(self):
        global speed
        self.z = self.z - speed

        if self.z < 1:
            self.z = py5.width
            self.x = random.uniform(-py5.width, py5.width)
            self.y = random.uniform(-py5.height, py5.height)
            self.pz = self.z

    def show(self):
        py5.fill(255)
        py5.no_stroke()

        sx = py5.remap(self.x / self.z, 0, 1, 0, py5.width)
        sy = py5.remap(self.y / self.z, 0, 1, 0, py5.height)

        r = py5.remap(self.z, 0, py5.width, 16, 0)
        py5.
        px = py5.remap(self.x / self.pz, 0, 1, 0, py5.width)
        py = py5.remap(self.y / self.pz, 0, 1, 0, py5.height)

        self.pz = self.z

        py5.stroke(255)
        py5.line(px, py, sx, sy)

def setup():
    py5.size(800, 800)
    for i in range(800):
        stars.append(Star())

def draw():
    global speed
    speed = py5.remap(py5.mouse_x, 0, py5.width, 0, 50)
    
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)

    for s in stars:
        s.update()
        s.show()

if __name__ == "__main__":

    py5.run_sketch()
