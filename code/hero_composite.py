from PIL import Image, ImageDraw, ImageFont
import os, glob
HERE=os.path.dirname(__file__); ROOT=os.path.normpath(os.path.join(HERE,".."))
src=sorted(glob.glob(os.path.join(ROOT,"hero_source","*.webp")))[0]
im=Image.open(src).convert("RGB")
W,H=im.size
# dark scrim over top third
overlay=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(overlay)
for y in range(int(H*0.42)):
    a=int(200*(1-y/(H*0.42)))
    d.line([(0,y),(W,y)], fill=(10,12,14,a))
im=Image.alpha_composite(im.convert("RGBA"), overlay); d=ImageDraw.Draw(im)
def font(sz):
    for path in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        try: return ImageFont.truetype(path, sz)
        except: pass
    return ImageFont.load_default()
d.text((60,50),"80.6% of scheduled",font=font(92),fill=(232,163,23,255))
d.text((60,160),"window-days are excavations",font=font(92),fill=(255,255,255,255))
d.text((60,285),"6,348 excavation permits of 20,500 in Nashville's active right-of-way layer",font=font(40),fill=(180,230,228,255))
d.text((60,345),"Machine Readable - Metro Nashville Active Right-of-Way Permits, Nov 12, 2026",font=font(34),fill=(220,220,220,255))
im.convert("RGB").save(os.path.join(ROOT,"hero.png"))
open(os.path.join(ROOT,"hero-headline.txt"),"w").write("80.6% of scheduled window-days are excavations\n")
print("hero done", im.size)
