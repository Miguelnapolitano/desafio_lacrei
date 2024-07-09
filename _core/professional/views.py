from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
import rest_framework.status as status
from professional.models import Professional, Address
from professional.serializers import ProfessionalSerializer, AddressSerializer


class ProfessionalViewSet (ModelViewSet):
    serializer_class = ProfessionalSerializer
    queryset = Professional.objects.all()
        
    def create(self, request, *args, **kwargs):
        
        address_data = request.data.pop("address", None)
        
        prof_serializer = ProfessionalSerializer(data=request.data)
        prof_serializer.is_valid(raise_exception=True)
        new_prof = prof_serializer.save()
        
        if address_data:
            address_data["user"] = new_prof.id
            address_serializer = AddressSerializer(data=address_data)
            address_serializer.is_valid(raise_exception=True)
            new_address = address_serializer.save()
        else:
            new_address = None
            
        inserted_prof = ProfessionalSerializer(new_prof)
        response_data = inserted_prof.data
        if new_address:
            response_data["address"] = AddressSerializer(new_address).data

        return Response(response_data, status=status.HTTP_201_CREATED)
    
    def partial_update(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        instance = self.get_object()
        address_data = request.data.pop("address", None)
        
        prof_serializer = self.get_serializer(instance, data=request.data, partial=True)
        prof_serializer.is_valid(raise_exception=True)
        self.perform_update(prof_serializer)

        if address_data:
            address_instance = Address.objects.filter(user_id=user_id).first()
            if address_instance:
                address_serializer = AddressSerializer(address_instance, data=address_data, partial=True)
                address_serializer.is_valid(raise_exception=True)
                address_serializer.save()
            else:
                address_data["user"] = user_id
                address_serializer = AddressSerializer(data=address_data)
                address_serializer.is_valid(raise_exception=True)
                address_serializer.save()

        response_data = prof_serializer.data
        if address_data:
            response_data["address"] = AddressSerializer(Address.objects.filter(user_id=user_id).first()).data
        
        return Response(response_data, status=status.HTTP_200_OK)