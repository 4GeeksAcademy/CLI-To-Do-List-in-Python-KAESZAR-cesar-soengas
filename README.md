# CLI-To-Do-List-in-Python-KAESZAR-cesar-soengas

## Descripción

Herramienta ligera de terminal desarrollada en Python para que el equipo de operaciones de una empresa de logística pueda registrar y consultar tareas pendientes, y dar seguimiento a los pendientes entre turnos. La interfaz usa [Rich](https://github.com/Textualize/rich) para mostrar el menú, los mensajes y la lista de tareas.

## Funcionalidades y funcionamiento

Al iniciar, la aplicación carga las tareas guardadas en `todos.csv` y presenta un menú interactivo:

1. **Agregar tarea:** solicita un título y lo añade a la lista en memoria. Los títulos vacíos no se aceptan.
2. **Mostrar tareas:** presenta todas las tareas en una tabla numerada desde `1`.
3. **Eliminar tarea:** muestra la lista y solicita el número de la tarea. Las posiciones que no existan o no sean numéricas se rechazan sin cerrar la aplicación.
4. **Guardar tareas:** guarda la lista actual en `todos.csv`.
5. **Salir:** guarda los cambios y termina la aplicación.

Se pueden agregar tantas tareas como se necesiten en una misma ejecución. Al agregar o eliminar una tarea, la aplicación también guarda automáticamente. Para modificar un título en esta versión, elimina la tarea y créala nuevamente.

El archivo `todos.csv` almacena una tarea por registro CSV, conservando correctamente títulos que incluyan comas o comillas. Si el archivo todavía no existe, la aplicación comienza con una lista vacía y lo crea al guardar.

En esta version no se editan tareas. Para corregir una, se elimina y se crea de nuevo.

Consulta [CONTEXT.md](CONTEXT.md) para conocer el contexto y el alcance del proyecto.

## Instalación y ejecución

Instala Rich con:

```bash
pip install -r requirements.txt
```

Inicia la aplicación desde la raíz del proyecto con:

```bash
python main.py
```

Ejecuta el comando desde la raíz del proyecto. El archivo `todos.csv` se crea en el directorio de trabajo actual desde el que inicias la aplicación.

## Estructura del proyecto

```text
.
├── main.py          # Funciones de tareas y menú interactivo con Rich
├── requirements.txt # Dependencias de Python
├── todos.csv        # Datos locales; se crea al guardar tareas
├── README.md        # Descripción, uso y estructura del proyecto
├── CONTEXT.md       # Contexto del problema y objetivo
├── spec.md          # Alcance y criterios de aceptación
└── rules-workflow.md # Reglas de trabajo del repositorio
```

### Organización de `main.py`

- `add_one_task(title)`: añade una tarea no vacía y persiste la lista.
- `print_list()`: muestra la tabla numerada o informa que no hay tareas.
- `delete_task(number_to_delete)`: elimina una tarea por su posición, comenzando en `1`.
- `save_todos()`: escribe las tareas en formato CSV.
- `load_todos()`: carga el archivo CSV a la lista en memoria.
- `show_menu()` y `main()`: presentan y gestionan el ciclo interactivo de la CLI.

Consulta [spec.md](spec.md) para ver los criterios de aceptación de esta versión.
