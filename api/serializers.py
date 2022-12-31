from rest_framework import serializers
from api.models import Products,Carts

class ProductSerilizer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)


    class Meta:
        model=Products
        fields="__all__"


class CartSerializer(serializers.ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields=["products",'user','date']

    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(**validated_data,user=user,product=product) 