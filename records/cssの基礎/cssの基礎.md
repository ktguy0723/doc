# CSSの基礎

## 概要

下記の動画を見て学んだことを記載していく。

【初心者向け】CSSの書き方の鉄板講座！美しいWebデザインを自分で設計しよう！～Flexboxの使い方も網羅～【たった1動画で全てが分かるCSSの教科書】

https://www.youtube.com/watch?v=h5xxHuvYy_I



## 内容

### 1. CSS記載場所

1. インラインCSS

   ```html
   <h1 style="color: red;">test</h1>
   ```

2. 内部参照

   ```html
   <style>
       h1 {
           color: red;
       }
   </style>
   ```

3. 外部参照

   ```html
   <link rel="stylesheet" href="css/style.css">
   ```

   ```css
   h1 {
       color: green;
   }
   ```



### 2. セレクタの指定

```html
<header>
	<p>hoge</p>
</header>
<p class="alert">
    アラート
</p>
```

```css
// クラスセレクター
p.alert {
    color: red
}

// 結合子
header p {
    font-size: 10px;
}
```

https://developer.mozilla.org/ja/docs/Web/CSS/CSS_Selectors



### 3. CSSインポート

CSSファイルで`@import`を使うことでCSSファイルのインポートが可能。

```css
@import url(import.css);
```



### 4. CSSで使う単位

```css
div p {
    font-size: 10px; // 10ピクセル（絶対値）
    font-size: 2em; // 親要素(div)の2倍の大きさ（相対値）
    font-size: 2rem; // ルート要素の2倍の大きさ（相対値）
}
.screen {
    vh
    vw
}
```



### 5. 色の指定

```css
.screen {
    color: white: // 文字指定（非推奨）
    color: #fff; //16進法RGB
    color: rgb(255, 255, 255); //10進法RGB
    color: transparent: // 透明
}
```



### 6. 背景

```css
header {
    background-color: #000;
    background-image: url(写真のURL);
    background-repeat: no-repeat;
    background-size: cover;
}
```



### 7. メディアクエリー

```css
// 幅が600pxより小さい場合に適用される
@media(max-width: 600px) {
    header h1 {
        font-size: 1.5rem;
    }
}
```



### 8. インライン、ブロック

- インライン：幅 `display: inline`
- ブロック：1行 `display: block`