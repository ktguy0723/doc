# Glueを使用したモダンアプリケーション

## 参考になるURL
### Amplify
1. 開発者用ドキュメント
APIとの連携とか認証認可系はここでわかると思う  
https://docs.amplify.aws/lib/storage/upload/q/platform/js/#upload-files

### Athena
1. Athena Tutorial (コンソール版)
Athenaについての説明。わかりやすかったが広告が多いため閲覧注意  
https://www.slideshare.net/AmazonWebServicesJapan/amazon-athena-81216877


2. Athena - Glue 考え方の基本
AthenaとGlueの関係性がわかりやすい。ただ、情報量少なめのため補足が必要  
https://blog.serverworks.co.jp/2023/01/05/091657


3. Athena で AWS Glue を使用するときのベストプラクティス
https://docs.aws.amazon.com/ja_jp/athena/latest/ug/glue-best-practices.html


## Tips
### Athena
- S3バケットにdate=yyymmのようにフォルダ切ると、自動でパーテション設定してくれる

