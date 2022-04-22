from rest_framework import serializers
from books.models import Book, Orders
from django.db.models import Count


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'


class BestBookSerializer(serializers.ModelSerializer):
	total_orders = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Book
		fields = ['title', 'author', 'price', 'category', 'date_added', 'is_available', 'total_orders']

	def get_total_orders(self,obj):
		orders = Orders.objects.values_list('book_id').annotate(orders_count=Count('book_id'))
		return orders

class OrderSerializer(serializers.ModelSerializer):
	user_id = serializers.ReadOnlyField(source='user.id')

	class Meta:
		model = Orders
		fields = ['user_id', 'book_id', 'payment_method', 'amount', 'deliver']



