from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, FormView
from .models import PdfFile
from django.urls import reverse_lazy
from django import forms, http
from django.http import HttpResponseRedirect
from .scripts import konwerter as kw
from .scripts import scrape_csv as scrape
from django.http import FileResponse
from django.http import JsonResponse
import os
from django.conf import settings

# def index(request):
#     return render(request, 'ipz/index.html')
# class PdfFileModelForm(forms.ModelForm):
#     success_url = reverse_lazy('success')
#     class Meta:
#         model = PdfFile
#         fields = "__all__"
#         widgets = {
#             'pdf': forms.ClearableFileInput()
#         }

class CsvScraperForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())



def download_csv():
    # if created:
    try:
        csv_name = 'Tracab_Data_Concatenated.csv'
        csv_path = os.path.join(settings.BASE_DIR, 'csvs', csv_name)
        response = FileResponse(open(csv_path, 'rb'), as_attachment=True)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(csv_name)
        response['Content-Type'] = "application/csv"
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

# class pdfView(TemplateView):
#     template_name = "ipz/pdf.html"

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['form'] = PdfFileModelForm
#         return context

    # def post(self, request, *args, **kwargs):
    #     form = PdfFileModelForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         pdf = form.cleaned_data['pdf']
    #         PdfFile_obj = PdfFile(pdf=pdf)
    #         PdfFile_obj.save()
    #         response = download_csv(None, PdfFile_obj)
    #         return response
        
class successView(TemplateView):
    template_name ="ipz/success.html"
    
    def dispatch(self, request, *args, **kwargs):
        #response = super().dispatch(request, *args, *kwargs)
        username = self.request.session.get('username')
        password = self.request.session.get('password')
        print(username)
        print(password)
        scrape.scrapeTracab(username, password, settings.BASE_DIR)
        scrape.concatenate_csvs(settings.BASE_DIR)
        scrape.add_transfermarkt(settings.BASE_DIR)
        response = download_csv()
        return response

class generateView(TemplateView):
    template_name = "ipz/generate.html"
    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, *kwargs)
    #     return redirect(reverse_lazy("success"))

class downloadCsvView(FormView):
    template_name = "ipz/dcv.html"
    form_class = CsvScraperForm
    success_url = reverse_lazy('generate')

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        try:
            scrape.check_tracab_user(username, password)
        except:
            return redirect(reverse_lazy("downloadCsvView"))
        print("kupa")
        self.request.session['username'] = username
        self.request.session['password'] = password
        return redirect(self.get_success_url())

# class PdfFileCreateView(CreateView):
#     model = PdfFile
#     fields = "__all__"

#     success_url = reverse_lazy('index')

#     def get_form(self, form_class=None):
#         form = super().get_form(form_class=form_class)
#         form.fields['pdf'].widget = forms.ClearableFileInput()
#         return form
