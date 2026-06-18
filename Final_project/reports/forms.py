from django import forms


class ExcelUploadForm(forms.Form):
    file = forms.FileField(label="Excel-файл")

    def clean_file(self):
        file = self.cleaned_data["file"]

        if not file.name.endswith((".xlsx", ".xls")):
            raise forms.ValidationError("Завантажте файл Excel у форматі .xlsx або .xls")

        return file