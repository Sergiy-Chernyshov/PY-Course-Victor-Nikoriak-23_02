from pathlib import Path
from uuid import uuid4

from django.conf import settings
from django.shortcuts import render

from .forms import ExcelUploadForm
from .services import process_excel_file, process_internet_orders_file


def save_uploaded_file(uploaded_file):
    upload_dir = Path(settings.MEDIA_ROOT) / "uploads"
    upload_dir.mkdir(parents=True, exist_ok=True)

    suffix = Path(uploaded_file.name).suffix or ".xlsx"
    safe_name = f"upload_{uuid4().hex}{suffix}"
    file_path = upload_dir / safe_name

    with open(file_path, "wb+") as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)

    return file_path


def index(request):
    return render(request, "reports/index.html")


def upload_ppt_file(request):
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.cleaned_data["file"]
            file_path = save_uploaded_file(uploaded_file)

            try:
                result = process_excel_file(file_path)
            except Exception as error:
                return render(request, "reports/upload.html", {
                    "form": form,
                    "error": str(error),
                    "title": "Не проведені ППТ за період",
                    "description": "Завантажте Excel-файл для формування Base, Svod, Excel та PDF звіту.",
                })

            return render(request, "reports/result.html", {
                "result": result,
                "file_name": uploaded_file.name,
            })

    else:
        form = ExcelUploadForm()

    return render(request, "reports/upload.html", {
        "form": form,
        "title": "Не проведені ППТ за період",
        "description": "Завантажте Excel-файл для формування Base, Svod, Excel та PDF звіту.",
    })


def upload_internet_orders_file(request):
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.cleaned_data["file"]
            file_path = save_uploaded_file(uploaded_file)

            try:
                result = process_internet_orders_file(file_path)
            except Exception as error:
                return render(request, "reports/upload.html", {
                    "form": form,
                    "error": str(error),
                    "title": "Ефективність обробки Інтернет замовлень",
                    "description": "Завантажте Excel-файл для аналізу ефективності обробки інтернет-замовлень.",
                })

            return render(request, "reports/internet_orders_result.html", {
                "result": result,
                "file_name": uploaded_file.name,
            })

    else:
        form = ExcelUploadForm()

    return render(request, "reports/upload.html", {
        "form": form,
        "title": "Ефективність обробки Інтернет замовлень",
        "description": "Завантажте Excel-файл для аналізу ефективності обробки інтернет-замовлень.",
    })