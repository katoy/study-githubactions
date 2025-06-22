# NumberHolder プロジェクト

NumberHolder プロジェクトは、2つの整数を保持し、それらの整数を返すシンプルな Python クラスです。

## 必要な環境

*   Python 3.9 以降
*   pytest

## インストール方法

```bash
pip install -r requirements.txt
```

## 実行方法

```bash
python number_class.py
```

## テスト方法

```bash
pytest
```

## テストカバレッジの計測

カバレッジ計測には `pytest-cov` を利用しています。

```bash
pytest --cov=number_class test/
```

カバレッジの詳細レポート（HTML）は以下で生成できます：

```bash
pytest --cov=number_class --cov-report=html test/
open htmlcov/index.html  # macOSの場合
```

## Lint チェック

コードのスタイルチェックには `flake8` を利用しています。

```bash
flake8 number_class.py test/
```

## CI（GitHub Actions）

pushやPR時に自動でテスト・カバレッジ計測が実行されます。

## 貢献方法

1.  リポジトリをフォークします。
2.  新しいブランチを作成します。
3.  変更をコミットします。
4.  プルリクエストを送信します。

## ライセンス

MIT
