#Crear formularios basados en los modelos
from django import forms
from ventas.models import Cliente, Producto


class AddClientesForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo','nombre', 'telefono')
        labels = {
            'codigo': 'Código cliente',
            'nombre': 'Nombre cliente',
            'telefono': 'Telefono: (Contacto):'
        }

class EditClientesForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo','nombre', 'telefono')
        labels = {
            'codigo': 'Código cliente',
            'nombre': 'Nombre cliente',
            'telefono': 'Telefono: (Contacto):'
        }
        widgets = {
              #forms.TextInput(attrs={'tyoe': 'text', 'id': 'codigo_editar'})
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
        }

        ###################################
class AddProductosForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo','descripcion', 'imagen', 'costo', 'precio', 'cantidad')
        labels = {
            'codigo': 'Código producto',
            'descripcion': 'Descripcion producto',
            'imagen': 'Imagen:',
            'costo': 'Costo:',
            'precio': 'Precio:',
            'cantidad': 'Cantidad:',
        }

class EditProductosForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo','descripcion', 'imagen', 'costo', 'precio', 'cantidad')
        labels = {
            'codigo': 'Código producto',
            'descripcion': 'Descripcion producto',
            'imagen': 'Imagen:',
            'costo': 'Costo:',
            'precio': 'Precio:',
            'cantidad': 'Cantidad:',
        }
        widgets = {
              #forms.TextInput(attrs={'tyoe': 'text', 'id': 'codigo_editar'})
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'descripcion': forms.TextInput(attrs={'id': 'descripcion_editar'}),
            'costo': forms.TextInput(attrs={'id': 'costo_editar'}),
            'precio': forms.TextInput(attrs={'id': 'precio_editar'}),
            'cantidad': forms.TextInput(attrs={'id': 'cantidad_editar'}),
        }




"""""

class ClienteForms(forms.ModelForm):
    class Meta:
        #imagen = forms.ImageField()
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono', 'imagen')
        labels = {
            'codigo': 'Código',
            'telefono': 'Telefono',
            'imagen': 'Imagen',
            'nombre':'Descripcion'
        }

class EditarClienteForms(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono', 'imagen')
        labels = {
            'codigo': 'Código',
            'telefono': 'Telefono',
            'imagen': 'Imagen',
            'nombre':'Descripcion'
        }

        widgets = {
            'codigo': forms.TextInput(attrs=('type': 'text', 'id': 'codigo_editar')),
            'nombre': forms.TextInput(attrs=('id': 'nombre_editar')),
            'telefono': forms.TextInput(attrs=('id': 'telefono_editar'))
            
        }

"""""