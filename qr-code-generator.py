import qrcode
import csv
import image

f = open('user-info.csv', 'r')
rdr = csv.reader(f)

for index, line in enumerate(rdr):
    qr = qrcode.QRCode(
        version=12,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=2,
        border=8
    )
    # line[0]: 이름
    # line[1]: 링크
    if index != 0:
        qr.add_data(line[1])
        qr.make()
        img = qr.make_image(fill_color="red", back_color="#23dda0")
        img.save("./qrcode/" + str(index) + line[0] + ".png")
f.close()
