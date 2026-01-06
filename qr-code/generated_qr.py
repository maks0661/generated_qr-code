import qrcode
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(
    version=None, # размер qr-кода
    error_correction=ERROR_CORRECT_H, # уровень коррекции ошибок
    box_size=10, # размер одного квадратика
    border=4, # ширина белой равки вокруг кода
)

# данные
data = "https://www.google.com"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "darkblue", back_color = "white")

img.save("custom_qr.png")

print("Кастомный QR-код сохранен как custom_qr.png")