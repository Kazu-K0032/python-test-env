# python-test-env

Python を使った検証環境

## 開発環境

Python(Pylance)

## リポジトリのセットアップ

### 1. リポジトリのクローン

```bash
git clone <repository>
cd python-test-env
```

### 2. 仮想環境の作成とアクティベート

```bash
# Linux(必要に応じて)
sudo apt update && sudo apt install -y python3.12-venv

# Python仮想環境を作成
python3 -m venv venv

# 仮想環境をアクティベート
source venv/bin/activate
```

### 3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

#### 4. 環境変数の設定

```bash
# .envファイルを作成
cp env.example .env
```

#### 5. アプリケーションの実行

```bash
python main.py
```
