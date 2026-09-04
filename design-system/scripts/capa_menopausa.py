#!/usr/bin/env python3
# Capa YouTube: "ENGORDOU NA MENOPAUSA? A CULPA NAO E SUA"
# Roda no sandbox do Higgsfield. Espera em /home/user: bg.png, cutout.png, prop.png, anton.ttf
# Saida: capa.png (1280x720) e capa-prev.jpg (preview leve)
# Canvas 2x (2560x1440) e downscale LANCZOS para matar serrilhado.
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops, ImageEnhance

W, H = 2560, 1440
SS = 2  # fator de supersampling (saida = W/SS x H/SS)

def load(p):
    return Image.open(p).convert('RGBA')

def cover(im, w, h):
    r = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * r + 0.5), int(im.height * r + 0.5)), Image.LANCZOS)
    x = (im.width - w) // 2
    y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))

canvas = cover(load('bg.png'), W, H)
canvas = ImageEnhance.Color(canvas).enhance(1.18)
canvas = ImageEnhance.Contrast(canvas).enhance(1.06)

# escurece a metade esquerda p/ texto
grad = Image.new('L', (W, 1))
for x in range(W):
    t = max(0.0, 1.0 - x / (W * 0.62))
    grad.putpixel((x, 0), int(200 * (t ** 1.3)))
grad = grad.resize((W, H))
canvas = Image.composite(Image.new('RGBA', (W, H), (8, 4, 16, 255)), canvas, grad)

# ---------- foto ----------
cut = load('cutout.png')
bb = cut.split()[3].getbbox()
cut = cut.crop(bb)
# escala pela altura: busto grande, ancorado embaixo a direita
ph = int(H * 1.18)
r = ph / cut.height
cut = cut.resize((int(cut.width * r), ph), Image.LANCZOS)
px = W - cut.width + int(0.06 * cut.width)   # encosta na direita
py = H - int(cut.height * 0.96)              # corta um pouco do fundo (mesa)

amask = cut.split()[3]

