# 🎭 GitHub Hybrid Automation Framework

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Pytest](https://img.shields.io/badge/test-pytest-green.svg)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/framework-playwright-orange.svg)](https://playwright.dev/python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 О проекте
Это современный гибридный фреймворк для автоматизации тестирования инфраструктуры **GitHub**. 
Он объединяет тесты на уровне **API** (для скорости и подготовки данных) и **UI** (для проверки пользовательского интерфейса), реализуя полноценный **End-to-End (E2E)** сценарий.

### Ключевые особенности:
*   **Hybrid Approach:** Создание тестовых данных через API и проверка их отображения в UI.
*   **Page Object Model (POM):** Разделение логики страниц и сценариев тестов для чистоты и поддерживаемости кода.
*   **API Client Wrapper:** Собственная обертка над библиотекой `requests` для удобного взаимодействия с REST API.
*   **Data Isolation:** Автоматическое управление жизненным циклом данных (Setup/Teardown) с использованием Pytest Fixtures и `yield`.
*   **Security First:** Безопасное хранение секретов (токенов и логинов) с использованием переменных окружения (`.env`).
*   **CI/CD Ready:** Настроенный пайплайн для автоматического запуска тестов в GitHub Actions.

---

## 🛠 Технологический стек
*   **Language:** Python 3.9+
*   **Test Runner:** Pytest
*   **API Testing:** Requests
*   **UI Testing:** Playwright (Web UI)
*   **Environment Management:** python-dotenv
*   **Infrastructure:** GitHub Actions (CI/CD)

---

## 📂 Структура проекта
```text
github-automation-framework/
├── api/
│   └── github_client.py     # Клиент для работы с GitHub REST API
├── pages/
│   └── repo_page.py         # Page Objects (Локаторы и действия в UI)
├── tests/
│   ├── conftest.py          # Глобальные фикстуры и настройки среды
│   └── test_ui_repos.py     # E2E и UI сценарии
├── .env                     # Секреты (не пушится в репо!)
├── pytest.ini               # Конфигурация запуска Pytest
└── requirements.txt         # Зависимости проекта
```

---

## ⚙️ Быстрый запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/ttolmacheva-qa/github-automation-framework.git
cd github-automation-framework
```

### 2. Настройка окружения
Создайте виртуальное окружение и установите зависимости:
```bash
python3 -m venv .venv
source .venv/bin/activate  # Для macOS/Linux
pip install -r requirements.txt
playwright install chromium
```

### 3. Настройка секретов
Создайте файл `.env` в корне проекта:
```text
GITHUB_TOKEN=your_personal_access_token
GITHUB_USERNAME=your_github_login
```
*Инструкция по получению токена: [GitHub Personal Access Tokens](https://github.com/settings/tokens)*

### 4. Запуск тестов
```bash
# Запуск всех тестов в консольном режиме
pytest

# Запуск с отображением браузера и подробным логом
pytest -v -s --headed
```

---

## 📈 Планы по развитию (Roadmap)
- [ ] Интеграция Allure Reports для визуализации отчетов.
- [ ] Параметризация тестов для проверки различных типов репозиториев.
- [ ] Добавление тестов на Pull Requests и Issues.
- [ ] Настройка Slack-уведомлений о результатах прогона в CI/CD.

---
**Разработано в рамках курса автоматизации тестирования.** 
Автор: [ttolmacheva-qa](https://github.com/ttolmacheva-qa)
