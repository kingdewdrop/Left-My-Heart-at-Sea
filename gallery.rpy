init:
    # Position the navigation on the right side of the screen.
    $ style.gallery_nav_frame.xpos = 800 - 10
    $ style.gallery_nav_frame.xanchor = 1.0
    $ style.gallery_nav_frame.ypos = 12

    # Add the gallery to the main menu.
    $ config.main_menu.insert(2, ('Gallery', "gallery", "True"))

# The entry point to the gallery code.
label gallery:
    python hide:

        # Construct a new gallery object.
        g = Gallery()


        g.locked_button = "button.jpg"
        g.locked_background = "docked.jpg"
        g.hover_border = "button2.jpg"
        g.idle_border = "button2.jpg"

        # An images used as the background of the various gallery pages.
        g.background = "gallery.jpg"

        # Lay out the gallery images on the screen.
        # These settings lay images out 3 across and 4 down.
        # The upper left corner of the gird is at xpos 10, ypos 20.
        # They expect button images to be 155x112 in size.
        g.grid_layout((2, 4), (10, 12), (160, 124))

        # Show the background page.
        g.page("Ashten")

        g.button("button2.jpg")
        g.unlock_image("dock")
        
        g.button("button2.jpg")
        g.unlock_image("dock")
        
        g.button("button2.jpg")
        g.unlock_image("dock")
        
        g.button("button2.jpg")
        g.unlock_image("dock")
        
        g.button("button2.jpg")
        g.unlock_image("dock")
        
        g.button("button2.jpg")
        g.unlock_image("dock")
        
        g.button("button2.jpg")
        g.unlock_image("dock")
        
        g.button("button2.jpg")
        g.condition("persistent.unlock_1")
        g.display("Midnight Snack")
        
        
        
        g.page("Larissa")
        
        g.button("button2.jpg")
        g.unlock_image("ocean")
        
        g.button("button2.jpg")
        g.unlock_image("ocean")
        
        g.button("button2.jpg")
        g.unlock_image("ocean")
        
        g.button("button2.jpg")
        g.unlock_image("ocean")
        
        g.button("button2.jpg")
        g.unlock_image("ocean")
        
        g.button("button2.jpg")
        g.unlock_image("ocean")
        
        g.button("button2.jpg")
        g.unlock_image("ocean")
        
        g.button("button2.jpg")
        g.condition("persistent.unlock_1")
        g.display("Midnight Snack")
        
        g.page("Mistral")

        g.button("button2.jpg")
        g.unlock_image("dock")
        
        g.button("button2.jpg")
        g.condition("persistent.unlock_1")
        g.display("Midnight Snack")

        # Now, show the gallery.
        g.show()
        

    jump main_menu_screen