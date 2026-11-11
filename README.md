# CLI-To-Do-List-in-Python-KAESZAR-cesar-soengas

## Descripcion

Herramienta ligera de terminal desarrollada en Python para que el equipo de operaciones de una empresa de logistica pueda registrar y consultar tareas pendientes, y dar seguimiento a los pendientes entre turnos.

## Funcionalidades

- Agregar una tarea nueva indicando su titulo.
- Mostrar todas las tareas pendientes con su posicion numerica.
- Eliminar una tarea indicando su posicion en la lista.
- Guardar las tareas en el archivo local `todos.csv`.
- Cargar las tareas guardadas en `todos.csv` para continuar el trabajo.

En esta version no se editan tareas. Para corregir una, se elimina y se crea de nuevo.

Consulta [CONTEXT.md](CONTEXT.md) para conocer el contexto y el alcance del proyecto.

## Ejecucion

Instala Rich con:

```bash
pip install -r requirements.txt
```

Inicia la aplicación desde la raíz del proyecto con:

```bash
python main.py
```

La lista se carga al iniciar y se guarda automáticamente al agregar o eliminar tareas. También puedes guardarla desde el menú. El archivo `todos.csv` se crea en el directorio desde el que ejecutas la aplicación.

Consulta [spec.md](spec.md) para ver los criterios de aceptación de esta versión.
