# tracker/views.py

from rest_framework import viewsets, permissions
from ..models import ExpenseIncome
from ..serializers.tracker_serializers import ExpenseIncomeSerializer

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.user == request.user

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