# glow roxo/dourado atras dela
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
gsil = Image.new('RGBA', (W, H), (0, 0, 0, 0))
gsil.paste(Image.new('RGBA', cut.size, (168, 60, 190, 255)), (px, py), amask)
gsil = gsil.filter(ImageFilter.GaussianBlur(70))
canvas = ImageChops.screen(canvas, gsil)
gsil2 = Image.new('RGBA', (W, H), (0, 0, 0, 0))
gsil2.paste(Image.new('RGBA', cut.size, (255, 170, 40, 255)), (px + 60, py - 20), amask)
gsil2 = gsil2.filter(ImageFilter.GaussianBlur(120))
gsil2.putalpha(gsil2.split()[3].point(lambda a: a * 45 // 100))
canvas = Image.alpha_composite(canvas, gsil2)

# sombra projetada
sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sh.paste(Image.new('RGBA', cut.size, (0, 0, 0, 190)), (px - 46, py + 30), amask)
sh = sh.filter(ImageFilter.GaussianBlur(38))
canvas = Image.alpha_composite(canvas, sh)

# grading da foto: contraste, saturacao, highlights quentes, sombras magenta
c = ImageEnhance.Contrast(cut).enhance(1.13)
c = ImageEnhance.Color(c).enhance(1.14)
c = ImageEnhance.Brightness(c).enhance(1.02)
warm = Image.new('RGBA', c.size, (255, 176, 90, 255))
c = Image.composite(Image.blend(c, ImageChops.screen(c, warm), 0.10), c, c.convert('L').point(lambda v: v if v > 120 else 0))
mag = Image.new('RGBA', c.size, (120, 30, 110, 255))
c = Image.composite(Image.blend(c, ImageChops.multiply(c, ImageChops.invert(mag)), 0.0), c, Image.new('L', c.size, 0))
c = Image.blend(c, ImageChops.overlay(c, Image.new('RGBA', c.size, (150, 60, 140, 255))), 0.06)
c.putalpha(amask)

# rim light direcional: magenta na esquerda, dourado na direita
er = amask.filter(ImageFilter.MinFilter(9))
rim = ImageChops.subtract(amask, er)
left = Image.new('L', amask.size, 0)
dl = ImageDraw.Draw(left)
dl.rectangle((0, 0, amask.width // 2, amask.height), fill=255)
rimL = ImageChops.multiply(rim, left)
rimR = ImageChops.multiply(rim, ImageChops.invert(left))
rl = Image.new('RGBA', amask.size, (0, 0, 0, 0))
rl.paste(Image.new('RGBA', amask.size, (255, 90, 220, 255)), (0, 0), rimL.filter(ImageFilter.GaussianBlur(3)))
rl.paste(Image.new('RGBA', amask.size, (255, 214, 120, 255)), (0, 0), rimR.filter(ImageFilter.GaussianBlur(3)))
c = ImageChops.screen(c, rl)
c.putalpha(amask)
canvas.paste(c, (px, py), c)

# ---------- prop (balanca + fita) ----------
prop = load('prop.png')
pb = prop.split()[3].getbbox()
prop = prop.crop(pb)
pw = 830
pr = pw / prop.width
prop = prop.resize((pw, int(prop.height * pr)), Image.LANCZOS)
ppx, ppy = 980, H - prop.height + 60
pg = Image.new('RGBA', (W, H), (0, 0, 0, 0))
pg.paste(Image.new('RGBA', prop.size, (255, 60, 160, 255)), (ppx, ppy), prop.split()[3])
pg = pg.filter(ImageFilter.GaussianBlur(55))
pg.putalpha(pg.split()[3].point(lambda a: a * 70 // 100))
canvas = ImageChops.screen(canvas, pg)
psh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
psh.paste(Image.new('RGBA', prop.size, (0, 0, 0, 200)), (ppx - 24, ppy + 26), prop.split()[3])
psh = psh.filter(ImageFilter.GaussianBlur(28))
canvas = Image.alpha_composite(canvas, psh)
pc = ImageEnhance.Contrast(prop).enhance(1.1)
pc = ImageEnhance.Color(pc).enhance(1.15)
canvas.paste(pc, (ppx, ppy), pc)

# ---------- texto ----------
def font(sz):
    return ImageFont.truetype('anton.ttf', sz)

def fit(text, maxw, start=400):
    sz = start
    while sz > 40:
        f = font(sz)
        if f.getbbox(text)[2] - f.getbbox(text)[0] <= maxw:
            return f, sz
        sz -= 4
    return font(40), 40

def text_layer(text, f, fill, stroke, sw, pad=80):
    b = f.getbbox(text)
    w = b[2] - b[0] + 2 * pad
    h = b[3] - b[1] + 2 * pad
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.text((pad - b[0], pad - b[1]), text, font=f, fill=fill, stroke_width=sw, stroke_fill=stroke)
    return im

def gold_gradient(im):
    # aplica gradiente vertical dourado so no preenchimento (nao no stroke)
    a = im.split()[3]
    g = Image.new('RGBA', im.size, (0, 0, 0, 0))
    top, bot = (255, 240, 150), (206, 110, 8)
    for y in range(im.height):
        t = y / im.height
        col = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
        ImageDraw.Draw(g).line((0, y, im.width, y), fill=col + (255,))
    g.putalpha(a)
    return g

def shear(im, deg):
    t = math.tan(math.radians(deg))
    nw = im.width + int(abs(t) * im.height)
    return im.transform((nw, im.height), Image.AFFINE, (1, t, (-t * im.height if t > 0 else 0), 0, 1, 0), resample=Image.BICUBIC)

def hard_shadow(layer, off=(14, 16)):
    shl = Image.new('RGBA', layer.size, (0, 0, 0, 0))
    shl.paste(Image.new('RGBA', layer.size, (0, 0, 0, 210)), off, layer.split()[3])
    shl = shl.filter(ImageFilter.GaussianBlur(6))
    return Image.alpha_composite(shl, layer)

MAXW = 1300
# L1 branco
f1, _ = fit('ENGORDOU NA', MAXW)
l1 = text_layer('ENGORDOU NA', f1, (255, 255, 255, 255), (0, 0, 0, 255), 20)
l1 = hard_shadow(shear(l1, -7))
# L2 dourado gigante
f2, _ = fit('MENOPAUSA?', MAXW + 60)
l2f = text_layer('MENOPAUSA?', f2, (255, 255, 255, 255), None, 0)
l2g = gold_gradient(l2f)
l2s = text_layer('MENOPAUSA?', f2, (0, 0, 0, 0), (0, 0, 0, 255), 22)
l2 = Image.alpha_composite(l2s, l2g)
# glow externo dourado
gl = Image.new('RGBA', l2.size, (0, 0, 0, 0))
gl.paste(Image.new('RGBA', l2.size, (255, 200, 60, 255)), (0, 0), l2.split()[3])
gl = gl.filter(ImageFilter.GaussianBlur(26))
gl.putalpha(gl.split()[3].point(lambda a: a * 55 // 100))
l2 = Image.alpha_composite(gl, l2)
l2 = hard_shadow(shear(l2, -7))

block = Image.new('RGBA', (1900, l1.height + l2.height + 40), (0, 0, 0, 0))
block.paste(l1, (0, 0), l1)
block.paste(l2, (0, l1.height - 60), l2)
block = block.rotate(1.6, expand=True, resample=Image.BICUBIC)
canvas.paste(block, (60, 60), block)

# faixa vermelha "A CULPA NAO E SUA"
fb, _ = fit('A CULPA NÃO É SUA', 1080, 200)
tb = fb.getbbox('A CULPA NÃO É SUA')
bw, bh = tb[2] - tb[0] + 120, tb[3] - tb[1] + 76
band = Image.new('RGBA', (bw + 40, bh + 40), (0, 0, 0, 0))
bd = ImageDraw.Draw(band)
bd.rounded_rectangle((20, 20, 20 + bw, 20 + bh), radius=16, fill=(196, 16, 24, 255))
bd.rounded_rectangle((20, 20 + bh - 14, 20 + bw, 20 + bh), radius=7, fill=(140, 6, 14, 255))
bd.text((20 + 60 - tb[0], 20 + 34 - tb[1]), 'A CULPA NÃO É SUA', font=fb, fill=(255, 255, 255, 255))
band = band.rotate(-2.4, expand=True, resample=Image.BICUBIC)
band = hard_shadow(band, (12, 14))
canvas.paste(band, (95, 905), band)

# interrogacoes amarelas
for (qx, qy, qs, qr) in ((1500, 90, 240, -14), (2320, 330, 170, 12), (1180, 300, 150, 18)):
    ql = text_layer('?', font(qs), (255, 226, 52, 255), (0, 0, 0, 255), 16)
    ql = hard_shadow(ql.rotate(qr, expand=True, resample=Image.BICUBIC), (8, 10))
    canvas.paste(ql, (qx, qy), ql)

# seta amarela curva apontando para a balanca
ar = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ad = ImageDraw.Draw(ar)
p0, p1, p2 = (700, 1210), (900, 1330), (1090, 1230)
pts = []
for i in range(41):
    t = i / 40
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    pts.append((x, y))
for wd, colr in ((46, (0, 0, 0, 255)), (30, (255, 226, 52, 255))):
    ad.line(pts, fill=colr, width=wd, joint='curve')
# cabeca da seta
ang = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
for wd, colr in ((1.55, (0, 0, 0, 255)), (1.0, (255, 226, 52, 255))):
    L = 95 * wd
    a1, a2 = ang + 2.6, ang - 2.6
    tri = [p2, (p2[0] + L * math.cos(a1), p2[1] + L * math.sin(a1)), (p2[0] + L * math.cos(a2), p2[1] + L * math.sin(a2))]
    ad.polygon(tri, fill=colr)
ar = hard_shadow(ar, (8, 10))
canvas = Image.alpha_composite(canvas, ar)

# vinheta
vg = Image.new('L', (W, H), 0)
vd = ImageDraw.Draw(vg)
vd.ellipse((-W * 0.25, -H * 0.35, W * 1.25, H * 1.35), fill=255)
vg = vg.filter(ImageFilter.GaussianBlur(220))
canvas = Image.composite(canvas, ImageEnhance.Brightness(canvas).enhance(0.62), vg)

out = canvas.convert('RGB').resize((W // SS, H // SS), Image.LANCZOS)
out.save('capa.png')
out.resize((960, 540), Image.LANCZOS).save('capa-prev.jpg', quality=72)
print('OK', out.size)
