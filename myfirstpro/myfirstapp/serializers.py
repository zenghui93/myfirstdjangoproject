from rest_framework import serializers
from .models import List, Record, Category


class RecordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    picture = serializers.ImageField()
    submission_date = serializers.DateTimeField()

    class Meta:
        model = Record
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    category_set = RecordSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'category_set')



class ListSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    list_sets = RecordSerializer(read_only=True, many=True)
    class Meta:
        model = List
        fields = ('id', 'name', 'list_sets')















