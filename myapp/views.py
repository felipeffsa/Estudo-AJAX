from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def home(request):
    return render(request,'home.html')




def processamento(request):
    if request.method == 'GET':
        dado = request.GET.get('dado', '')  # Obtém o dado enviado na requisição POST
        algo = request.GET.get('algo', '')
        id = request.GET.get('id','')
        print(dado)
        print(algo)
        print(id)
        
        # Faça a manipulação desejada com o dado recebido
        # Por exemplo, você pode salvar no banco de dados, processar, etc.
        
        # Neste exemplo, apenas retornamos uma mensagem de confirmação
        return JsonResponse({'status': 'sucesso', 'mensagem': 'Dado recebido: ' + dado})

