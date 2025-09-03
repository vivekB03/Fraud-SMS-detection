# SMS Spam Detection 

## 📌 Features

* **Model Training**: Trained on a Kaggle SMS dataset (CSV) using Python and scikit-learn.
* **Flask API**: Served the model predictions via REST API endpoints.
* **Docker Deployment**: Containerized the application for smooth deployment and portability.
* **SMS Client Interface**: Built a simple CLI tool (`sms_client.py`) where users can type SMS text and get predictions instantly.
* **Hosting**: Tested both hosted API and containerized versions for real-world scenarios.

---

## 🛠️ Tech Stack

* **Languages**: Python
* **Libraries**: scikit-learn, pandas, numpy, flask
* **Tools**: Docker, Flask, CMD/Terminal
* **Dataset**: SMS Spam Collection Dataset (Kaggle)

---

## ⚙️ How It Works

1. **Train the Model**

   * Load CSV dataset from Kaggle.
   * Preprocess and train a classification model.
   * Save the trained model (`model.pkl`).

2. **Run Flask API**

   ```bash
   python app.py
   ```

   * API endpoint: `http://127.0.0.1:5000/test?msg=Hello%20World`

3. **Dockerize the App**

   * Build image:

     ```bash
     docker build -t sms-spam-api .
     ```
   * Run container:

     ```bash
     docker run -p 5000:5000 sms-spam-api
     ```

4. **Use SMS Client**

   * Run in terminal:

     ```bash
     python sms_client.py
     ```
   * Enter SMS → get prediction (Spam / Trusted).

---

## 🔍 Example Output

```bash
Enter SMS: You won free money!
Prediction: Spam
```

```bash
Enter SMS: Meeting at 5 PM.
Prediction: Trusted
```

---

## 🚀 Learnings

* Hands-on experience with **Docker containerization and deployment**.
* Debugging **library mismatches and connectivity issues** between Flask API and client.
* Exposure to **real-world ML pipeline**: training → deployment → usability.

---

## 📂 Project Structure

```
├── app.py             # Flask API for model
├── model.pkl          # Trained ML model
├── sms_client.py      # CLI client for predictions
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker setup
└── README.md          # Project documentation
```

