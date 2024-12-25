FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install --force
RUN npm install -g @angular/cli@17

COPY . .

EXPOSE 4200

CMD ng serve --host 0.0.0.0