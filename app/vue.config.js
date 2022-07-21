const { defineConfig } = require('@vue/cli-service')
const NodePolyfillPlugin = require('node-polyfill-webpack-plugin')

module.exports = defineConfig({
  publicPath: process.env.NODE_ENV === 'production' ? '/codstorage/' : '/',

  transpileDependencies: true,
  configureWebpack: {
    plugins: [
      new NodePolyfillPlugin()
    ],
    // Copied from:
    //    https://stackoverflow.com/a/64392550
    resolve: {
      fallback: {
        fs: false
      }
    },
    optimization: {
      splitChunks: {
        chunks: 'all',
      },
    },
  },
});
