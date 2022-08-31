import qrcode
import csv
import image

f = open('user-info.csv', 'r')
rdr = csv.reader(f)

for index, line in enumerate(rdr):
    # line[0]: 이름
    # line[1]: 링크
    if index != 0:
        qr = qrcode.make(line[1])
        qr.save("./qrcode/" + str(index) + line[0] + ".png")
f.close()
