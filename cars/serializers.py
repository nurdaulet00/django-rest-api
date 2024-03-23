import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Cars

#class CarsModel:
#    def __init__(self, title, content):
#       self.title = title
#        self.content = content

class CarsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) # Скрытое поле где прописывается сразу какой пользователь, это для того чтобы когда пользователь добавляет свою запись он не выбирал имя

    class Meta:
        model = Cars
        fields = "__all__"




#def encode():
#    model = CarsModel('Mercedes', 'Content: 2024-22')
#    model_sr = CarsSerializer(model)
#    print(model_sr.data, type(model_sr.data), sep='\n')
#    json = JSONRenderer().render(model_sr.data)
#    print(json)


#def decode():
#    stream =  io.BytesIO (b'{"title":"Mercedes","content":"Content: 2024-22"}')
#    data = JSONParser().parse(stream)
#    serializer = CarsSerializer(data=data)
#    serializer.is_valid()
#    print(serializer.validated_data)
