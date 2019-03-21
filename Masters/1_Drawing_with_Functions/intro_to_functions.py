def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

   # call your draw functions

    draw_sun()

        # Call on_draw every 60th of a second.
   arcade.schedule(on_draw, 1 / 60)
   arcade.run()

    # Call the main function to get the program started.


    arcade.finish_render()
    arcade.run()

main()
