FROM node:8.15.1-alpine AS builder
# FROM node:8.15.1-alpine

RUN mkdir react && \
    cd react && \
    yarn init -y && \
    mkdir src public && \
    yarn add react react-dom && \
    yarn add webpack webpack-dev-server webpack-cli --dev && \
    yarn add @babel/core babel-loader @babel/preset-env @babel/preset-react @babel/cli --dev

COPY ./package.json ./webpack.config.js ./.babelrc /react/
COPY ./src/* /react/src/

WORKDIR /react

RUN yarn build

FROM  builder
COPY --from=builder /react/public/js/app.js /react/public/js/app.js

WORKDIR /react
CMD ["yarn", "start"]
