from django.core.management.base import BaseCommand
from customer_service_app.models import ServiceRequest

class Command(BaseCommand):
    help = 'Track service requests'

    def handle(self, *args, **kwargs):
        requests = ServiceRequest.objects.all()
        if requests.exists():
            for request in requests:
                self.stdout.write(
                    f"Report ID: {request.id},\nReport Type: {request.request_type},\n"
                    f"Status: {request.status},\nCreated At: {request.created_at},\n"
                    f"Resolved At: {request.resolved_at or 'Not Resolved'}"
                )
        else:
            self.stdout.write("No service requests found.")
