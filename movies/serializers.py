from rest_framework import serializers
from .models import Actor, Movie, Review

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview', )

class MovieSerializer(serializers.ModelSerializer):
    class MovieActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    actors = MovieActorSerializer(many=True, read_only=True)
    
    class MovieReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content',)
    review_set = MovieReviewSerializer(many=True, read_only=True)
        
    class Meta:
        model = Movie
        fields = '__all__'

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class ActorMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movies = ActorMovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

class ReviewSerializer(serializers.ModelSerializer):
    class ReviewMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = ReviewMovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)       