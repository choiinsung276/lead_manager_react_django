from leads.models import  Lead
from rest_framework import viewsets, permissions
from .serializers import  LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.leads.all()
    # lead를 create할때 우리가 lead owner를 저장하는것을 허락한다.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
