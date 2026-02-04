from rest_framework import serializers

from .models import Child

class ChildSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(
        source='get_status_display',
        read_only=True
    )

    class Meta:
        model=Child
        fields = ['id', 'full_name', 'cyberons', 'status', 'status_display']