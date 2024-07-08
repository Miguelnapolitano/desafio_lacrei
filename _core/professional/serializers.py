from rest_framework import serializers
from professional.models import Professional, Address

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = "__all__"
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"