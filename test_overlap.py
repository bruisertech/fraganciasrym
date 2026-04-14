from PIL import Image

r = Image.open('ralone.png').convert("RGBA")
m = Image.open('malone.png').convert("RGBA")

# Create a blank canvas
canvas = Image.new("RGBA", r.size)
canvas.paste(r, (0, 0), r)
canvas.paste(m, (0, 0), m)
canvas.save('overlap_test.png')
