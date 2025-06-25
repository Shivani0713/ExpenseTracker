from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer
from django.db.models import Sum
from django.db.models.functions import TruncMonth

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Expense.objects.filter(user=user)

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='analytics')
    def analytics(self, request):
        user = request.user
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        expenses = Expense.objects.filter(user=user)
        if start_date and end_date:
            expenses = expenses.filter(date__range=[start_date, end_date])

        total = expenses.aggregate(total=Sum('amount'))['total'] or 0

        category_wise = expenses.values('category').annotate(total=Sum('amount'))

        monthly = expenses.annotate(month=TruncMonth('date')).values('month').annotate(
            total=Sum('amount')
        ).order_by('month')

        return Response({
            "total_expense": total,
            "category_breakdown": category_wise,
            "monthly_trends": monthly
        })
