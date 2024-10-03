# gym_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, PagoForm, GastoForm
from .models import Cliente, Pago, Gasto
from django.utils import timezone

# Vista para agregar un cliente
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'gym_app/agregar_cliente.html', {'form': form})

# Vista para listar clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gym_app/listar_clientes.html', {'clientes': clientes})

# Vista para editar un cliente
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'gym_app/editar_cliente.html', {'form': form})

# Vista para eliminar un cliente
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'gym_app/eliminar_cliente.html', {'cliente': cliente})

# Vista para agregar un pago
def agregar_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = PagoForm()
    return render(request, 'gym_app/agregar_pago.html', {'form': form})

# Vista para agregar un gasto
def agregar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = GastoForm()
    return render(request, 'gym_app/agregar_gasto.html', {'form': form})

# Vista para mostrar balance mensual
def balance_mensual(request):
    hoy = timezone.now()
    pagos = Pago.objects.filter(mes__month=hoy.month, mes__year=hoy.year)
    clientes = Cliente.objects.all()
    clientes_no_pagaron = []

    for cliente in clientes:
        if not pagos.filter(cliente=cliente).exists():
            clientes_no_pagaron.append(cliente)

    total_ingresos = sum([pago.importe for pago in pagos])
    gastos = Gasto.objects.filter(fecha__month=hoy.month, fecha__year=hoy.year)
    total_gastos = sum([gasto.monto for gasto in gastos])
    balance = total_ingresos - total_gastos

    return render(request, 'gym_app/balance_mensual.html', {
        'total_ingresos': total_ingresos,
        'total_gastos': total_gastos,
        'balance': balance,
        'clientes_no_pagaron': clientes_no_pagaron
    })
