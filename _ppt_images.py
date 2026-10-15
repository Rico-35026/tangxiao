# -*- coding: utf-8 -*-
import olefile, os, re

p = r'C:\Users\t2412\Desktop\基于 TRIZ 理论的自适应浮桥结构及其施工方法的设计与研发.ppt'
ole = olefile.OleFileIO(p)
streams = {
    'pics': ole.openstream('Pictures').read(),
    'doc': ole.openstream('PowerPoint Document').read(),
}

outdir = r'd:\ai\2627vscode\ppt_images'
os.makedirs(outdir, exist_ok=True)

png_sig = b'\x89PNG\r\n\x1a\n'
jpg_sig = b'\xff\xd8\xff'
gif_sig = b'GIF8'

def carve(buf, tag):
    found = []
    # PNG
    for m in re.finditer(re.escape(png_sig), buf):
        s = m.start()
        e = buf.find(b'IEND\xaeB`\x82', s)
        if e != -1:
            found.append(('png', s, e + 8))
    # JPEG
    for m in re.finditer(re.escape(jpg_sig), buf):
        s = m.start()
        e = buf.find(b'\xff\xd9', s)
        if e != -1 and e - s < 10_000_000:
            found.append(('jpg', s, e + 2))
    # GIF
    for m in re.finditer(re.escape(gif_sig), buf):
        s = m.start()
        e = buf.find(b'\x00;', s)
        if e != -1 and e - s < 5_000_000:
            found.append(('gif', s, e + 2))
    return found

saved = []
for tag, buf in streams.items():
    items = carve(buf, tag)
    items.sort(key=lambda x: x[1])
    for i, (ext, s, e) in enumerate(items):
        data = buf[s:e]
        if len(data) < 3000:  # skip tiny icons
            continue
        fn = '%s_%02d.%s' % (tag, i, ext)
        with open(os.path.join(outdir, fn), 'wb') as f:
            f.write(data)
        saved.append((fn, len(data)))

for fn, size in saved:
    print(fn, size)
print('TOTAL:', len(saved))
