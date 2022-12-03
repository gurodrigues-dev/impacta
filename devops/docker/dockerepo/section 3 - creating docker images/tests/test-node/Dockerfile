FROM node:12-alpine
WORKDIR /app
COPY . .
RUN apk add --no-cache python2 g++ make
CMD ["node", "src/index.js"]
EXPOSE 3000
