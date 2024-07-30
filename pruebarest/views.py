from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .serializers import PostSerializer, PostModelSerializer
from .models import Post


# Create your views here.
class Post_APIView(APIView):

    # Obtiene todos los posts
    def get(self, request, format=None, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    # Crea un Post
    def post(self, request, format=None):
        serializer = PostModelSerializer(data=request.data, context={"request": self.request})
        if serializer.is_valid():
            exp = serializer.save()
            data = PostSerializer(exp, many=True).data
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Post_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    # Serializa el post obtenido de la funcion anterior
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # Actualiza el post
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Elimina el Post
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
