#!/bin/bash
echo La fecha actual es: "$(date)"

read -p "Deseas cambiarla? (s/n): " input

if [[ "$input" == "s" ]]; then
   echo "Introduce Fecha y Hora (yyyy-mm-dd hh:mm:ss)"
   read fecha_usr hora_usr
   #sudo date -s "${fecha_usr} ${hora_usr}"
   #python main.py
elif [[ "$input" == "n" ]]; then
   #python main.py
   echo "python main.py"
else
   echo "The strings are different."
fi
