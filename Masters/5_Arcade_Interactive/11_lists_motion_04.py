"""
1. Use a loop to generate a lot of rain.
"""
import random
import arcade


WIDTH = 640
HEIGHT = 480

rain = arcade.ShapeElementList()

# first set up empty lists
rain_x_positions = []
rain_y_positions = []

tunnel_x_positions = []
tunnel_y_positions = []

for _ in range(0,100,30):
    x = random.randrange(WIDTH + 50)
    y = random.randrange(-50,HEIGHT)

    tunnel_x_positions.append(x)
    tunnel_y_positions.append(y)

# loop 100 times
for _ in range(0,100,30):
    # generate random x and y values
    x = random.randrange(WIDTH+50)
    y = random.randrange(HEIGHT, HEIGHT+50)

    # append the x and y values to the appropriate list
    rain_x_positions.append(x)
    rain_y_positions.append(y)


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_draw = on_draw_2
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    for index in range(len(rain_x_positions)):
        rain_x_positions[index] -= 3
        

        if rain_x_positions[index] < 0:
            rain_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            rain_x_positions[index] = random.randrange(WIDTH, WIDTH+50)

        i


def on_draw():
    arcade.start_render()
    # Draw in here...
    for x, y in zip(rain_x_positions, rain_y_positions):
        arcade.draw_rectangle_filled(x, y, 30, 500,arcade.color.BLUE)

def on_draw_2():
    arcade.start_render()

    for x,y in zip(tunnel_x_positions, tunnel_y_positions):
        arcade.draw_rectangle_filled(x,y,30,500,arcade.color.BLUE)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
