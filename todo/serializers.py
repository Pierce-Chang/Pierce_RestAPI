from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        # user = request.user
        fields = ['id', 'first_name', 'last_name', 'username', 'email'] # , 'user'
        
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        # user = request.user
        fields = ['id', 'title', 'description', 'created_at', 'user', 'time_passed'] # , 'user'