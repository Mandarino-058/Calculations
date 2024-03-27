import string
import time

BAR_LEN = 18
elements = ["=", "\\", "|", "/"]

for i in range(BAR_LEN+1):
    frame = i % len(elements)
    print(f"\r[{elements[frame]*i:=^{BAR_LEN}}]", end='')
    time.sleep(0.1)

text = " HOLAAAA..... "
temp = ""
for ch in text:
    for i in string.printable:
        if i == ch or ch == i:
            time.sleep(0.02)
            print(temp+i)
            temp += ch
            break
        else:
            time.sleep(0.02)
            print(temp+i)