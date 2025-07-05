
    
from rest_framework import serializers
from ..models import ExpenseIncome

class ExpenseIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseIncome
        fields = '__all__'