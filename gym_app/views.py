# gym_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Pago, Gasto
from .forms import ClienteForm, PagoForm, GastoForm
from django.db.models import Sum
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

# Vista para listar los clientes
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
    return render(request, 'gym_app/editar_cliente.html', {'form': form, 'cliente': cliente})

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
            pago = form.save()
            # Actualizar el estado del cliente a 'pagado' si el pago es mayor que 0
            if pago.importe > 0:
                cliente = pago.cliente
                cliente.pagado = True
                cliente.save()
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

# Vista para mostrar el balance mensual
def balance_mensual(request):
    fecha_actual = timezone.now()
    pagos = Pago.objects.filter(fecha__year=fecha_actual.year, fecha__month=fecha_actual.month).aggregate(total_pagos=Sum('importe'))
    gastos = Gasto.objects.filter(fecha__year=fecha_actual.year, fecha__month=fecha_actual.month).aggregate(total_gastos=Sum('monto'))

    total_pagos = pagos['total_pagos'] if pagos['total_pagos'] else 0
    total_gastos = gastos['total_gastos'] if gastos['total_gastos'] else 0
    balance = total_pagos - total_gastos

    return render(request, 'gym_app/balance_mensual.html', {
        'total_pagos': total_pagos,
        'total_gastos': total_gastos,
        'balance': balance
    })