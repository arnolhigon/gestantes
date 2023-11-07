
from  django.urls import path
from .views import home,formulario, datos,semanal, registros,asociados, mensual, generar_excel_semanal, generar_excel_mensual, eliminar_mensual
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('',home,name='home'),
  path('formulario',formulario,name='formulario'),
  path('semanal',datos,name='datos'),
  path('semanal/generar',generar_excel_semanal, name='generar_excel_semanal'),
  path('registros',registros, name='registros'),
  path('mostrar/<str:tipo_cedula>/<str:numero_cedula>/',asociados, name='mostrar'),
  path('mensual',mensual, name='mensual'),
  path('mensual/mensual', generar_excel_mensual, name='generar_excel_mensual'),
  path('eliminar_mensual/<int:datosgestante_id>/',eliminar_mensual, name='elimina_mensual'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """