import py5
import random

# Premenná pre rýchlosť a zoznam hviezd
stars = []
speed = 0

class Star:
    def __init__(self):
        # Inicializácia pozície (x, y od -width po width kvôli translate)
        self.x = random.uniform(-py5.width, py5.width)
        self.y = random.uniform(-py5.height, py5.height)
        self.z = random.uniform(0, py5.width)
        self.pz = self.z  # Predchádzajúca poloha Z

    def update(self):
        global speed
        self.z = self.z - speed
        
        # Ak hviezda zmizne v "kamere", resetuj ju na koniec
        if self.z < 1:
            self.z = py5.width
            self.x = random.uniform(-py5.width, py5.width)
            self.y = random.uniform(-py5.height, py5.height)
            self.pz = self.z

    def show(self):
        py5.fill(255)
        py5.no_stroke()

        # Projekcia 3D súradníc na 2D plochu obrazovky
        sx = py5.remap(self.x / self.z, 0, 1, 0, py5.width)
        sy = py5.remap(self.y / self.z, 0, 1, 0, py5.height)

        # Polomer hviezdy sa zväčšuje, čím je bližšie (menšie z)
        r = py5.remap(self.z, 0, py5.width, 16, 0)
        py5.ellipse(sx, sy, r, r)

        # Výpočet predchádzajúcej pozície pre efekt čiary (motion blur)
        px = py5.remap(self.x / self.pz, 0, 1, 0, py5.width)
        py = py5.remap(self.y / self.pz, 0, 1, 0, py5.height)

        self.pz = self.z

        py5.stroke(255)
        py5.line(px, py, sx, sy)

def setup():
    py5.size(800, 800)
    # Vytvorenie 800 hviezd (ekvivalent Star[800])
    for i in range(800):
        stars.append(Star())

def draw():
    global speed
    # Mapovanie pozície myši na rýchlosť
    speed = py5.remap(py5.mouse_x, 0, py5.width, 0, 50)
    
    py5.background(0)
    # Posun súradníc do stredu obrazovky (ako v Java kóde)
    py5.translate(py5.width / 2, py5.height / 2)
    
    # Prechádzanie zoznamu hviezd a volanie metód
    for s in stars:
        s.update()
        s.show()

if __name__ == "__main__":
    py5.run_sketch()