"""
Django commands to wait for database to be available.
"""

import time
from typing import Any, Optional
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django command to wait for database
    """
    def handle(self, *args, **options):
        """Entry point for Command
        """
        self.stdout.write("Waiting for the database to spin up.......")
        db_up=False
        while db_up is False:
            try:
                self.check(database=['default'])
                db_up=True
            except(Psycopg2OpError,OperationalError):
                self.stdout.write('Database Unavailable, waiting 1 second.....')
                
        
