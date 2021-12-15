import colorgram

colors = colorgram.extract('/home/jeremy/repos/Udemy/100 days of Python/Day 18 - Turtle and GUI/hirst_painting.jpg', 30)

rgb_list = []
rgb_tuple = ()

for color in range(30):
    first_color = colors[color]
    rgb = first_color.rgb
    rgb_tuple = (rgb[0],rgb[1],rgb[2])
    rgb_list.append(rgb_tuple)

print(rgb_list)