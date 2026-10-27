"""Original code-drawn artwork for Abhishek Tiwari's GitHub README.

Requires Python 3 and Pillow. No network access, credentials or live metrics.
Run from any directory: python design-source/render_assets.py
Font paths below use Linux defaults; point FONT_DIR to your own DejaVu fonts
on another system. All artwork can be regenerated and edited here.
"""
from pathlib import Path
import html
import math
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'Abhii26' / 'assets'
OUT.mkdir(parents=True, exist_ok=True)
FONT_DIR = Path(os.environ.get('FONT_DIR', '/usr/share/fonts/truetype/dejavu'))

def font(size, bold=False, mono=False):
    name = 'DejaVuSansMono' if mono else 'DejaVuSans'
    return ImageFont.truetype(str(FONT_DIR / (name + ('-Bold' if bold else '') + '.ttf')), size)

W, H = 1120, 370
BG, PANEL, LINE = '#0B1220', '#101E30', '#23364D'
WHITE, MUTED, CYAN, VIOLET = '#F1F5FC', '#A9B9CE', '#67E8F9', '#B7A4FF'
base = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(base)
for y in range(H):
    t = y / H
    d.line((0,y,W,y),fill=(11+int(4*t),18+int(7*t),32+int(10*t)))
for x in range(0,W,28):
    for y in range(0,H,28):
        if x > 710: d.ellipse((x,y,x+1,y+1),fill='#20344B')
d.rounded_rectangle((1,1,W-2,H-2),radius=24,outline=LINE,width=2)
d.rounded_rectangle((36,34,133,65),radius=15,fill='#153341')
d.text((53,40),'ABHII26',font=font(16,True,True),fill=CYAN)
d.text((150,41),'PYTHON / VISION / EDGE AI',font=font(15,False,True),fill=MUTED)
d.text((46,99),'Abhishek Tiwari',font=font(53,True),fill=WHITE)
d.text((49,176),'Python Developer',font=font(28),fill=CYAN)
d.text((49,217),'Computer Vision  /  On-Device ML',font=font(23),fill=MUTED)
d.rounded_rectangle((48,279,685,331),radius=10,fill='#0A1422',outline=LINE,width=1)
d.text((65,294),'>',font=font(20,True,True),fill=CYAN)
d.text((795,326),'OFFLINE-FIRST THINKING',font=font(13,False,True),fill=MUTED)

# Stylized, abstract computer-vision face mesh. This is artwork, not a scan.
points=[(888,100),(851,117),(829,161),(830,212),(851,257),(887,281),
        (923,257),(945,212),(945,161),(923,117),(856,164),(879,163),
        (898,163),(921,164),(888,185),(875,215),(899,215),(860,235),
        (889,246),(917,235),(851,193),(925,193),(888,128),(888,226)]
edges=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,0),
       (10,11),(12,13),(11,14),(12,14),(14,15),(14,16),(15,16),(17,18),
       (18,19),(10,20),(20,17),(13,21),(21,19),(0,22),(22,11),(22,12),
       (2,10),(8,13),(15,23),(16,23),(23,18),(4,17),(6,19),(18,5),
       (1,22),(9,22),(20,15),(21,16),(3,20),(7,21)]
for a,b in edges: d.line((*points[a],*points[b]),fill='#385669',width=2)
for x,y in points: d.ellipse((x-2,y-2,x+2,y+2),fill=CYAN)
for x,y,dx,dy in [(803,86,1,1),(970,86,-1,1),(803,297,1,-1),(970,297,-1,-1)]:
    d.line((x,y,x+dx*24,y),fill=VIOLET,width=3)
    d.line((x,y,x,y+dy*24),fill=VIOLET,width=3)

