# Contexto del proyecto

## Situacion

El equipo de herramientas internas de una pequeña empresa de logistica necesita mejorar el seguimiento de tareas operativas. Actualmente, los coordinadores anotan los pendientes en mensajes de chat y notas sueltas, por lo que algunos seguimientos importantes se pierden entre turnos.

## Objetivo

Crear una herramienta ligera de terminal, desarrollada en Python, que permita gestionar rapidamente las tareas pendientes desde la linea de comandos y conservarlas entre sesiones.

## Comportamiento requerido

- Registrar una tarea nueva por titulo.
- Consultar todas las tareas pendientes, cada una con su posicion numerica.
- Eliminar una tarea usando su posicion en la lista.
- Guardar las tareas en el archivo local `todos.csv`.
- Cargar las tareas desde `todos.csv` para recuperar el progreso.

## Alcance de esta version

No se necesita editar una tarea. Si hay que corregirla, el flujo esperado es eliminarla y crearla nuevamente.