from rest_framework import serializers, exceptions
from properties.models import Prop


class PropSerializer(serializers.ModelSerializer):
    """
    Basic property serializer.
    Used when retrieving a property object.
    """

    def human_format(self, num):
        """
        Convert float to human readable money format.
        """
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '$%.2f%s' % (num, ['', 'K', 'M', 'B', 'T', 'P'][magnitude])

    price = serializers.SerializerMethodField('_price')    
    def _price(self, obj):
        return self.human_format(obj.price)

    class Meta:
        model = Prop
        fields = ('id', 'area_unit', 'bathrooms', 'bedrooms', 'home_size', 'last_sold_date', 'last_sold_price', 'link', 'price', 'property_size', 'rent_price', 'rentzestimate_amount', 'rentzestimate_last_updated', 'tax_value', 'tax_year', 'year_built', 'zestimate_amount', 'zestimate_last_updated', 'zillow_id', 'address', 'city', 'state', 'zipcode', 'created_at', 'updated_at')

class CreatePropSerializer(serializers.Serializer):
    """
    Create propery serializer.
    Used to validate and create a propery object.
    """
    zillow_id = serializers.FloatField(allow_null=False, write_only=True, required=True)
    area_unit = serializers.CharField(max_length=20, allow_null=True, required=False)
    bathrooms = serializers.FloatField(allow_null=True, required=False)
    bedrooms = serializers.IntegerField(allow_null=True, required=False)
    home_size = serializers.IntegerField(allow_null=False, required=True)
    home_type = serializers.CharField(max_length=50, allow_null=True, required=False)
    last_sold_date = serializers.DateField(allow_null=True, required=False)
    last_sold_price = serializers.FloatField(allow_null=True, required=False)
    link = serializers.CharField(max_length=1024, allow_null=True, required=False)
    price = serializers.FloatField(allow_null=True, required=True)
    property_size = serializers.FloatField(allow_null=True, required=True)
    rent_price = serializers.FloatField(allow_null=True, required=False)
    rentzestimate_amount = serializers.FloatField(allow_null=True, required=False)
    rentzestimate_last_updated = serializers.DateField(allow_null=True, required=False)
    tax_value = serializers.FloatField(allow_null=True, required=True)
    tax_year = serializers.IntegerField(allow_null=True, required=True)
    year_built = serializers.IntegerField(allow_null=True, required=True)
    zestimate_amount = serializers.FloatField(allow_null=True, required=True)
    zestimate_last_updated = serializers.DateField(allow_null=True, required=False)
    address = serializers.CharField(max_length=256, allow_null=True, required=True)
    city = serializers.CharField(max_length=256, allow_null=True, required=True)
    state = serializers.CharField(max_length=256, allow_null=True, required=True)
    zipcode = serializers.CharField(max_length=6, allow_null=True, required=True)

    def create(self, validated_data):
        zillow_id = validated_data.get('zillow_id')
        area_unit = validated_data.get('area_unit')
        bathrooms = validated_data.get('bathrooms')
        bedrooms = validated_data.get('bedrooms')
        home_size = validated_data.get('home_size')
        home_type = validated_data.get('home_type')
        last_sold_date = validated_data.get('last_sold_date')
        last_sold_price = validated_data.get('last_sold_price')
        link = validated_data.get('link')
        price = validated_data.get('price')
        property_size = validated_data.get('property_size')
        rent_price = validated_data.get('rent_price')
        rentzestimate_amount = validated_data.get('rentzestimate_amount')
        rentzestimate_last_updated = validated_data.get('rentzestimate_last_updated')
        tax_value = validated_data.get('tax_value')
        tax_year = validated_data.get('tax_year')
        year_built = validated_data.get('year_built')
        zestimate_amount = validated_data.get('zestimate_amount')
        zestimate_last_updated = validated_data.get('zestimate_last_updated')
        address = validated_data.get('address')
        city = validated_data.get('city')
        state = validated_data.get('state')
        zipcode = validated_data.get('zipcode')

        try:
            # create the prop object.
            prop = Prop.objects.create(
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
        except Exception as e:
           raise e

        return prop