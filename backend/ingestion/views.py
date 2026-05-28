import csv
from io import TextIOWrapper

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmissionRecord, Tenant
from .serializers import EmissionRecordSerializer


@api_view(['GET'])
def emission_records(request):

    records = EmissionRecord.objects.all()

    for record in records:

        if (
            (record.activity_type == "Diesel Fuel" and record.quantity > 10000)
            or
            (record.activity_type == "Electricity" and record.quantity > 50000)
            or
            (record.activity_type == "Flight Travel" and record.quantity > 20000)
        ):

            if record.review_status != 'APPROVED':

                record.review_status = 'FLAGGED'

                record.save()

    serializer = EmissionRecordSerializer(records, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def approve_record(request, record_id):

    try:
        record = EmissionRecord.objects.get(id=record_id)

        record.review_status = 'APPROVED'

        record.locked = True

        record.save()

        return Response({
            "message": "Record approved successfully"
        })

    except EmissionRecord.DoesNotExist:

        return Response({
            "error": "Record not found"
        }, status=404)


@api_view(['POST'])
def upload_csv(request):

    file = request.FILES['file']

    decoded_file = TextIOWrapper(file, encoding='utf-8')

    reader = csv.DictReader(decoded_file)

    tenant = Tenant.objects.first()

    for row in reader:

        EmissionRecord.objects.create(
            tenant=tenant,
            source_type=row['source_type'],
            activity_type=row['activity_type'],
            quantity=float(row['quantity']),
            unit=row['unit'],
            scope=row['scope']
        )

    return Response({
        "message": "CSV uploaded successfully"
    })