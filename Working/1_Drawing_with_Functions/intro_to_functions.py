import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions

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


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    draw_hill()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()