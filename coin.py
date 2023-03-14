alien = Actor('alien')
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        alien_hurt()
    else:
        print("You missed me!")

def alien_hurt():
    print("Eek!")
    alien.image = 'alien_hurt'
    clock.schedule_unique(set_alien_normal, 1.0)
def set_alien_normal():
    alien.image = 'alien'
