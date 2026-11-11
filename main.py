"""CLI para administrar tareas pendientes con persistencia CSV."""

import csv
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
todos = []
TODOS_FILE = Path("todos.csv")


def add_one_task(title):
    """Agrega una tarea no vacía a la lista y la guarda."""
    task = title.strip()
    if not task:
        console.print("El título de la tarea no puede estar vacío.", style="yellow")
        return False

    todos.append(task)
    console.print(f"Tarea agregada: [bold]{task}[/bold]", style="green")
    save_todos()
    return True


def print_list():
    """Muestra todas las tareas con posiciones que comienzan en 1."""
    if not todos:
        console.print("No hay tareas pendientes.", style="yellow")
        return

    table = Table(title="Tareas pendientes", header_style="bold cyan")
    table.add_column("#", justify="right", style="dim", width=4)
    table.add_column("Tarea", style="white")
    for position, task in enumerate(todos, start=1):
        table.add_row(str(position), task)
    console.print(table)


def delete_task(number_to_delete):
    """Elimina la tarea indicada por una posición numérica desde 1."""
    try:
        position = int(number_to_delete)
    except (TypeError, ValueError):
        console.print("Ingresa una posición numérica válida.", style="yellow")
        return False

    if position < 1 or position > len(todos):
        console.print(f"La posición debe estar entre 1 y {len(todos)}.", style="yellow")
        return False

    removed_task = todos.pop(position - 1)
    console.print(f"Tarea eliminada: [bold]{removed_task}[/bold]", style="green")
    save_todos()
    return True


def save_todos():
    """Guarda las tareas, una por fila, en el archivo CSV local."""
    try:
        with TODOS_FILE.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows([task] for task in todos)
    except OSError as error:
        console.print(f"No se pudieron guardar las tareas: {error}", style="bold red")
        return False
    return True


def load_todos():
    """Carga tareas desde el CSV. Si el archivo no existe, inicia una lista vacía."""
    try:
        with TODOS_FILE.open("r", newline="", encoding="utf-8") as csv_file:
            loaded_tasks = [row[0] for row in csv.reader(csv_file) if row and row[0].strip()]
    except FileNotFoundError:
        loaded_tasks = []
    except (OSError, csv.Error) as error:
        console.print(f"No se pudieron cargar las tareas: {error}", style="bold red")
        return False

    todos.clear()
    todos.extend(loaded_tasks)
    return True


def show_menu():
    """Presenta las opciones disponibles con Rich."""
    console.print(
        Panel(
            "[bold cyan]1[/bold cyan]  Agregar tarea\n"
            "[bold cyan]2[/bold cyan]  Mostrar tareas\n"
            "[bold cyan]3[/bold cyan]  Eliminar tarea\n"
            "[bold cyan]4[/bold cyan]  Guardar tareas\n"
            "[bold cyan]5[/bold cyan]  Salir",
            title="Lista de tareas",
            border_style="cyan",
        )
    )


def main():
    """Ejecuta el menú interactivo hasta que el usuario elija salir."""
    load_todos()
    console.print("[bold green]Gestor de tareas[/bold green]")

    while True:
        show_menu()
        try:
            choice = input("Selecciona una opción (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\nGuardando y cerrando...")
            save_todos()
            break

        if choice == "1":
            title = input("Título de la tarea: ")
            add_one_task(title)
        elif choice == "2":
            print_list()
        elif choice == "3":
            print_list()
            if todos:
                number = input("Número de la tarea que quieres eliminar: ")
                delete_task(number)
        elif choice == "4":
            if save_todos():
                console.print("Tareas guardadas en todos.csv.", style="green")
        elif choice == "5":
            save_todos()
            console.print("¡Hasta luego!", style="bold cyan")
            break
        else:
            console.print("Opción no válida. Elige un número del 1 al 5.", style="yellow")


if __name__ == "__main__":
    main()
