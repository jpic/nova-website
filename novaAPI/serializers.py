from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User

default_fields = ('id', 'title', 'date', 'picto', 'content')
blog_post_fields = ('id', 'title', 'author', 'date', 'picto', 'content')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class BusinessPropositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProposition
        fields = default_fields

class BlogPostSerializer(serializers.ModelSerializer):
    child = User.objects.all()
    author = UserSerializer(child)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'author', 'date', 'picto', 'content')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'abstract', 'date', 'picto', 'content', 'bg_image', 'description')

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'title', 'date', 'picto', 'pdf', 'content')

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = default_fields

class CrossIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CrossIndustry
        fields = default_fields

class LearningLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningLab
        fields = default_fields

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = default_fields

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = default_fields

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = default_fields

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = default_fields

class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = default_fields

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = default_fields

class DeploySerializer(serializers.ModelSerializer):
    class Meta:
        model = Deploy
        fields = default_fields

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = default_fields

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = default_fields

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = default_fields
