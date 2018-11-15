from django.db import models


class Prop(models.Model):
    """
    Propery model.
    """
    zillow_id = models.IntegerField(blank=True, null=True)
    area_unit = models.CharField(max_length=20, blank=True, null=True)
    bathrooms = models.FloatField(blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    home_size = models.IntegerField(null=False, default=0)
    home_type = models.CharField(max_length=50, db_index=True, blank=True, null=True)
    last_sold_date = models.DateField(blank=True, null=True)
    last_sold_price = models.FloatField(blank=True, null=True, default=0.0)
    link = models.CharField(max_length=1024, blank=True, null=True)
    price = models.FloatField(blank=True, null=True, default=0.0)
    property_size = models.FloatField(blank=True, null=True, default=0.0)
    rent_price = models.FloatField(blank=True, null=True, default=0.0)
    rentzestimate_amount = models.FloatField(blank=True, null=True, default=0.0)
    rentzestimate_last_updated = models.DateField(blank=True, null=True)
    tax_value = models.FloatField(blank=True, null=True, default=0.0)
    tax_year = models.IntegerField(blank=True, null=True)
    year_built = models.IntegerField(blank=True, null=True)
    zestimate_amount = models.FloatField(blank=True, null=True, default=0.0)
    zestimate_last_updated = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    state = models.CharField(max_length=256, blank=True, null=True)
    zipcode = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'properties'

    def __str__(self):
        return "%s - %s" %(self.id, self.zillow_id)