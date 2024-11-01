from django.http import HttpResponse

def pagina_web_inicial(request):
    codigo_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Unir México</title>
    </head>
    <body>
        <h1>Bienvenidos a la UNIR!!!</h1>
        <h2> Proyecto de Django </h2>
        <img src="/static/unir.png" alt="Logo de la UNIR">
        <p>Proyecto inicial del framework Django. Realizado por los estudiantes Víctor y Citlali</p>
    </body>
    </html>
    """
    return HttpResponse(codigo_html)

