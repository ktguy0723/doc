# AWS サーバレスアプリハンズオン

## 参考URL

- ハンズオン

https://dev.classmethod.jp/articles/serverless-web-app-hands-on/

https://aws.amazon.com/jp/getting-started/hands-on/build-serverless-web-app-lambda-apigateway-s3-dynamodb-cognito/



- CodeCommitで使えるユーザーの作成

https://proglearn.com/2019/12/27/%E3%80%90aws%E3%80%91codecommit%E7%94%A8%E3%81%AEiam%E3%83%A6%E3%83%BC%E3%82%B6%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B%E6%89%8B%E9%A0%86/



## 概要
- ハンズオン参照

## 所感

#### Amplify

- AmplifyはWebアプリのCI/CDを含め、まとめて実施してくれる
  - CodeCommitを使えばAWS上で画面の構成管理がまとまる
  - ブランチ戦略、レビュー方法、自動テスト、環境変数設計は検討が必要
  - Amplifyはビルド時間によって課金が発生する

#### Cognito

- Cognitoのユーザープールを作成して、認証情報の設計検討が重要と感じた
  - 新規ユーザを作成する際はどのような情報を入力させるか（ユーザー名、メールアドレス、パスワードのほかも必要か）
  - パスワードを忘れた場合、どのような手段で復旧する想定か（メールアドレスに送信など）
    - プロバイダーのメールアドレスが必要、AWS SESの知識も必要
  - 二段階認証などは必要か
- 今回のハンズオンでは、e-mail, パスワード, 確認パスワード　を入力すると、登録したe-mailあてにパスコードが通知され、e-mail, パスコードを入力するとログインできる仕組み
- userPoolClientId がなかなか見つからなかったが、[アプリケーションの統合] > [アプリケーションクライアントのリスト] にあった

#### IAM
- 信頼されるエンティティ: ロールを作成するときに指定する。作成するロールがアタッチ可能なAWSリソースを定義する
- ポリシー ≒ AWSリソースへのアクセス権限
- ロール ≒ 1つ以上のポリシーが付与（アタッチ）されており、AWSリソースに付与（アタッチ）される
