from django.core.management.base import BaseCommand
from account.models import Account
from django.core.exceptions import ObjectDoesNotExist
import random

def username(first_name,last_name):
    user_name=str(last_name)+str(first_name)+str(int(random.randint(10,99)))
    return user_name

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',type=str,help='txt file contains user email'
        )
        parser.add_argument(
            'branch_name',type=str,help='Branch Name'
        )
        parser.add_argument(
            'year', type=str, help='Year'
        )

    def handle(self, *args, **options):
        file_name=options['file_name']
        branch_name=options['branch_name']
        year=options['year']

        with open(f'{file_name}.txt') as file:
            for row in file:
                if row!=None:
                    email=row.lower()
                    list_ = email.split(".")
                    first_name = list_[0]
                    last_name = list_[1].split("@")[0]
                    try:
                        Account.objects.get(email=email)
                        print(email,"Is already exists ..!")
                    except ObjectDoesNotExist:
                        Account.objects.create(email=email,
                                               first_name=first_name.title(),
                                               last_name=last_name.title(),
                                               branch=branch_name,year=year,
                                               username=username(first_name,last_name),
                                               password="Vlibrary"+str(first_name)+str(12))
                        print(email,"Imported ..!")

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))