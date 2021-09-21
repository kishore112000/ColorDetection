# importing libraries

import pandas as pd
import cv2

# creating a image path
# creating a csv file path

img_path = 'pic2.jpg'
csv_path = 'colors.csv'

# index variable with attributes

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)

# getting the image

img = cv2.imread(img_path)

# resizing the image
img = cv2.resize(img, (800, 600))

clicked = False
r = g = b = x_pos = y_pos = 0

# function to get the colour in the image

def get_color_name(R, G, B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, 'color_name']

    return cname


print(get_color_name(255, 255, 255))

# function to determine the positions

def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r, g, b, x_pos, y_pos
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


# on mouse click draw function is called

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

# displaying the colours while mouse is clicked

while True:
    cv2.imshow('image', img)
    if clicked:
        cv2.rectangle(img, (20, 20), (600, 60), (b, g, r), -1)
        text = get_color_name(r, g, b) + 'R=' + str(r) + 'G=' + str(g) + 'B=' + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break

# destroy the windows

cv2.destroyAllWindows()
