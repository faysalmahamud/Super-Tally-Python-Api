# import openpyxl

# wb = openpyxl.Workbook()
# ws = wb.worksheets[0]
# img = openpyxl.drawing.image.Image('img.jpg')
# img.anchor = 'A1'
# ws.add_image(img)
# wb.save('out.xlsx')


import pyqrcode


def generate_qr():
    link_to_post = "https://medium.com/@ngengesenior/qr-codes-generation-with-python-377735be6c5f"
    url = pyqrcode.create(link_to_post)
    url.png('url.png', scale=5)
    print("Printing QR code")
    print(url.terminal())


if __name__ == '__main__':
    generate_qr()