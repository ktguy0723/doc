# Amplify Vue Workshop

## URL
- https://catalog.workshops.aws/amplify-vue3/ja-JP/1-introduction
- https://aws-samples.github.io/jp-contents-hub/#front-end-web-mobile

## 実技
### 2. 環境構築/Vueアプリの作成

#### 2-1. AWS Cloud9
- VSCode で実装するためハンズオンを飛ばした

> Cloud9 では最初にコンソールを開いたときに、AWS 管理の一時認証情報が作成されます。 以降の手順では、Amplify CLI で発行するユーザの権限を使用するため、Cloud9 の一時認証情報を無効化します。 左上から Cloud9 > Preferences > AWS SETTING と進み AWS managed temporary credentials: のトグルを以下の図のように OFF にします。

- これで一時認証情報を無効化できるようだ

#### 2-2. Vue環境
- Viteで構築している
  - ViteではVueを選択するとデフォルトでvue3となるようだ
  - アプリを起動すると（`npm run dev`）localhost:5173 で起動する
  - ポートを変えたい場合、vite.config.jsの設定変更が必要

```js
import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      './runtimeConfig': './runtimeConfig.browser',
    },
  },
  server: {
    host: true,
    port: 8080,
  },
});
```

#### 2-3. Amplify CLI

