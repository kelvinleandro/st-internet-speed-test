# ⚡ Internet Speed Test Web App

A clean and modern web application built with Python and Streamlit to measure your internet connection speed. This app provides real-time metrics for download speed, upload speed, and ping, along with details about the server used for testing.

---

## ✨ Features

- **Interactive & User-Friendly:** Simple one-click interface to start the test.
- **Comprehensive Metrics:** Measures key performance indicators:
  - ⬇️ **Download Speed** (Mbps)
  - ⬆️ **Upload Speed** (Mbps)
  - 📶 **Ping** (ms)
- **Smart Server Selection:** Automatically finds the optimal server for the most accurate results.
- **Detailed Information:** Displays your ISP & IP address, plus the test server's sponsor and location.

---

## 🚀 Getting Started

Follow these instructions to get a local copy up and running.

### Installation

1.  **Clone the repository:**

    ```shell
    git clone https://github.com/kelvinleandro/st-internet-speed-test.git
    cd st-internet-speed-test
    ```

2.  **Create and activate a virtual environment:**

    - **Windows:**

      ```shell
      python -m venv .venv
      .venv\Scripts\activate
      ```

    - **macOS / Linux:**
      ```shell
      python -m venv .venv
      source .venv/bin/activate
      ```

3.  **Install the required packages:**
    ```shell
    pip install -r requirements.txt
    ```

---

## 🖥️ Usage

Once the installation is complete, you can run the Streamlit application with a single command:

```shell
streamlit run app.py
```

This command will start the application and automatically open it in your default web browser.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
