from django.urls import path

from .views import emission_records, approve_record, upload_csv

urlpatterns = [
    path('records/', emission_records),
    path('approve/<int:record_id>/', approve_record),
    path('upload-csv/', upload_csv),
]