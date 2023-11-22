#!/bin/bash
echo "La fecha actual es: $(date)"

read -p "Deseas cambiarla? (s/n): " input

if [ "$input" = "s" ]; then
   echo "Introduce Fecha y Hora (yyyy-mm-dd hh:mm:ss)"
   read -p "Fecha: " fecha_usr
   read -p "Hora: " hora_usr
   sudo date -s "${fecha_usr} ${hora_usr}"
   python main.py
elif [ "$input" = "n" ]; then
   echo "Ejecutando python main.py..."
   python main.py
else
   echo "Opción no válida. Por favor, selecciona 's' o 'n'."
fi

