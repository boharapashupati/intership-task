from rest_framework import serializers
from ..models import ExpenseIncome

class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    
    class Meta:
        model = ExpenseIncome
        fields = ['id', 'title', 'description', 'amount', 'transaction_type', 
                 'tax', 'tax_type', 'total', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']