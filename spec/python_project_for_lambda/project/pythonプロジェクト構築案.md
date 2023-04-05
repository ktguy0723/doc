# Pythonプロジェクト構築案

## 1. 概要
- PythonとVSCodeを使ったプロジェクト構築方法

## 1.構成
- テスト: pytest
- カバレッジ: pytest-cov
- AWS Lambda: boto3

## 2.手順
1. プロジェクトの作成
```bash
$ mkdir [プロジェクトファイル名]
$ cd [プロジェクトファイル名]
$ code . 
```
2. 仮想環境の作成
`ctrl + @`でターミナルを起動し、下記を実行する。
```bash
$ python3 -m venv .venv
```
これにより、.venvという名前の仮想環境が作成される。

3. VSCodeの設定
Pythonの拡張機能をインストール
これにより、Pythonの開発に必要なツールが自動的にインストールされる。

4. 仮想環境の指定
[View] -> [Command Palette] or `ctrl + shift + P`を開き、"Python: Select Interpreter"と入力し、仮想環境を選択。

5. パッケージのインストール
ターミナルを起動する。（.venv と表示され、仮想環境で実行していることが確認できる。）  
以下のコマンドを使用して、必要なパッケージをインストールする。
```bash
 pip install pytest pytest-cov boto3
```

6. プロジェクトの構成
プロジェクトのフォルダに、以下のファイルとフォルダを作成。
- main.py：AWS LambdaにアップロードするPythonスクリプト
- tests/：UnitTestを格納するフォルダ
- requirements.txt：依存パッケージを格納するファイル

7. main.pyの作成
/project/main.py を参照

8. UnitTestの作成
/project/tests/test_main.py を参照
注意：`__init__.py`も作ること

9. カバレッジの測定
以下のコマンドを使用して、pytest-covを使用してカバレッジを測定。
```bash
$ pytest --cov=main tests/
$ pytest --cov=main --no-cov-on-fail tests/ # 上記で実行しない場合
$ pytest --cov=main --cov-report=html --no-cov-on-fail tests/ # レポート出力したい場合
```

10. AWS Lambdaへのデプロイ
- AWS Lambdaコンソールにアクセスして、新しいLambda関数を作成
- ランタイムにPython 3.xを選択し、アップロードするファイルにmain.pyを指定
- 依存パッケージをインストールするために、requirements.txtをアップロード

TODO: AWS Lambda　CLIからのデプロイ

11. 仮想環境を抜ける
```bash
$ deactivate
```