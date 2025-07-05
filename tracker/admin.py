from django.contrib import admin
from .models import ExpenseIncome
# Register your models here.


@admin.register(ExpenseIncome)
class ExpenseIncomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'amount', 'transaction_type', 'tax_type', 'total', 'created_at']
    list_filter = ['transaction_type', 'tax_type', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    readonly_fields = ['total', 'created_at', 'updated_at']
    
    def total(self, obj):
        return obj.total
    total.short_description = 'Total Amount'
