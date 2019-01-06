from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apiviewapp.serializers import NameSerializer, EmployeeSerializer
from apiviewapp.models import Employee
# Create your views here.
class TestAPIView(APIView):
	""" This APIView for Http methods operation"""
	def get(self, request):
		colors=['RED', 'YELLOW', 'ORANGE', 'BLUE']
		return Response({'msg':'Welcome to color full year', 'colors':colors})

	def post(self, request):
		serializer =NameSerializer(data = request.data)
		if serializer.is_valid():
			msg = 'Hello {} Whish you happy new year..'.format(serializer.data.get('name'))
			return Response({'msg':msg})
		return Response(serializer.errors, status=400)
	def put(self, request, pk = None):#put, patch and delete id must be required
		return Response({'msg':'Response from put method'})

	def patch(self, request, pk = None):
		return Response({'msg':'Response form patch method'})
	def delete(self, request, pk = None):
		return Response({'msg':'Response form delete method'})
# ViewSets Example
from rest_framework import viewsets
class TestViewSets(viewsets.ViewSet):
	"""This is viewsets test program """
	def List(self, request):
		colors = ['RED', 'BLUE', 'RED', 'ORANGE']
		return Response({'msg':'wish you colorsful day', 'colors':colors,})
	def Create(self, request):
		serializer = NameSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			msg = 'Hello {} your life will be setteled in 2019'.format('name')
			return Response({'msg':msg,})
			print(msg)
		return Response(serializer.errors, status=400)
	def retrive(self, request, pk=None):
		return Response({'msg':'Response form retrive method'})

	def update(self, request, pk=None):
		return Response({'msg':'Response form update method'})

	def partial_update(self, request, pk=None):
		return Response({'msg':'Response form partial_update method'})

	def destroy(self, request, pk=None):
		return Response({'msg': 'Response from destroy method'})


class EmployeeListView(APIView):
	""" Listview APIView demo application"""
	def get(self, request, format=None):
	 	qs = Employee.objects.all()
	 	serializer = EmployeeSerializer(qs, many=True)
	 	return Response(serializer.data)
from rest_framework import generics
class EmployeeAPIView(generics.ListAPIView):
	#queryset = Employee.objects.filter(ename="shankar")
	serializer_class = EmployeeSerializer
	def get_queryset(self):
		qs = Employee.objects.all()
		name = self.request.GET.get('ename')
		if name is not None:
			qs = qs.filter(ename__contains=name)
			return qs

class EmployeeCreateAPIView(generics.CreateAPIView):
	""" To create resource on the Employee table """
	queryset = Employee.objects.all()
	serializer_class =EmployeeSerializer

class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
	""" To Retreive resource on the Employee table """
	queryset = Employee.objects.all()
	serializer_class =EmployeeSerializer
	lookup_field='id'
class EmployeeUpdateAPIView(generics.UpdateAPIView):
	""" To update resource on the Employee table """
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	lookup_field = 'id'
class EmployeeDeleteAPIView(generics.DestroyAPIView):
	""" To Delete resource on the Employee table """
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	lookup_field = 'id'
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
	""" To get all resource and create resource on the Employee table """
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	lookup_field = 'id'
class EmployeeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	""" To Retrive and Update resource on the Employee table """
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	lookup_field = 'id'

class EmployeeRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
	""" To Retrieve and Destroy resource on the Employee table """
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	lookup_field = 'id'
class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	""" To retrieve, update and destroy resource on the Employee table """
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	lookup_field = 'id'
