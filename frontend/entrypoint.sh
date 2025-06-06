#!/bin/sh

# Compilar Tailwind CSS
npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch

# Servir el contenido estático
python3 -m http.server 3000
