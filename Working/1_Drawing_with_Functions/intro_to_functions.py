import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
arcade.start_render()

def draw_cloud(x,y):
    '''Draw white clouds '''

    arcade.draw_circle_filled(250 + x, 500 + y, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(330 + x, 550 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(390 + x, 500 + y, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(330 + x,470 + y,40,arcade.color.WHITE)
    arcade.draw_circle_filled(650 + x, 500 + y, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(730 + x, 550 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(790 + x, 500 + y, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(730 + x, 470 + y, 40, arcade.color.WHITE)

def draw_hill():
    arcade.draw_circle_filled(150,-190,400,arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(600,-150,300,arcade.color.DARK_GREEN)

def draw_tree(x,y):
      arcade.draw_circle_filled(250+x,300+y, 50, arcade.color.DARK_GREEN)
      arcade.draw_circle_filled(290+x,270+y, 30, arcade.color.DARK_GREEN)
      arcade.draw_circle_filled(260+x,260+y, 30, arcade.color.DARK_GREEN)
      arcade.draw_circle_filled(230+x,250+y,40,arcade.color.DARK_GREEN)
      arcade.draw_rectangle_filled(250+x, 230+y, 45, 150,arcade.color.PALE_BROWN)

def draw_sun():
    arcade.draw_circle_filled(50,600,70, arcade.color.YELLOW)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE
                                )
    arcade.start_render()

   # call your draw functions
    draw_cloud(100,10)
    draw_cloud(200,40)
    draw_cloud(250,80)
    draw_tree(10,20)
    draw_tree(50,50)
    draw_tree(100,300)
    draw_hill()
    draw_sun()

    arcade.finish_render()
    arcade.run()

main()