frames=[]
messages=['build > Python APIs','run > Vision on device','tune > Inference pipelines']
for i in range(60):
    im=base.copy();p=ImageDraw.Draw(im)
    message=messages[i//20]
    count=min(len(message),int((i%20)/11*len(message)))
    # Keep the first frame useful before animation starts.
    if i==0: count=len(message)
    label=message[:count]
    p.text((96,294),label,font=font(20,False,True),fill='#D0DAE9')
    if i%8<5:
        cursor=96+int(p.textlength(label,font=font(20,False,True)))+4
        p.rectangle((cursor,295,cursor+8,316),fill=CYAN)
    scan_y=108+int((math.sin(i/60*math.pi*2-math.pi/2)+1)*78)
    p.line((813,scan_y,962,scan_y),fill=CYAN,width=2)
    angle=i/60*math.pi*2
    for off in [0,math.pi]:
        x=887+int(103*math.cos(angle+off)); y=190+int(103*math.sin(angle+off))
        p.ellipse((x-4,y-4,x+4,y+4),fill=VIOLET)
    frames.append(im)
palette=frames[0].quantize(colors=112,method=Image.Quantize.MEDIANCUT)
indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
indexed[0].save(OUT/'hero.gif',save_all=True,append_images=indexed[1:],duration=100,loop=0,optimize=True,disposal=1)
frames[0].save(OUT/'hero-static.png',optimize=True)

# A less dense composition for phone-width README containers.
mobile=Image.new('RGB',(640,360),BG)
q=ImageDraw.Draw(mobile)
q.rounded_rectangle((1,1,638,358),radius=24,outline=LINE,width=2)
q.text((30,27),'ABHII26 / ENGINEERING',font=font(16,False,True),fill=CYAN)
q.text((27,85),'Abhishek Tiwari',font=font(44,True),fill=WHITE)
q.text((30,158),'Python Developer',font=font(28),fill=CYAN)
q.text((30,206),'Computer Vision / On-Device ML',font=font(23),fill=MUTED)
q.rounded_rectangle((29,276,610,330),radius=10,fill='#0A1422',outline=LINE,width=1)
mobile_frames=[]
for i in range(60):
    im=mobile.copy();q=ImageDraw.Draw(im)
    message=messages[i//20]
    count=len(message) if i==0 else min(len(message),int((i%20)/11*len(message)))
    q.text((45,292),'> '+message[:count],font=font(20,False,True),fill=CYAN)
    q.line((30,251,30+int(580*((i%20)+1)/20),251),fill=VIOLET,width=2)
    mobile_frames.append(im)
mp=mobile_frames[0].quantize(colors=96)
mi=[f.quantize(palette=mp,dither=Image.Dither.NONE) for f in mobile_frames]
mi[0].save(OUT/'hero-mobile.gif',save_all=True,append_images=mi[1:],duration=100,loop=0,optimize=True,disposal=1)
mobile_frames[0].save(OUT/'hero-mobile-static.png',optimize=True)

def esc(t): return html.escape(t)
def svg(width,height,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><style>text{{font-family:system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif}}</style>{body}</svg>\n'
def text(x,y,t,size=20,color=WHITE,weight=400):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}">{esc(t)}</text>'

cards=''
for i,(metric,title,detail,color) in enumerate([
    ('29%','Less group-photo time','210 s to 150 s',CYAN),
    ('< 3 s','On-device selfie recognition','Measured in professional work',VIOLET),
    ('3 feeds','RTSP inference on Jetson','Batched multi-stream pipeline',CYAN)]):
    x=4+i*374
    cards+=f'<rect x="{x}" y="4" width="364" height="176" rx="18" fill="{PANEL}" stroke="{LINE}"/>'
    cards+=f'<rect x="{x+23}" y="25" width="32" height="3" rx="1" fill="{color}"/>'
    cards+=text(x+23,82,metric,42,color,700)+text(x+23,119,title,19,WHITE,600)+text(x+23,149,detail,16,MUTED)
(OUT/'impact.svg').write_text(svg(1120,186,cards))
mobile_impact=''
for i,(metric,title,detail,color) in enumerate([
    ('29%','Less processing time','Group photos: 210 s to 150 s',CYAN),
    ('< 3 s','Selfie recognition','Measured on device',VIOLET),
    ('3 feeds','RTSP inference','Batched pipeline on Jetson Orin',CYAN)]):
    y=4+i*134
    mobile_impact+=f'<rect x="2" y="{y}" width="636" height="124" rx="18" fill="{PANEL}" stroke="{LINE}"/>'
    mobile_impact+=text(25,y+74,metric,40,color,700)+text(208,y+49,title,24,WHITE,600)+text(208,y+85,detail,19,MUTED)
(OUT/'impact-mobile.svg').write_text(svg(640,408,mobile_impact))

for name,title,description,stack,idx,color,cta in [
    ('faceauth','FaceAuth','Offline enrollment and face authentication.','Flutter / Dart / SQLite','01',CYAN,'PROJECT NOTES'),
    ('facialytics','Facialytics','Webcam recognition with face-api.js.','Node.js / Express / JavaScript','02',VIOLET,'VIEW SOURCE'),
    ('shortifly','Shortifly','URL shortening with click analytics.','Node.js / Express / MongoDB','03',CYAN,'VIEW SOURCE')]:
    b=f'<rect x="1" y="1" width="1118" height="158" rx="18" fill="{PANEL}" stroke="{LINE}"/>'
    b+=f'<rect x="25" y="27" width="78" height="106" rx="16" fill="#132A3C"/>'
    b+=text(39,91,idx,30,color,700)
    b+=text(132,52,title,29,WHITE,700)+text(132,86,description,21,MUTED)+text(132,121,stack,17,color)
    b+=f'<rect x="879" y="55" width="210" height="47" rx="23" fill="#142A3D" stroke="{LINE}"/>'
    b+=text(902,85,cta,16,color,600)
    (OUT/f'{name}.svg').write_text(svg(1120,160,b))
    mb=f'<rect x="1" y="1" width="638" height="138" rx="18" fill="{PANEL}" stroke="{LINE}"/>'
    mb+=text(25,81,idx,30,color,700)+text(97,56,title,31,WHITE,700)+text(97,100,stack,19,color)
    (OUT/f'{name}-mobile.svg').write_text(svg(640,140,mb))

for name,label,color in [('linkedin','LinkedIn',CYAN),('email','Email me',VIOLET)]:
    b=f'<rect x="1" y="1" width="176" height="46" rx="23" fill="{PANEL}" stroke="{LINE}"/>'
    b+=f'<circle cx="25" cy="24" r="4" fill="{color}"/>'+text(42,30,label,17,WHITE,600)
    (OUT/f'{name}.svg').write_text(svg(178,48,b))
print('Created',len(list(OUT.iterdir())),'assets; GIF', (OUT/'hero.gif').stat().st_size,'bytes')
