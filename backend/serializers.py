from rest_framework import serializers
from .models import Member, Stores, Inquiry

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = '__all__'

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'