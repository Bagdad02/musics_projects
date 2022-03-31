from rest_framework import serializers

from music_db.models import Music, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        model = Music
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        category = CategorySerializer(Category.objects.get(music=instance.id)).data
        print(category)

        print(representation)
        return representation