from django.core.management.base import BaseCommand
from customer_service_app.models import ServiceRequest

class Command(BaseCommand):
    help = 'Submit a new service request'

    def handle(self,*args, **kwargs):
        request_type = input("Enter Report Type: ")
        description = input("Enter Description: ")
        
        service_request = ServiceRequest.objects.create(
            request_type=request_type,
            description=description
        )
        self.stdout.write(f"Service request created with ID {service_request.id}.")
