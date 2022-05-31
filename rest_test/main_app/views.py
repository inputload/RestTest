from rest_framework.views import APIView
from rest_framework.response import Response


class MainView(APIView):  # класс который будем отображать
    def get(self, request):
        return Response({})  # возврат пустого списка


class SumView(APIView):
    def get(self, request):
        query = request.GET  # Собрали query-параметры в переменную
        numbers = query.get('numbers')  # Записали в переменную query-параметр с ключем numbers
        # До "1,15,7,12"
        numbers = numbers.split(',')  # Разделили строку на разные строки по запятой
        # После ["1","15","7","12"]
        print(numbers)
        return Response({'res': ''})

    def post(self, request):
        pass