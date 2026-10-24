from django.http import HttpResponse
from saludo.application.services.saludar_service import SaludarService

def saludar_view(request):
    # Adaptador web de entrada para manejar peticiones HTTP
    nombre = request.GET.get('nombre', 'Mundo')
    try:
        servicio = SaludarService()
        mensaje = servicio.ejecutar(nombre)
        return HttpResponse(f"<h1>{mensaje}</h1>", content_type="text/html; charset=utf-8")
    except ValueError as e:
        return HttpResponse(f"<h1>Error de validación: {e}</h1>", status=400)
