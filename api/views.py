from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.decorators import action

from api.serializers import ProductSerilizer,CartSerializer
from api.models import Products
# Create your views here.


class ProductsView(ModelViewSet):
    serializer_class=ProductSerilizer
    queryset=Products.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]


    @action(methods=["GET"],detail=False)
    def categories(self,request,*args,**kw):
        #[(electronics),(cloths),(mobiles)...] listil touple ayit   
        qs=Products.objects.values_list("category",flat=True).distinct  # touple alland varan flat  distinct--->duplicate varathai erikan
        return Response(data=qs)

    def list(self, request,*args,**kwargs):
        qs=Products.objects.all()
        if "category" in request.query_params:
            qs=qs.filter(category=request.query_params.get("category"))
        serializer=ProductSerilizer(qs,many=True)
        return Response(data=serializer.data)


#localhost:8000/products/1/addtocart/
    @action(methods=["POST"],detail=True)
    def addto_cart(self,request,*args,**kw):

        product=self.get_object()
        user=request.user()
        serializer=CartSerializer(data=request.data,context={"user":user,"product":product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    