module.exports = {
  watch: true,
  entry: { app: "./src/index.js" },
  output: {
    path: __dirname + '/public',
    filename: "bundle.js"
  },
  devServer: {
    contentBase: __dirname + '/public',
    port: 3000,
    publicPath: 'bundle.js',
    disableHostCheck: true,
    watchContentBase: true,
    watchOptions: {
            poll: true
    },
    hot: true,
    host: '0.0.0.0'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader'
      }
    ]
  },
  mode: 'none'
};
