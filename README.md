# Django Gastos Project

Este proyecto es una aplicación básica de Django que permite gestionar y visualizar una lista de gastos. Incluye autenticación de usuarios, un panel de administración, y una interfaz de usuario sencilla para mostrar los datos de los gastos.

## Características

1. **Autenticación de usuarios:** Inicio y cierre de sesión.
2. **Modelo Gasto:** Manejo de información de gastos con los campos:
   - Nombre
   - Monto
   - Fecha
3. **Interfaz de Administración:** Administración de los datos de gastos desde el panel de Django Admin.
4. **Visualización de Datos:** Presenta una tabla con los registros del modelo `Gasto` en la página principal.

## Requisitos Previos

- Python 3.8+
- Django 5.1.5

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Ve al directorio del proyecto:
   ```bash
   cd django-gastos
   ```

3. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```

4. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

6. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```

7. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

8. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

9. Accede a la aplicación en tu navegador:
   - Panel de Administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Página de Inicio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Estructura del Proyecto

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── middleware.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   ├── tests.py
│   ├── views.py
│   ├── static/
│       ├── css/
│       │   ├── home.css
│       │   ├── login.css
```

## Uso

### Panel de Administración
Accede al panel de administración para gestionar los datos de `Gasto`.

### Inicio de Sesión
1. Dirígete a la página de login: [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)
2. Ingresa las credenciales del superusuario o un usuario registrado.

### Visualización de Gastos
1. Tras iniciar sesión, serás redirigido a la página de inicio.
2. La página principal muestra una tabla con los registros del modelo `Gasto`.
3. Usa el botón "Cerrar Sesión" para salir.

## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

## Contribuciones
Si deseas contribuir, envía un pull request o abre un issue con tus sugerencias.
