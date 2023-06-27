from django.db import models
from uuid import uuid4
import os

def file_wrapper(model, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join('pdfs/', filename)

class PdfFile(models.Model):
    pdf = models.FileField(upload_to=file_wrapper)

    
