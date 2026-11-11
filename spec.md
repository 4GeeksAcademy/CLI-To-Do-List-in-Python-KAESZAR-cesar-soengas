# Especificación: CLI de tareas

## Objetivo

Permitir que coordinadores de operaciones administren tareas pendientes desde una terminal y conserven la lista entre sesiones.

## Funcionalidad

- `add_one_task(title)`: agregar un título no vacío a la lista en memoria.
- `print_list()`: mostrar tareas con posiciones numéricas desde 1; comunicar claramente cuando la lista está vacía.
- `delete_task(number_to_delete)`: eliminar por posición 1-based y manejar entradas no numéricas o fuera de rango sin cerrar la aplicación.
- `save_todos()`: persistir cada tarea como un registro CSV en `todos.csv`.
- `load_todos()`: reemplazar la lista en memoria con los registros CSV; un archivo inexistente representa una lista vacía.
- Menú interactivo que permite repetir operaciones en una misma ejecución sin límite fijo de tareas.

## Interfaz

Usar Rich para presentar el menú, los mensajes y la lista en una interfaz clara. Ofrecer opciones para agregar, listar, eliminar, guardar y salir. Al iniciar se cargan las tareas; agregar y eliminar guardan automáticamente. La salida guarda los cambios.

## Criterios de aceptación

1. Se pueden agregar varias tareas consecutivamente en una sola ejecución.
2. El listado muestra cada tarea con una posición clara y comenzando en 1.
3. La eliminación remueve solo la tarea elegida por posición y no falla ante una posición inválida.
4. Guardar y volver a cargar conserva títulos y orden, incluidos títulos con comas o comillas.
5. El usuario puede navegar por el menú hasta elegir salir; salir guarda antes de terminar.
