const { defineConfig } = require('@vue/cli-service');
const path = require('path');

module.exports = defineConfig({
  transpileDependencies: true,

  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    }
  },

  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    }
  },

  chainWebpack: config => {
    // 确保 Webpack 正确处理图片等静态资源
    config.module
      .rule('images')
      .use('file-loader')
      .loader('file-loader')
      .options({
        name: 'img/[name].[hash:7].[ext]'
      });
  },

  devServer: {
    host: 'localhost', 
    port: 8080,
  },
  pages: {
    index: {
      entry: 'src/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'We Hack the Site', // 设置网页标题
    }
  }
});