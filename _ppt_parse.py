# -*- coding: utf-8 -*-
import olefile, struct, io, sys

p = r'C:\Users\t2412\Desktop\基于 TRIZ 理论的自适应浮桥结构及其施工方法的设计与研发.ppt'
ole = olefile.OleFileIO(p)
doc = ole.openstream('PowerPoint Document').read()

RT_SLIDE = 0x03EE
RT_NOTES = 0x03EC
RT_MASTER = 0x03F0
RT_TEXTCHARS = 0x0FA0   # UTF-16LE
RT_TEXTBYTES = 0x0FA8   # ANSI bytes

def walk(data, start, end, depth, ctx, results):
    pos = start
    while pos + 8 <= end:
        ver_inst, rtype, rlen = struct.unpack_from('<HHI', data, pos)
        body = pos + 8
        if body + rlen > end:
            break
        ver = ver_inst & 0x000F
        if rtype == RT_SLIDE and ver == 0xF:
            results.append(('SLIDE_START', None))
            walk(data, body, body + rlen, depth + 1, 'slide', results)
            results.append(('SLIDE_END', None))
            pos = body + rlen
            continue
        if rtype == RT_NOTES and ver == 0xF:
            pos = body + rlen  # skip notes text
            continue
        if rtype == RT_TEXTCHARS:
            raw = data[body:body + rlen]
            try:
                t = raw.decode('utf-16-le', errors='ignore')
            except Exception:
                t = ''
            if t.strip():
                results.append(('TEXT', t))
        elif rtype == RT_TEXTBYTES:
            raw = data[body:body + rlen]
            for enc in ('gbk', 'latin-1'):
                try:
                    t = raw.decode(enc, errors='ignore')
                    break
                except Exception:
                    t = ''
            if t.strip():
                results.append(('TEXT', t))
        if ver == 0xF:
            walk(data, body, body + rlen, depth + 1, ctx, results)
        pos = body + rlen

results = []
walk(doc, 0, len(doc), 0, 'root', results)

slides = []
cur = None
in_slide = False
for kind, val in results:
    if kind == 'SLIDE_START':
        cur = []
        in_slide = True
    elif kind == 'SLIDE_END':
        if cur is not None:
            slides.append(cur)
        cur = None
        in_slide = False
    elif kind == 'TEXT' and in_slide:
        cur.append(val)

# 若部分文本未落在slide容器（如全局），记录残余
lines = []
lines.append('SLIDE COUNT: %d' % len(slides))
for i, texts in enumerate(slides, 1):
    lines.append('==== SLIDE %d ====' % i)
    for t in texts:
        t = t.replace('\r', '\n').replace('\x0b', '\n')
        lines.append(t)
    lines.append('')

out = '\n'.join(lines)
open(r'd:\ai\2627vscode\_ppt_extract.txt', 'w', encoding='utf-8').write(out)
print(out[:3000])
print('...TOTAL CHARS:', len(out))
