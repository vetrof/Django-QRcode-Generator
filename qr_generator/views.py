from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render
import qrcode
from urllib.parse import urlencode


def generate_qr(request, url):

    # Создаем объект QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Добавляем URL в QRCode
    qr.add_data(url)
    qr.make(fit=True)

    # Создаем изображение QRCode
    img = qr.make_image(fill_color="black", back_color="white")

    # Возвращаем изображение как ответ HTTP
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

