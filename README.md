#  Selenium Automation Project

This project is a technical assignment to demonstrate skills in:

- ✅ Selenium automation using Page Object Model (POM) design
- ✅ Web scraping (articles and images)
- ✅ Text processing and translation
- ✅ CI/CD integration using GitHub Actions
- ✅ Cross-browser cloud testing readiness (e.g., BrowserStack)

---

##  Project Overview

- Visit the **El País** Spanish news website
- Navigate to the **Opinion** section
- Scrape first **5 articles**:
  - Get titles and content (in Spanish)
  - Download cover images (if available)
- Translate titles to English
- Analyze repeated words in translated headers

---

##  Tech Stack

- Python 3.10
- Selenium WebDriver
- Googletrans (or alternative translation library)
- Page Object Model (POM) architecture
- GitHub Actions for CI
- Headless Chrome for automation

---

## ⚙️ How to run locally

```bash
git clone <your-repo-link>
cd <your-repo-folder>
pip install -r requirements.txt
python Main.py
