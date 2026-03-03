# 🛒 E-Commerce Playwright Automation Framework

A scalable, production-ready UI automation framework built using **Python, Playwright, and Pytest**, designed with industry best practices like Page Object Model (POM), Driver Factory Pattern, BDD support, and CI/CD compatibility.

---

## 🚀 Tech Stack

* **Python 3.10+**
* **Playwright**
* **Pytest**
* **Pytest-BDD**
* **Pytest-HTML Reports**
* **Logging (Python logging module)**

---

## 📁 Project Structure

```
ecommerce-playwright-framework/
│
├── core/                # Framework engine
│   ├── driver_factory.py
│   ├── base_page.py
│
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│
├── tests/               # Test cases
│   ├── test_login.py
│
├── features/            # BDD feature files
│   ├── login.feature
│
├── utils/               # Utilities
│   ├── config.py
│   ├── logger.py
│
├── reports/             # Test reports, logs, videos
│
├── conftest.py          # Pytest fixtures & CLI options
├── pytest.ini           # Pytest configuration
├── requirements.txt     # Dependencies
└── README.md
```

---

## 🏗 Framework Design Patterns Used

* ✅ Page Object Model (POM)
* ✅ Driver Factory Pattern
* ✅ Centralized Configuration
* ✅ Fixture-based Test Setup
* ✅ CLI-based Dynamic Browser Control
* ✅ Video Recording Support
* ✅ HTML Reporting
* ✅ CI/CD Ready Structure

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd ecommerce-playwright-framework
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Playwright Browsers

```bash
playwright install
```

---

## ▶️ Running Tests

### Run all tests

```bash
pytest
```

### Run in headed mode (visible browser)

```bash
pytest --headed
```

### Run with slow motion (for demo/debug)

```bash
pytest --headed --slow 500
```

### Run in specific browser

```bash
pytest --browser firefox --headed
```

Supported browsers:

* chromium
* firefox
* webkit

---

## 📊 Reports & Artifacts

After execution:

* 📄 HTML Report → `reports/report.html`
* 📝 Logs → `reports/test.log`
* 🎥 Videos (if enabled) → `reports/videos/`

---

## 🧪 Sample Test Flow

1. Launch browser
2. Navigate to application
3. Perform login
4. Validate successful login
5. Close browser

---

## 🔍 Key Features

* Dynamic browser selection via CLI
* Headless / Headed execution
* Slow motion debugging
* Video recording support
* Clean teardown
* Scalable structure for large projects
* Easy integration with Jenkins / GitHub Actions

---

## 🔄 Continuous Integration (CI Ready)

This framework is compatible with:

* Jenkins
* GitHub Actions
* GitLab CI
* Dockerized execution

Headless mode is recommended for CI pipelines.

---

## 🧠 Why This Framework?

This project demonstrates:

* Strong automation architecture
* Clean separation of concerns
* Maintainable and scalable codebase
* Industry-level test design
* Interview-ready automation structure

---

## 👨‍💻 Author

Gaurav Chaudhari
Automation Enthusiast | Python | Playwright | CI/CD

---

## 📌 Future Enhancements

* Allure reporting integration
* Parallel execution
* Network request interception
* Environment switching (QA/Stage/Prod)
* Docker support
* API + UI hybrid testing

---

## ⭐ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is for educational and demonstration purposes.
