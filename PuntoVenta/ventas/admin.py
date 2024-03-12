from django.contrib import admin
from ventas.models import Cliente,Producto,Empresa
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'codigo')
    search_fields = ['nombre'] #envio una lista
    readonly_fields = ('created', 'updated') #no editar manual
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente,ClienteAdmin) #paso modelo
#llamo los datos que necesito del modelo para crear
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'cantidad', 'costo')
    search_fields = ['descripcion'] #envio una lista
    readonly_fields = ('created', 'updated') #no editar manual
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto,ProductoAdmin) #paso modelo



class EmpresaAdmin(admin.ModelAdmin):#campbiar por proveedor
    list_display = ('nombre', 'domicilio', 'telefono')
    search_fields = [] #envio una lista
    readonly_fields = ('created', 'updated') #no editar manual
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Empresa,EmpresaAdmin) #paso modelo