import qrcode

def qrcreate():
    # import url
    res = str(input())
    img = qrcode.make(res)
    type(img)
    img.save("qr228.png")



qrcreate()