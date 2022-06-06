from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from resume.models import Resume

class ResumeSerializer(serializers.ModelSerializerr):
    class Meta:
        model = Resume
        fields = "__all__"
    
