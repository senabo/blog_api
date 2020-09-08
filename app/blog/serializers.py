from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    comment_set = CommentSerializer(many=True, required=False, read_only=True)
    count_votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "url",
            "author",
            "created",
            "count_votes",
            "comment_set",
        )
