SRC = '/home/srsaiet/cobol/neofetch.cob'
CPY = '/home/srsaiet/cobol/b64data.cpy'
with open(SRC, encoding='utf-8') as f:
    src = f.read()
with open(CPY, encoding='utf-8') as f:
    cpy = f.read()
old = '           COPY b64data.\n'
assert src.count(old) == 1, 'COPY no encontrado una vez'
src = src.replace(old, cpy)
with open(SRC, 'w', encoding='utf-8', newline='') as f:
    f.write(src)
print('inline ok')
