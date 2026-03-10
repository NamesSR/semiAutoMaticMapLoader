import cv2
import sys

map_data = ""

m = 0
Ax_start = 12
Ay = 8

if len(sys.argv) < 2:
    print("Drag an image onto this program.")
    input("Press Enter to exit...")
    sys.exit()

image_path = sys.argv[1]

img = cv2.imread(image_path)

if img is None:
    print("Failed to load image.")
    input()
    sys.exit()

height, width = img.shape[:2]

if width != 987 or height != 543: # can Resize but do not know if it wor
    print("Resizing image to 987 x 543")
    img = cv2.resize(img, (987, 543))

print("Image size OK: 987 x 543")

for y in range(17):

    Ax = Ax_start

    for x in range(31):

        pixel_color = img[Ay][Ax]
        b, g, r = pixel_color

        print(f"Pixel color at ({x},{y}): {pixel_color}")

        if y in (0, 16) or x in (0,30):
            s = "#"
        else:
            s = "T"

        if s not in ("w", "B"):

            if 65 <= r <= 80 and 150 <= g <= 160 and 80 <= b <= 95:
                map_data += s + "g"

            elif 30 <= r <= 45 and 100 <= g <= 120 and 240 <= b <= 255:
                print("player Color")
                p = input() 
                map_data += f"P{p}"

            elif 35 <= r <= 48 and 95 <= g <= 108 and 40 <= b <= 55:
                map_data += s + "gd"

            elif 40 <= r <= 50 and 40 <= g <= 50 and 40 <= b <= 50:
                map_data += "#b"

            elif 130 <= r <= 140 and 130 <= g <= 140 and 130 <= b <= 140:
                map_data += s + "y"

            elif 60 <= r <= 75 and 60 <= g <= 75 and 60 <= b <= 75:
                map_data += "Fyd"

            elif 90 <= r <= 110 and 85 <= g <= 110 and 90 <= b <= 110:
                map_data += s + "yy"

            elif 165 <= r <= 185 and 50 <= g <= 65 and 50 <= b <= 65:
                map_data += s + "r"
            elif 250 <= r <= 255 and 0 <= g <= 10 and 0 <= b <= 10: 
                print("enemy Color")
                p = input() 
                print("Which Enemy")
                l = input() 
                map_data += f"E{p}{l}" 
                
            elif 250 <= r <= 255 and 250 <= g <= 255 and 250 <= b <= 255:
                print("waipoint Color")
                p = input() 
                print("waiPoint of Which Enemy ")
                l = input() 
                print("WaiPointCount start At 0")
                i = input()
                
                map_data += f"W{p}{l}{i}" 
                
            elif 0 <= r <= 5 and 0 <= g <= 5 and 0 <= b <= 5:
                map_data += "#d" 
            elif 250 <= r <= 255 and 0 <= g <= 5 and 250 <= b <= 255:
                print("powerOrb Color")
                p = input() 
                map_data += f"B{p}"
            else:
                print("Unknown color:", pixel_color)

        Ax += 32
    map_data += ",\n"
    Ay += 32


    

with open("map_output.txt", "w") as f:
    f.write(map_data)

print("Map saved to map_output.txt")
input("Press Enter to exit...")

# print(map_data)