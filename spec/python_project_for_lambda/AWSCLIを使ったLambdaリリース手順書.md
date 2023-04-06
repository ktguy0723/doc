# AWS CLIでLambdaへのデプロイについて

## 1. 新規作成
1.1. AWS CLIをインストールし、設定。
TODO

1.2. ローカル環境でLambda関数のコードを作成。
AWSCLIを使ったLambdaリリース手順書.md 参照

1.3. 作成したLambda関数をzip化
7z.exeをインストール、環境変数を設定する。
```bash
$ cd project/src
$ 7z.exe a ../output/src.zip main.py
```

1.4. AWS CLIを使用して、Lambda関数を作成。以下のコマンドを実行。`/project/create_lambda.sh` 参照


```bash
aws lambda create-function --function-name my-function \
--runtime python3.8 --role $IAM_ROLE \
--handler main.lambda_handler --zip-file fileb://output/src.zip
```
パラメータ
function-name：Lambda関数の名前
runtime：Lambda関数で使用するプログラミング言語のランタイム（例：python3.8）
role：Lambda関数が使用するIAMロールのARN
handler：Lambda関数のハンドラー名
zip-file：Lambda関数のコードを含むZIPファイルのパス

1.5. Lambda関数が作成されたことを確認
```bash
aws lambda get-function --function-name my-function
```
パラメータ
<function-name>：作成したLambda関数の名前を指定

## 2. 編集
2.1. コードの更新
再度、「1.3. 作成したLambda関数をzip化」を実行し、下記のコマンドを実行
```bash
$ aws lambda update-function-code --function-name my-function --zip-file fileb://output/src.zip
```

2.2. 設定の編集
例：関数のタイムアウトを10秒に設定
```bash
$ aws lambda update-function-configuration --function-name my-function --timeout 10
```




