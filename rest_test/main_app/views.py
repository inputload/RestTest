import time

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

        # Первый вариант

        # res = 0
        # for num in numbers:
        #     res += float(num)

        # Второй вариант

        res = sum([float(num) for num in numbers])

        return Response({'res': res})

    def post(self, request):
        pass


class BankView(APIView):
    def get(self, request):
        currency = {
            "BYN": 2.6,
            "EUR": 1.1,
            "PLN": 4.5,
        }
        cur = request.GET.get("cur")
        count = request.GET.get("count")
        return Response({
            "cur": cur,
            f"USD to {cur}": f"{currency[cur]}",
            "res": f"{currency[cur]*float(count)}",
            "time": f"{time.ctime()}"
        })