from rest_framework import serializers
from .models import Project, Student, UserProfile, ApplyProject

class mainappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = {'user', 'p_title', 'p_category', 'diff_level', 'no_of_contrib', 'p_status', 'p_location', 'p_description','p_privacy','skills','post_date'}
