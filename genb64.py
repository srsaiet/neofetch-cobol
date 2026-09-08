import base64
raw = open('/home/jihdez/cobol/logo.six', 'rb').read()
b64 = base64.b64encode(raw).decode()
lines = [b64[i:i + 64] for i in range(0, len(b64), 64)]
lines[-1] = lines[-1] + 'A' * (64 - len(lines[-1]))
print('lineas:', len(lines), 'ultima:', len(lines[-1]))
with open('/home/jihdez/cobol/b64data.cpy', 'w') as f:
    for ln in lines:
        f.write('         05 FILLER PIC X(64) VALUE "' + ln + '".\n')
print('cpy escrito')
