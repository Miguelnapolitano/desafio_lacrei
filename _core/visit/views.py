from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
import uuid

from visit.serializers import VisitSerializer
from visit.models import Visit
from professional.models import Professional

class VisitViewSet (ModelViewSet):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()
    
    @action(detail=False, methods=["GET"])
    def get_by_professional(self, request):
        professional_id = request.GET.get("professional")
        if not professional_id:
            raise ParseError(
                detail="Url parameter prof is required."
            )
        
        professional_id = uuid.UUID(professional_id)
        result = Visit.objects.filter(professional_id=professional_id).values("date")
        schedule = list(result)
        
        return Response({"schedule": schedule}, status=HTTP_200_OK)