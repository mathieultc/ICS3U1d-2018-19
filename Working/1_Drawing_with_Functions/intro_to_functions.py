import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
arcade.start_render()

def draw_cloud():
    '''Draw white clouds '''
    arcade.draw_circle_filled(250, 500, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(330, 550, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(390, 500, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(330,470,40,arcade.color.WHITE)
    arcade.draw_circle_filled(650, 500, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(730, 550, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(790, 500, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(730, 470, 40, arcade.color.WHITE)

def draw_hill():
    arcade.draw_circle_filled(150,-190,400,arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(600,-150,300,arcade.color.DARK_GREEN)

def draw_tree():
      arcade.draw_circle_filled(250,300, 50, arcade.color.DARK_GREEN)
      arcade.draw_circle_filled(290,270, 30, arcade.color.DARK_GREEN)
      arcade.draw_circle_filled(260,260, 30, arcade.color.DARK_GREEN)
      arcade.draw_circle_filled(230,250,40,arcade.color.DARK_GREEN)
      arcade.draw_rectangle_filled(250, 230, 45, 150,arcade.color.PALE_BROWN)

def draw_sun():
    arcade.draw_circle_filled(50,600,70, arcade.color.YELLOW)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE
                                )
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    draw_tree()
    draw_hill()
    draw_sun()

    arcade.finish_render()
    arcade.run()

main()









