FROM node:18-alpine

WORKDIR /app

# Instalar dependencias
RUN npm install -g npm@10.8.2
RUN npm install -g postcss@8.4.33 autoprefixer@10.4.17 tailwindcss@3.4.1

# Crear directorio dist
RUN mkdir -p dist

# Copiar archivos
COPY . .

# Configurar Tailwind
RUN npx tailwindcss init -p

# Compilar Tailwind CSS
RUN npx tailwindcss -i ./src/input.css -o ./dist/output.css

# Verificar que el archivo CSS se ha creado
RUN test -f ./dist/output.css

# Instalar servidor estático
RUN npm install -g http-server

EXPOSE 3000

CMD ["http-server", "-p", "3000"]
