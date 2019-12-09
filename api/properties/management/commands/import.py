from django.core.management.base import BaseCommand, CommandError
from properties.models import Prop
import csv
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import the properties from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="csv file path")

    def safe_cast(self, val, to_type, default=None):
        try:
            return to_type(val)
        except (ValueError, TypeError):
            return default
    
    def parse_price(self, value):
        value = value.replace('$', '')
        if 'M' in value:
            value = value.replace('M', '')
            value = self.safe_cast(value, float, 0.0) * 1000000
        
        elif 'K' in value:
            value = value.replace('K', '')
            value = self.safe_cast(value, float, 0.0) * 1000

        return value

    def handle(self, *args, **options):
        Prop.objects.all().delete()
        try:
            props_to_insert = []
            with open(options['path'], 'r') as inputFile:
                reader = csv.DictReader(inputFile)
                for prop in reader:
                    zillow_id = self.safe_cast(prop['zillow_id'], int, 0)
                    area_unit = prop['area_unit']
                    bathrooms = self.safe_cast(prop['bathrooms'], float, 0.0)
                    bedrooms = self.safe_cast(prop['bedrooms'], int, 0)
                    home_size = self.safe_cast(prop['home_size'], int, 0)
                    home_type = prop['home_type']
                    last_sold_date = parse_date(prop['last_sold_date'])
                    last_sold_price = self.safe_cast(prop['last_sold_price'], float, 0.0)
                    link = prop['link']
                    price = self.parse_price(prop['price'])
                    property_size = self.safe_cast(prop['property_size'], float, 0.0)
                    rent_price = self.safe_cast(prop['rent_price'], float, 0.0)
                    rentzestimate_amount = self.safe_cast(prop['rentzestimate_amount'], float, 0.0)
                    rentzestimate_last_updated = parse_date(prop['rentzestimate_last_updated'])
                    tax_value = self.safe_cast(prop['tax_value'], float, 0.0)
                    tax_year = self.safe_cast(prop['tax_year'], int, 2018)
                    year_built = self.safe_cast(prop['year_built'], int, 1990)
                    zestimate_amount = self.safe_cast(prop['zestimate_amount'], float, 0.0)
                    zestimate_last_updated = parse_date(prop['zestimate_last_updated'])
                    address = prop['address']
                    city = prop['city']
                    state = prop['state']
                    zipcode = prop['zipcode']
                    
                    self.stdout.write('Importing %s' %(zillow_id))

                    prop = Prop(
                        area_unit=area_unit,
                        bathrooms=bathrooms,
                        bedrooms=bedrooms,
                        home_size=home_size,
                        home_type=home_type,
                        last_sold_date=last_sold_date,
                        last_sold_price=last_sold_price,
                        link=link,
                        price=price,
                        property_size=property_size,
                        rent_price=rent_price,
                        rentzestimate_amount=rentzestimate_amount,
                        rentzestimate_last_updated=rentzestimate_last_updated,
                        tax_value=tax_value,
                        tax_year=tax_year,
                        year_built=year_built,
                        zestimate_amount=zestimate_amount,
                        zestimate_last_updated=zestimate_last_updated,
                        zillow_id=zillow_id,
                        address=address,
                        city=city,
                        state=state,
                        zipcode=zipcode,
                    )
                    
                    # Added to the array for bulk creation.
                    props_to_insert.append(prop)

                # Injest all the records in one DB commit.
                Prop.objects.bulk_create(props_to_insert)


        except IOError as error:
            self.stdout.write(self.style.ERROR(error))
            self.stdout.write(self.style.ERROR('Failed to import "%s"' % options['path']))

        self.stdout.write(self.style.SUCCESS('Successfully imported "%s"' % options['path']))