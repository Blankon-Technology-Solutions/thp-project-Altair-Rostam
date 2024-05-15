from rest_framework import serializers

from ..models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "content", "status"]

    def create(self, validated_data):
        """
        Create a new Todo instance.
        """
        return Todo.objects.create(content=validated_data["content"])


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "content", "status"]

    def update(self, instance, validated_data):
        """
        Update an existing Todo instance.
        """
        instance.content = validated_data.get("content", instance.content)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance

    def to_representation(self, instance):
        """
        Serialize the Todo instance for update.
        """
        return {"id": instance.id, "content": instance.content, "status": instance.status}
