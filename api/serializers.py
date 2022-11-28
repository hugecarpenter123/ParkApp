from rest_framework import serializers
from parking.models import Location, Section, Spot, Motion

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = "__all__"

class SectionSerializer(serializers.ModelSerializer):
    spot_qs = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Section
        fields = [
            "id",
            "name",
            'rows',
            'columns',
            "spot_qs",
        ]

    def get_spot_qs(self, obj):
        spot_set = obj.spot_set.all()
        return SpotSerializer(spot_set, many=True, context=self.context).data

class LocationSerializer(serializers.ModelSerializer):
    section_qs = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Location
        fields = [
            'id',
            'image',
            'section_qs',
        ]

    def get_section_qs(self, obj):
        section_set = obj.section_set.all()
        return SectionSerializer(section_set, many=True, context=self.context).data


class LocationSearchSerializer(serializers.ModelSerializer):

    image_path = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = [
            'id',
            'name',
            'image_path',
        ]

    def get_image_path(self, obj):
        return {f'/static/parking/images/{obj.image}_lookup.png'}

class MotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Motion
        fields = '__all__'

