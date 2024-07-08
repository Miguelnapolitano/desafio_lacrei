from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
import rest_framework.status as status
from professional.models import Professional, Address
from professional.serializers import ProfessionalSerializer, AddressSerializer


class ProfessionalViewSet (ModelViewSet):
    serializer_class = ProfessionalSerializer
    queryset = Professional.objects.all()
    
    def create(self, request, *args, **kwargs):
        
        address = request.data.pop("address")
        
        prof_serializer = ProfessionalSerializer(data=request.data)
        
        if prof_serializer.is_valid():
            print('$$$$$$$$$$$$$$$$$$$')
            new_prof = prof_serializer.save()
            address["user_id"] = new_prof
            address_serializer = AddressSerializer(data=address)
            
            if address_serializer.is_valid():
                new_address = address_serializer.save()            
                                    
                inserted_prof = ProfessionalSerializer(new_prof)
                inserted_prof.data["address"] = new_address
                
                return Response(new_prof.data, status=status.HTTP_201_CREATED)
            # else:
            #     return Response({"detail": "Error during insert address at database."}, status=status.HTTP_404_)