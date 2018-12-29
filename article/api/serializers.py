from rest_framework import serializers
from article.models import Article

# Serializers allow complex data such as querysets and
# model instances to be converted to native Python datatypes
# that can then be easily rendered into JSON, XML or other content types.

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'