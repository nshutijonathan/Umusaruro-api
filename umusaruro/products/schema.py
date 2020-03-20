import graphene 
from graphene_django import DjangoObjectType
from .models import Products
class LinkType(DjangoObjectType):
    class Meta:
        model=Products
class Query(graphene.ObjectType):
    products=graphene.List(LinkType)
    
    def resolve_products(self,info,**kwargs):
        return Products.objects.all()
