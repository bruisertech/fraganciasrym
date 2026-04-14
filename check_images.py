from PIL import Image

r = Image.open('malone.png')
print("malone:", r.size, r.getbbox())

m = Image.open('ralone.png')
print("ralone:", m.size, m.getbbox())

both = Image.open('rm-logo1.png')
print("both:", both.size, both.getbbox())
