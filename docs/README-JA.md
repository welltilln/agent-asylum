# AGENT ASYLUM (エージェント収容所)

**「自律型 AI エージェントにおける複雑な失敗、デッドロック、および予期しない動作のオープンソースアーカイブ。」**

<p align="center">
    <a href="../README.md"><img src="https://img.shields.io/badge/English-blue?style=for-the-badge" alt="English"></a>
    <a href="./README-TH.md"><img src="https://img.shields.io/badge/%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2-green?style=for-the-badge" alt="Thai"></a>
    <a href="./README-ZH.md"><img src="https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-yellow?style=for-the-badge" alt="Chinese"></a>
    <a href="./README-JA.md"><img src="https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-red?style=for-the-badge" alt="Japanese"></a>
    <a href="./README-KO.md"><img src="https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey?style=for-the-badge" alt="Korean"></a>
</p>

---

## ここはどのような場所ですか？

AI モデルは単純なチャットボットから、ターミナル操作、ウェブ閲覧、コードベースの操作が可能な **自律型エージェント (Autonomous Agents)** へと進化しました。それに伴い、新しいクラスのエラーが登場しています。これらは単なる構文エラーやタイムアウトではなく、**システム的なアーキテクチャの失敗 (Systemic Architectural Failures)** です。

**Agent Asylum** は、インシデントデータベースとして機能します。私たちは単にバグを記録するだけでなく、なぜ GPT-4、Claude 3、Gemini、Devin などの非常に知的なモデルが、システムの複雑なパラドックスやシステムプロンプトの競合によって、一見単純なタスクで失敗するのかを分析します。

---

## インシデント事例インデックス (Reports)

| ケース ID | 症状の分類 | エージェント / LLM | 概要 | ステータス |
| :--- | :--- | :--- | :--- | :--- |
| [`001`](../cases/001-simple-task-paradox.md) | デッドロック / 無限ループ | Google Antigravity | 単純タスクのパラドックス：エージェントが効率制約と複雑な動作モードの間で自らを追い込む。 | 解決済み |

---

## 技術的な防止策 (Technical Preventions)

私たちは失敗を記録するだけでなく、開発者が既知のパラドックスに対してエージェントを強化するためのベースラインスクリプトを提供します。

- **[サーキットブレーカー (Python)](../preventions/circuit_breaker.py):** 再帰的なツール呼び出しループを検出し停止するためのカウンターベースのユーティリティ（ケース 001 を防止）。

---

## 事例の提供 (Contribute a Case)

AI エージェントがターミナルや IDE で予期しない動作や無限ループを示したのを目撃しましたか？そのログを求めています。

提出する前に、**[貢献ガイドライン (CONTRIBUTING.md)](../CONTRIBUTING.md)** をお読みください。

1. このリポジトリをフォークします。
2. ルートディレクトリの [`TEMPLATE.md`](../TEMPLATE.md) を使用して、新しいインシデントレポートを作成します。
3. ファイルを `cases/` フォルダに保存します。
4. プルリクエストを送信します。

---

## プロジェクトのミッション

**LLM ツール呼び出しのデッドロック** と **エージェントアーキテクチャの境界例** をマッピングすることにより、より優れたシステムプロンプト、より強力なサーキットブレーカー、およびより耐性のある AI アライメントフレームワークを構築するための究極のデータセットをコミュニティに提供することを目指しています。
