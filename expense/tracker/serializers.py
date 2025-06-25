from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ExpenseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'category', 'date', 'user']
        read_only_fields = ['user']
