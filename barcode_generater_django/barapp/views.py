# from typing import Sequence, Optional, Union
# from django.shortcuts import render
from django.http import HttpResponse
import barcode
from barcode.writer import ImageWriter


# Create your views here.
def bar(request):
    # Generate barcode using the provided code
    code = "123456789023"
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(code, writer=ImageWriter())
    barcode_file_path = f"{code}"  # You may need to create the 'media/barcodes' directory
    ean.save(barcode_file_path)
    return HttpResponse("welcome to django")