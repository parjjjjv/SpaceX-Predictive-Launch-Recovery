# 🚀 SpaceX Predictive Launch Recovery

A complete end-to-end Data Science and Machine Learning project focused on predicting the successful landing of SpaceX Falcon 9 first-stage boosters using public launch data.

## 📌 Project Overview

SpaceX significantly reduced launch costs through reusable Falcon 9 boosters. Predicting whether the first stage will successfully land is valuable for:

* Cost estimation
* Mission planning
* Aerospace analytics
* Competitive commercial bidding

This project applies:

* Data Collection
* Data Wrangling
* Exploratory Data Analysis (EDA)
* Interactive Visualization
* Machine Learning Classification

to analyze historical SpaceX launch data and predict landing success.

---

# 🧠 Problem Statement

Can we predict whether the Falcon 9 first-stage booster will land successfully using publicly available launch data?

---

# ⚙️ Technologies Used

## Programming & Analysis

* Python
* Pandas
* NumPy
* Scikit-learn
* SQLite

## Visualization

* Matplotlib
* Seaborn
* Plotly Dash
* Folium

## Data Collection

* SpaceX REST API
* Web Scraping using BeautifulSoup

---

# 📂 Project Workflow

## 1️⃣ Data Collection

Data was collected from:

* SpaceX REST API
* Wikipedia launch records through web scraping

### Extracted Features

* Booster Version
* Payload Mass
* Orbit Type
* Launch Site
* Mission Outcome
* Landing Outcome
* Latitude & Longitude

---

## 2️⃣ Data Wrangling

Performed:

* Missing value handling
* Data type corrections
* Feature engineering
* Label encoding
* Outcome classification

---

## 3️⃣ Exploratory Data Analysis (EDA)

### Visualization Analysis

Analyzed relationships between:

* Payload Mass vs Launch Site
* Payload Mass vs Orbit Type
* Flight Number vs Orbit Type
* Flight Number vs Launch Site

### SQL Analysis

Performed SQL queries to analyze:

* Launch frequencies
* Orbit-wise success rates
* Payload statistics
* Launch trends
* Landing outcomes

---

## 4️⃣ Interactive Visual Analytics

### Folium Maps

Built interactive launch site maps showing:

* Launch locations
* Coastline proximity
* Railway & highway distances
* Geographic advantages

### Plotly Dash Dashboard

Interactive dashboard with:

* Launch site filtering
* Payload sliders
* Pie charts
* Scatter plots
* Real-time callbacks

---

## 5️⃣ Predictive Analysis

Implemented multiple classification models:

* Logistic Regression
* Support Vector Machine (SVM)
* Decision Tree
* K-Nearest Neighbors (KNN)

### Model Evaluation

Models were evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification comparison

---

# 📊 Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 83.33%   |
| SVM                 | 83.33%   |
| Decision Tree       | 83.33%   |
| KNN                 | 55.56%   |

---

# 🔍 Key Findings

* Falcon 9 FT boosters showed significantly higher landing success.
* Payload ranges between 3000–5000 kg achieved strong recovery performance.
* KSC LC-39A demonstrated the highest overall launch success contribution.
* Launch success improved consistently from 2010–2020.
* Geographic positioning near coastlines improves operational safety.

---

# 📈 Dashboard Features

✔ Launch Site Selection
✔ Payload Range Filtering
✔ Success vs Failure Analysis
✔ Booster Performance Comparison
✔ Interactive Scatter Plots

---

# 🗺️ Geographic Insights

* Launch sites are positioned near coastlines for safety.
* Florida launch sites benefit from lower latitude for orbital efficiency.
* Railways and highways are strategically placed for payload transport.

---

# 🧪 Machine Learning Insights

* Logistic Regression, SVM, and Decision Tree performed equally well.
* KNN struggled due to sparse and high-dimensional categorical features.
* The final models achieved strong success recall for safe landing prediction.


---

# 🚀 Future Improvements

* Use larger and newer launch datasets
* Deploy prediction model using Flask or FastAPI
* Add deep learning models
* Build real-time launch prediction API
* Integrate live SpaceX API updates

---

# 📚 References

* SpaceX REST API
* IBM Data Science Capstone Project
* Plotly Dash Documentation
* Folium Documentation
* Scikit-learn Documentation

---

# 👨‍💻 Author

**Parjanya Vasisht**

* BCA Student
* Data Analytics & Machine Learning Enthusiast
* Professional Cricketer

---

# ⭐ Acknowledgements

This project was developed as part of the IBM Data Science Professional Certificate Capstone Project.
