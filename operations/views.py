import datetime
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response
from stores.models import Store
from operations.models import Operation
from operations.serializer import OperationSerializer, OperationStoreSerializer
from .form import FileForm


def upload(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        file = request.FILES["file"]
        operations = file.readlines()

        for operation in operations:
            parse(operation=operation)
    else:
        form = FileForm()

    return render(request, "./index.html", {"form": form})


def parse(operation):
    parsed = operation.decode()

    tipo = parsed[:1]
    data = datetime.date.fromisoformat(f"{parsed[1:5]}-{parsed[5:7]}-{parsed[7:9]}")
    valor = int(int(parsed[9:19]) / 100)
    cpf = parsed[19:30]
    cartao = parsed[30:42]
    hora = datetime.time.fromisoformat(
        f"{parsed[42:44]}:{parsed[44:46]}:{parsed[46:48]}"
    )

    dono = parsed[48:62]
    nome = parsed[62:80]

    store, _ = Store.objects.get_or_create(nome=nome, dono=dono)

    serializer = OperationSerializer(
        data={
            "tipo": tipo,
            "data": data,
            "valor": valor,
            "cpf": cpf,
            "cartao": cartao,
            "hora": hora,
            "store": store.id,
        }
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()


class OperationView(APIView):
    def get(self, request, store_id):
        store = get_object_or_404(Store, id=store_id)

        operations = Operation.objects.filter(store_id=store.id)
        serializer = OperationStoreSerializer(operations, many=True)

        total = 0
        tipos = ["2", "3", "9"]
        for operation in operations:
            if operation.tipo in tipos:
                total = total - operation.valor

            else:
                total = total + operation.valor

        return Response(
            [
                {"total": total},
                *serializer.data,
            ]
        )
