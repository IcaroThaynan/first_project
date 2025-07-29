from django.shortcuts import render  # Importa a função render para renderizar templates
from .models import Produto          # Importa o modelo Produto do arquivo models.py
from django.shortcuts import get_object_or_404  # Importa a função para obter um objeto ou retornar 404 se não encontrado
from django.http import HttpResponse  # Importa HttpResponse para retornar respostas HTTP
from django.template import loader  # Importa o carregador de templates
# Função que trata a view da página inicial
def index(request):
    produtos = Produto.objects.all()  # Busca todos os objetos do modelo Produto no banco de dados
    
    context = {
        'produtos' : produtos                           # Lista de produtos para ser usada no template
    }
    # Renderiza o template 'index.html' passando o contexto acima
    return render(request,'index.html',context)

# Função que trata a view da página de contato
def contato(request):
    # Renderiza o template 'contato.html' sem contexto adicional
    return render(request,'contato.html')
def produto(request, pk):
    #prod = Produto.objects.get(id=pk)  # Busca o produto pelo ID fornecido na URL
    prod = get_object_or_404(Produto, id=pk)  # Se não encontrado, retorna 404
    context = {
        'produto': prod  # Passa o produto encontrado para o contexto
    }
    return render(request, 'produto.html', context)  # Renderiza o template 'produto.html' com o contexto do produto


def error404(request,exception):
    template = loader.get.template('404.html')  # Carrega o template '404.html'
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)  # Retorna a resposta HTTP com o template renderizado e status 404

def error500(request):
    template = loader.get_template('500.html')  # Carrega o template '500.html'
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)  # Retorna a resposta HTTP com o template renderizado e status 500