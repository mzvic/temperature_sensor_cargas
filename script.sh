#!/bin/bash

echo Introduce fecha y hora yyy-mm-dd hh:mm:ss
read fecha_usr hora_usr

sudo date -s "${fecha_usr} ${hora_usr}"

cd test 
python main2.py