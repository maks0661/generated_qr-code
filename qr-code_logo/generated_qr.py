import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

data = "https://t.me/zmalex"
logo_path = "my_logo.png"
output_path = "qr_logo.png"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

try:
    logo = Image.open(logo_path)
except FileNotFoundError:
    print(f"ОШИБКА: Файл '{logo_path}' не найден.")
    exit()

logo = logo.convert("RGBA")

qr_width, qr_height = qr_img.size
logo_width, logo_height = logo.size

max_logo_size = qr_height // 3

aspect_ratio = logo_width / logo_height
if aspect_ratio > 1:
    new_width = max_logo_size
    new_height = int(max_logo_size / aspect_ratio)
else:
    new_height = max_logo_size
    new_width = int(max_logo_size * aspect_ratio)

logo = logo.resize((new_width, new_height), Image.LANCZOS)

pos_x = (qr_width - new_width) // 2
pos_y = (qr_height - new_height) // 2

qr_img.paste(logo, (pos_x, pos_y), mask=logo)

qr_img.save(output_path)
print(f"QR-код с логотипом успешно сохранен как {output_path}")