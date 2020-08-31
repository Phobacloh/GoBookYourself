from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly
from users.models import CustomUser
from rest_framework import filters


# Create your views here.

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['category', 'date_created']

    def get_queryset(self):
        
        queryset = Project.objects.all()
        username = self.request.query_params.get('username', None)
        category = self.request.query_params.get('category', None)
        date_created = self.request.query_params.get('date_created', None)
        if username is not None:
            queryset = queryset.filter(owner__username=username)
        if category is not None:
            queryset = queryset.filter(category=category)
        # if date_created is not None:
        #     queryset = queryset.filter(dated_created=date_created)
        return queryset

    def get(self, request):
        projects = self.get_queryset()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class ProjectDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_object(self,pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        self.check_object_permissions(request, project)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project, 
            data=data, 
            partial=True
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def delete (self, request, pk):
        project = self.get_object(pk)
        self.check_object_permissions(request, project)
        project.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        
        queryset = Pledge.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(supporter__username=username)
        return queryset
    
    def get(self, request):
        pledges = self.get_queryset()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class PledgeDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]

    def get_object(self,pk):
        try:
            return Pledge.objects.get(pk=pk)
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        self.check_object_permissions(request, pledge)
        data = request.data
        serializer = PledgeDetailSerializer(
            instance=pledge, 
            data=data, 
            partial=True
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def delete (self, request, pk):
        pledge = self.get_object(pk)
        self.check_object_permissions(request, pledge)
        pledge.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
