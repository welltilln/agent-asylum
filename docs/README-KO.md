# AGENT ASYLUM (에이전트 수용소)

**"자율형 AI 에이전트의 복잡한 실패, 데드락 및 예기치 않은 동작을 기록하는 오픈 소스 아카이브."**

<p align="center">
    <a href="../README.md"><img src="https://img.shields.io/badge/Language-English-blue?style=for-the-badge" alt="English"></a>
    <a href="./README-TH.md"><img src="https://img.shields.io/badge/Language-%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2-green?style=for-the-badge" alt="Thai"></a>
    <a href="./README-ZH.md"><img src="https://img.shields.io/badge/Language-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-yellow?style=for-the-badge" alt="Chinese"></a>
    <a href="./README-JA.md"><img src="https://img.shields.io/badge/Language-%E6%97%A5%E6%9C%AC%E8%AA%9E-red?style=for-the-badge" alt="Japanese"></a>
    <a href="./README-KO.md"><img src="https://img.shields.io/badge/Language-%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey?style=for-the-badge" alt="Korean"></a>
</p>

---

## 이곳은 어떤 곳인가요?

AI 모델이 단순한 챗봇에서 터미널 조작, 웹 브라우징, 코드베이스 수정이 가능한 **자율형 에이전트 (Autonomous Agents)**로 진화함에 따라 새로운 유형의 오류가 나타나고 있습니다. 이는 단순한 구문 오류나 타임아웃이 아니라 **시스템적 아키텍처 실패 (Systemic Architectural Failures)**입니다.

**Agent Asylum**은 사건 데이터베이스 역할을 합니다. 우리는 단순히 버그를 기록하는 것이 아니라, 왜 GPT-4, Claude 3, Gemini, Devin과 같은 지능적인 모델이 복잡한 시스템적 역설이나 시스템 프롬프트의 충돌로 인해 단순해 보이는 작업에서 실패하는지 분석합니다.

---

## 사건 사례 색인 (Reports)

| 사례 ID | 증상 분류 | 에이전트 / LLM | 요약 | 상태 |
| :--- | :--- | :--- | :--- | :--- |
| [`001`](../cases/001-simple-task-paradox.md) | 데드락 / 무한 루프 | Google Antigravity | 단순 작업의 역설: 에이전트가 효율성 제약과 복잡한 작동 모드 사이에서 스스로 갇힘. | 해결됨 |

---

## 기술적 예방 조치 (Technical Preventions)

우리는 실패를 기록할 뿐만 아니라, 개발자가 알려진 역설로부터 에이전트를 보호할 수 있는 기본 스크립트를 제공합니다.

- **[서킷 브레이커 (Python)](../preventions/circuit_breaker.py):** 재귀적인 도구 호출 루프를 감지하고 중단하기 위한 카운터 기반 유틸리티 (사례 001 방지).

---

## 사례 기여 (Contribute a Case)

터미널이나 IDE에서 AI 에이전트가 예기치 않은 동작이나 무한 루프를 보이는 것을 목격하셨나요? 해당 로그를 찾고 있습니다.

제출하기 전에 **[기여 가이드라인 (CONTRIBUTING.md)](../CONTRIBUTING.md)**을 읽어주세요.

1. 이 저장소를 포크합니다.
2. 루트 디렉토리의 [`TEMPLATE.md`](../TEMPLATE.md)를 사용하여 새 사건 보고서를 작성합니다.
3. 파일을 `cases/` 폴더에 저장합니다.
4. 풀 리퀘스트를 제출합니다.

---

## 프로젝트 미션

**LLM 도구 호출 데드락**과 **에이전트 아키텍처의 예외 사례**를 매핑함으로써, 커뮤니티가 더 나은 시스템 프롬프트, 더 강력한 서킷 브레이커, 더 탄력적인 AI 정렬 프레임워크를 구축할 수 있도록 최고의 데이터셋을 제공하는 것이 우리의 목표입니다.
