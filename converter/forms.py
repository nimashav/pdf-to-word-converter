# Define a form to upload PDF files
# The form allows users to select and submit a PDF file
from django import forms

class UploadPDFForm(forms.Form):
    pdf_file = forms.FileField(label="Select a PDF File")

