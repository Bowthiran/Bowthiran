from django.core.management.base import BaseCommand
from customer_service_app.models import ServiceRequest
from datetime import datetime

class Command(BaseCommand):
    help = 'Resolve a service request'

    def handle(self, *args, **kwargs):
        request_id = input("Enter request ID to resolve: ")
        try:
            service_request = ServiceRequest.objects.get(id=request_id)
            service_request.status = 'Resolved'
            service_request.resolved_at = datetime.now().replace(microsecond=0)
            service_request.save()
            self.stdout.write(f"Service request ID {request_id} marked as resolved.")
        except ServiceRequest.DoesNotExist:
            self.stdout.write("Service request not found.")