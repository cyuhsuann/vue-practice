FROM node:18

RUN apt-get update

## make the 'app' folder the current working directory
WORKDIR /app

## copy 'package.json' to install dependencies
COPY ./package.json ./yarn.lock /

## copy files and folders to the current working directory 
COPY . .

RUN yarn install


####
# docker build -t my-vue-app .
# docker run -it my-vue-app ----> ' npm run dev -- --host '
####