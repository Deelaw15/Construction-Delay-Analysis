# 🏗️ Construction Delay Risk Estimator

🔗 [👉 Try the App on Streamlit Cloud](https://construction-delay-estimator.streamlit.app/)  
📂 [View the Code on GitHub]([https://github.com/yourusername/construction-delay-estimator](https://github.com/Deelaw15/Construction-Delay-Analysis.git))

---

## 📌 Project Overview

This project is a **Construction Delay Risk Estimator** built using machine learning and deployed as a web app via Streamlit. It predicts the likelihood of delays in construction projects using early-stage data.

> It was built using real-world data from the New York City School Construction Authority (SCA) and is designed to demonstrate how predictive analytics can support better decision-making in construction.
> The model is realistic for early-stage planning and budgeting, as it uses only information typically available before the project starts, such as budget, planned duration, start season, and project phase.
> This project reflects the application of data science principles in a domain-specific context, combining machine learning with practical understanding of construction workflows.
---

## 🎯 Problem Context

Delays are common in construction, leading to cost overruns, missed deadlines, and stakeholder dissatisfaction. Predicting delays ahead of time is difficult, especially without access to full project histories.

This project explores whether **early indicators** like:
- Project phase
- Budget
- Planned duration
- Start season
- Project type

…can be used to flag potential delays.

---

## 🗂️ Dataset Information

- **Source**: NYC Open Data (Capital Project Schedules and Budgets)
- [Dataset link](https://catalog.data.gov/dataset/capital-project-schedules-and-budgets)
- Covers capital projects related to **public school construction and renovations**

---

## 🛠️ Tech Stack

- **Python**
- **Pandas / NumPy** – Data handling
- **Scikit-learn / XGBoost** – Modeling
- **Streamlit** – App deployment
- **Joblib** – Model serialization
- **Git / GitHub** – Version control & sharing

---

## 🔍 Key Features

- Accepts user input for project details (budget, duration, type, etc.)
- Predicts whether the project will be **Delayed** or **On-Time**
- Built with early-stage, pre-construction data only
- Simple UI deployed to the cloud

---

## ⚠️ Domain Awareness & Limitations

- The model is trained on **public school construction projects** in NYC.
- Project types and statuses (e.g., “SCA Lease Site Improvement”) are specific to the **SCA's internal classifications**.
- Therefore, the model **should not be generalized directly** to private-sector or international construction contexts.

### 📈 Future Adaptation

This project shows how data science can support construction planning. With access to new datasets, this approach could be adapted to:

- Housing or commercial developments
- Infrastructure (roads, bridges)
- International construction markets
- Private construction firms with detailed internal records

---

## 🧪 Want to Run It Locally?

You can clone the repo and run `streamlit run app.py` if you have Python and the required libraries installed.

...

## 🧠 Author & Purpose

This project was created by **Faruq Lawal**, a data scientist with a background in civil engineering and construction. It reflects a strong interest in applying data science to real-world challenges in the construction industry.

> 🎯 _The goal of this project is to demonstrate practical ML application, domain understanding, and the ability to deploy solutions that could support early decision-making in construction planning._

## 🤝 Let's Connect

- 💼 [LinkedIn](https://www.linkedin.com/in/faruq-lawal-710871266/)
- 📝 [Portfolio](https://deelaw15.github.io/portfolio/#)
- 💬 Open to feedback, collaboration, and ideas in construction analytics.


