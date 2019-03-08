import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

# define your draw functions
arcade.start_render()

#Parameters for clouds
def draw_cloud(x,y):
    arcade.draw_circle_filled(250 + x, 500 + y, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(330 + x, 550 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(390 + x, 500 + y, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(330 + x,470 + y,40,arcade.color.WHITE)
    arcade.draw_circle_filled(650 + x, 500 + y, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(730 + x, 550 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(790 + x, 500 + y, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(730 + x, 470 + y, 40, arcade.color.WHITE)

#Parameters for hill
def draw_hill():
    arcade.draw_circle_filled(150,-190,400,arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(600,-150,300,arcade.color.DARK_GREEN)

#Parameters for tree
def draw_tree(x,y):
      arcade.draw_circle_filled(250+x,300+y, 50, arcade.color.DARK_GREEN)
      arcade.draw_circle_filled(290+x,270+y, 30, arcade.color.DARK_GREEN)
      arcade.draw_circle_filled(260+x,260+y, 30, arcade.color.DARK_GREEN)
      arcade.draw_circle_filled(230+x,250+y,40,arcade.color.DARK_GREEN)
      arcade.draw_rectangle_filled(250+x, 230+y, 45, 150,arcade.color.PALE_BROWN)

#parameters for apple
def draw_apple(x,y):
    arcade.draw_circle_filled(x,y,10,arcade.color.RED)

def draw_sun(x,y):
    arcade.draw_circle_filled(x,600+y,70, arcade.color.YELLOW)

    arcade.finish_render()

#moving sun
def on_draw(delta_time):
    global draw_sun_x

    """ Draw everything """
    arcade.start_render()

    draw_tree(10,20)
    draw_tree(70,-10)
    draw_tree(300,-10)
    draw_apple(250,350)
    draw_apple(220,300)
    draw_apple(280,250)
    draw_apple(280,300)
    draw_hill()

    draw_sun(draw_sun_x, 140)
    draw_cloud(draw_cloud_x,140)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    draw_sun_x += 1

draw_sun_x = 140

#moving cloud
def moving(delta_time):
    global draw_cloud_x

    arcade.start_render()

    draw_cloud(draw_cloud_x,100)
    draw_cloud_x += 1

#Create a value that our snow_person1_x will start at.
draw_cloud_x = 100

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/30)
    arcade.schedule(moving, 1/60)
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()