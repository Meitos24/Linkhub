# Linktree API - Django REST Framework

Este proyecto es una API REST básica desarrollada con Django y Django REST Framework (DRF).
La finalidad es gestionar usuarios para un sistema tipo Linktree mejorado, donde más adelante se podrán asociar enlaces personalizados.

## 🚀 Tecnologías utilizadas
- **Python**: 3.13.
- **Django**: 5.
- **Django REST Framework**.

## 🔌 Endpoints disponibles

Base Url: `http://127.0.0.1:8000/api/`

1. **Listar Usuarios GET** `/usuarios/`
2. **Crear Usuarios POST** `/usuarios/`
3. **Obtener usuario por ID GET** `/usuarios/{id}/`
4. **Actualizar usuario PUT/PATCH** `/usuarios/{id}/`
5. **Eliminar usuario DELETE** `/usuarios/{id}/`

## 💻 Ejecutar el proyecto
   
1. Clonar el repositorio
```bash
  git clone https://github.com/tuusuario/linktree-backend.git
  cd backend
```

2. Crear y activar entorno virtual
```bash
  python -m venv myenv
  source myenv\bin\activate # Linux/Mac
  myenv\Scripts\activate # Windows
```

3. Instalar dependencias
```bash
  pip install djangorestframework
```

4. Aplicar migraciones
```bash
  python manage.py makemigrations
  python manage.py migrate
```

5. Ejecutar servidor
```bash
  python manage.py runserver
```

