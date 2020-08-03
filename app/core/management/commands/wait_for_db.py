import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """pause excution until db is ready"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for db ...')
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections['default']
            except OperationalError:
                self.stdout.write('retry in 1 sec ...')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('DB AVAILABLE'))