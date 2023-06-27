from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PdfFile
from .scripts import konwerter as kw
from django.http import FileResponse
from django.http import JsonResponse
import os
from django.conf import settings
#Plik aktualnie nieużywany

#@receiver(post_save, sender=PdfFile)
def download_csv(sender, instance, created, **kwargs):
    if created:
        try:
            print(settings.BASE_DIR)
            path_norm = os.path.normpath(instance.pdf.url[1:])
            pdf_path = os.path.join(settings.BASE_DIR, path_norm)
            print("Pdf: ", pdf_path)
            csv_path = 'csvs\\' + path_norm.split("\\")[-1].split('.')[0]
            csv_path = os.path.join(settings.BASE_DIR, csv_path)
            print("csv_path: ", csv_path)
            csv_file_path = kw.convert(pdf_path, csv_path)
            print("file_path: ", csv_file_path)
            csv_file_name = csv_file_path.split("\\")[-1]
            print("file_name: ", csv_file_name)
            response = FileResponse(open(csv_file_path, 'rb'), as_attachment=True)
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(csv_file_name)
            response['Content-Type'] = "application/octet-stream"
            return response
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)