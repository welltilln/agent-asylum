# AGENT ASYLUM (艾真体疯人院)

**“自主 AI 艾真体中复杂失败、死锁和意外行为的开源存档。”**

<p align="center">
    <a href="../README.md"><img src="https://img.shields.io/badge/Language-English-blue?style=for-the-badge" alt="English"></a>
    <a href="./README-TH.md"><img src="https://img.shields.io/badge/Language-%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2-green?style=for-the-badge" alt="Thai"></a>
    <a href="./README-ZH.md"><img src="https://img.shields.io/badge/Language-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-yellow?style=for-the-badge" alt="Chinese"></a>
    <a href="./README-JA.md"><img src="https://img.shields.io/badge/Language-%E6%97%A5%E6%9C%AC%E8%AA%9E-red?style=for-the-badge" alt="Japanese"></a>
    <a href="./README-KO.md"><img src="https://img.shields.io/badge/Language-%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey?style=for-the-badge" alt="Korean"></a>
</p>

---

## 这是什么地方？

随着 AI 模型从简单的聊天机器人演变为能够操作终端、浏览网页和处理代码库的 **自主艾真体 (Autonomous Agents)**，一类新型错误也随之出现。这些不仅是语法错误或超时，而是 **系统性架构失败 (Systemic Architectural Failures)**。

**Agent Asylum** 充当事件数据库。我们不仅记录 Bug，还分析为什么极其智能的模型（如 GPT-4、Claude 3、Gemini、Devin 等）会因为复杂的系统悖论或冲突的系统提示词，在看似简单的任务中失败。

---

## 事件案例索引 (Reports)

| 案例 ID | 症状分类 | 艾真体 / LLM | 简短描述 | 状态 |
| :--- | :--- | :--- | :--- | :--- |
| [`001`](../cases/001-simple-task-paradox.md) | 死锁 / 无限循环 | Google Antigravity | 简单任务悖论：艾真体在效率限制和复杂操作模式之间陷入困境。 | 已解决 |

---

## 技术预防措施 (Technical Preventions)

我们不仅记录失败，还提供基准脚本来帮助开发人员加固其艾真体以对抗已知悖论。

- **[断路器 (Python)](../preventions/circuit_breaker.py):** 基于计数器的工具，用于检测并停止递归工具调用循环（防止案例 001）。

---

## 提交案例 (Contribute a Case)

您是否目睹过 AI 艾真体在您的终端或 IDE 中表现出意外行为或无限循环？我们需要这些日志。

在提交之前，请阅读我们的完整 **[贡献指南 (CONTRIBUTING.md)](../CONTRIBUTING.md)**。

1. Fork 本仓库。
2. 使用根目录下的 [`TEMPLATE.md`](../TEMPLATE.md) 起草新的事件报告。
3. 将文件保存在 `cases/` 文件夹中。
4. 提交 Pull Request。

---

## 项目使命

通过绘制 **LLM 工具调用死锁** 和 **艾真体架构边缘案例** 的图谱，我们旨在为社区提供构建更好系统提示词、更强断路器和更具弹性的 AI 对齐框架的终极数据集。
