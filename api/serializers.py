from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    label = serializers.CharField(max_length=30)
    author = serializers.CharField(max_length=30)
    year = serializers.IntegerField()
    genre = serializers.CharField(max_length=30)