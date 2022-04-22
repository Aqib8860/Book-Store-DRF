from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from django.core.exceptions import ObjectDoesNotExist
from books.serializers import BookSerializer, OrderSerializer, BestBookSerializer
from user.models import User
from books.models import Book, Orders
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


User = get_user_model()


class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['title', 'category']
	#http_method_names = ['get', 'post', 'options', 'head']

	def create(self, request, *args, **kwargs):
		if Book.objects.filter(title=self.request.data['title']).exists():
			return Response({"msg": "This Book is Already exists"}, status=400)
		else:
			serializer = self.get_serializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			self.perform_create(serializer.save())
			return Response({"msg": "Book Add Success"}, status=200)


class BestBookViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BestBookSerializer


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Orders.objects.all()
	serializer_class = OrderSerializer
	filter_backends = [filters.OrderingFilter]
	ordering_fields = ['order_date']
	permission_classes = [permissions.IsAuthenticated]


	def list(self, request, *args, **kwargs):
		try:
			user = User.objects.get(id=request.user.id)
		except ObjectDoesNotExist:
			return Response({"msg": "User Does not exist"}, status=400)

		queryset = self.queryset.filter(user_id=user)
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		try:
			user = User.objects.get(id=request.user.id)
		except ObjectDoesNotExist:
			return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

		try:
			book = Book.objects.get(id=request.data['book_id'])
		except ObjectDoesNotExist:
			return Response({"msg": "Book Does Not Exist"}, status=400)


		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(
            serializer.save(user_id=request.user)
        )
		return Response({"msg": "Order Success"}, status=200)

