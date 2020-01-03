from django.conf import settings
from django.core.management.base import BaseCommand
from loan_app.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        if CustomUser.objects.count() == 0:
            mtechuser = CustomUser.objects.create(
                username='mtech',
                email='mtech@machineertech.com',
                is_staff=True,
                is_superuser=True,
                permissions='{"loan":{"create":true,"retrieve":true,"update":true,"delete":true},"loantype":{"create":true,"retrieve":true,"update":true,"delete":true},"payment":{"create":true,"retrieve":true,"update":true,"delete":true},"user":{"create":true,"retrieve":true,"update":true,"delete":true}}',
            )

            mtechuser.set_password("machineertech")

            mtechuser.save()

            clientuser = CustomUser.objects.create(
                username='noc',
                email='noc@noc.com',
                is_staff=True,
                is_superuser=True,
                permissions='{"loan":{"create":true,"retrieve":true,"update":true,"delete":true},"loantype":{"create":true,"retrieve":true,"update":true,"delete":true},"payment":{"create":true,"retrieve":true,"update":true,"delete":true},"user":{"create":true,"retrieve":true,"update":true,"delete":true}}',
            )

            clientuser.set_password('nocpassword')

            clientuser.save()
