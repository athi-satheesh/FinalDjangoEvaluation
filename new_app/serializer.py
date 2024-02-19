from rest_framework import serializers

from new_app.models import Student


#Creating serializer for listing out student
class Student_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'dob', 'contact_number',)

