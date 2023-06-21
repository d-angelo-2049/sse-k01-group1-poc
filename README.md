# sse-k01-group1-poc
このリポジトリはスマートエスイー K01 スマート開発実習 group1用です。 <br>
## 概要
- 庭の雑草刈り時候補日提案

## 当面やること（全部簡単なスクリプトでよい）
- 天気情報の取得
- Google Calendar の予定を取得
- 天気情報とGoogle Calendarの予定から 直近2週間分の雑草刈り候補日を提示

## links
- [リーンキャンバス](https://miro.com/app/board/uXjVMB-tnT8=/)
- [ストーリーマッピング](https://miro.com/app/board/uXjVMAJL7hI=/)

## セットアップ
パッケージ管理ツールとして poetry を使用しています。 <br>
poetry 環境を構成する方法は [こちらの Poetry をインストールする](https://pleiades.io/help/pycharm/poetry.html#748fc371) に沿って 構築してください。 <br>
また、Python 3.7 以上が必要になります。

### はじめてのひと
1. 本リポジトリをクローンする
```commandline
$ git clone git@github.com:d-angelo-2049/simple-ccm-study.git
```
2. 依存関係を インストール する
```commandline
$ poetry install
```
3. 依存が整ったら自由にスクリプトを組んでください。

### 依存を追加・更新したい場合
1. `pyproject.toml`をひらく
2. `[tool.poetry.dependencies]`のセクションに必要な依存を定義する。

```toml
# 定義追加の例です。
# major の前の ^ はその version 以上という制約です。
google-api-python-client = "^2.13.0"
google-auth-httplib2 = "^0.1.0"
google-auth-oauthlib = "^0.4.6"
```
3. 依存関係を更新する
```commandline
$ poetry update
```
