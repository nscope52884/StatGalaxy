from PIL import Image

img = Image.open(r'C:\Users\nscop\Documents\Projects\StatGalaxy\Logos\Logo_Rough_Draft.png')
img = img.convert("RGBA")
datas = img.getdata()
threshold = 75

newData = []
for item in datas:
    if item[0] >= threshold and item[1] >= threshold and item[2] >= threshold:
        newData.append((0, 0, 0, 255))
    else:
        newData.append((255, 255, 255, 255))

img.putdata(newData)
img.save(r'C:\Users\nscop\Documents\Projects\StatGalaxy\Logos\Logo_Rough_Draft_Inverse.png', "PNG")
