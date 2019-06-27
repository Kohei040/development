FROM node:8.15.1-alpine AS builder

RUN mkdir react && \
    cd react && \
    yarn init -y && \
    mkdir src public && \
    yarn add react react-dom && \
    yarn add webpack webpack-dev-server webpack-cli --dev && \
    yarn add @babel/core babel-loader @babel/preset-env @babel/preset-react @babel/cli --dev

COPY ./package.json ./webpack.config.js ./.babelrc /react/

WORKDIR /react
CMD ["yarn", "build"]

FROM  builder

WORKDIR /react
CMD ["yarn", "start"]
