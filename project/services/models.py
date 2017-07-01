'''Model definitions for the application'''
from mongoengine import (Document, StringField, EmailField, PolygonField,
                         ListField, FloatField, ReferenceField)


class Provider(Document):
    '''Details of service provider and their areas'''
    name = StringField(max_length=200, required=True)
    email = EmailField(required=True)
    phone = StringField(max_length=15, required=True)
    languages = ListField(StringField(max_length=20, required=True))
    currency = StringField(max_length=10, required=True)
    meta = {'strict': False}


class ServiceArea(Document):
    '''Details of the service area'''
    name = StringField(max_length=100, required=True)
    price = FloatField(required=True)
    area = PolygonField(required=True)

    Provider = ReferenceField(Provider, required=True)
