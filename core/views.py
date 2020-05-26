from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.forms import  CadastroVeiculoForm
from core.models import Veiculo


@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def veiculosList(request):
    veiculos = Veiculo.objects.all() 
    return render(request, 'listar-veiculos.html', {'veiculos': veiculos} )

@login_required
def cadastrarVeiculo(request):
    if request.method == 'POST':
        form = CadastroVeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form = CadastroVeiculoForm()
        formContextToRender = {'form': form}
        return render(request, 'cadastrar-veiculo.html',formContextToRender )

@login_required
def atualizarVeiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    form = CadastroVeiculoForm(request.POST or None, instance=veiculo)
    if form.is_valid():
        form.save()
        return redirect('listar-veiculos')
    return render(request, 'editar-veiculo.html',{'form': form, 'veiculo': veiculo} )

@login_required
def deletarVeiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar-veiculos')
    return render(request, 'deletar-veiculo.html', {'veiculo': veiculo})