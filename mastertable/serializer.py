from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# // ----- // ----- // ----- // Notes // ----- // ----- // ----- //
        
# // ----- // ----- // ----- // References // ----- // ----- // ----- //

# puedes relacionar tablas en un serializer
    # Libreria --> from rest_framework import serializer
        # serializers.<FieldName>

    # fields --> specify keyword from model, 1 by 1.
        # fields = ['id', 'alfa2', 'alfa3', 'phone', 'num']

    # read_only_fields --> only allows read, do not edit.
        # read_only_fields = ['alfa2']
    
    # extra_kwargs --> only allows read, do not edit.
    # extra_kwargs = {'password': {'write_only': True}}

    # exclude --> you can exclude arguments use this.
    # exclude = ['users']

# // ----- // ----- // ----- // Bibliography // ----- // ----- // ----- //

# Serializador --> https://www.django-rest-framework.org/api-guide/serializers/
# relations --> https://www.django-rest-framework.org/api-guide/relations/

# ForeignKey

    # utilizando los serializers relacionados.