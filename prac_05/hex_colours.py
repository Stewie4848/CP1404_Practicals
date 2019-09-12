HEX_COLOURS = {"aliceblue": "#f0f8ff", "azure1": "#f0ffff", "aquamarine1": "#7fffd4", "beige": "#ffe4c4",
               "blueviolet": "#8a2be2", "burlywood": "#deb887", "cadetblue": "#5f9ea0", "darkgreen": "#006400",
               "floralwhite": "#fffaf0", "ghostwhite": "#f8f8ff", "gainsboro": "#dcdcdc"}

hex_colour = input("Enter hex colour: ").lower()
while hex_colour != "":
    if hex_colour in HEX_COLOURS:
        print(hex_colour, "is", HEX_COLOURS[hex_colour])
    else:
        print("Invalid hex colour")
    hex_colour = input("Enter hex colour: ").lower()
