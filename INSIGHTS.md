# 📊 Insights & Findings

# 1️⃣ Launch Site Trends

## Flight Number vs Launch Site

* Early launches (Flight Numbers 0–20) were primarily conducted from CCAFS SLC-40.
* KSC LC-39A became more dominant during later operational phases.
* VAFB SLC-4E had comparatively fewer launches, indicating specialized mission usage.

### Insight

Launch site selection evolved alongside SpaceX operational growth and mission complexity.

---

# 2️⃣ Payload Distribution Analysis

## Payload vs Launch Site

* KSC LC-39A handled several high-payload missions exceeding 10,000 kg.
* CCAFS SLC-40 was commonly used for low and medium payload launches.
* VAFB SLC-4E was associated with medium payload missions.

### Insight

Different launch sites appear optimized for different payload capacities and mission requirements.

---

# 3️⃣ Orbit Type Performance

## Success Rate vs Orbit Type

* SSO missions achieved consistently high success rates.
* GTO and ISS missions had moderate success despite high mission frequency.
* VLEO missions showed strong overall reliability.

### Insight

Mission frequency alone does not guarantee higher success rates. Orbit complexity and operational requirements strongly influence mission outcomes.

---

# 4️⃣ Mission Evolution Over Time

## Flight Number vs Orbit Type

* GTO and ISS missions appeared consistently across multiple mission phases.
* VLEO missions became more common during later operational stages.
* Specialized orbit types such as HEO and GEO appeared infrequently.

### Insight

SpaceX mission objectives diversified significantly over time as operational capabilities improved.

---

# 5️⃣ Payload Mass vs Orbit Type

* GTO missions demonstrated flexibility across a wide payload range.
* LEO missions were associated with lighter payloads.
* VLEO missions concentrated around heavier payloads.

### Insight

Payload mass alone does not fully determine orbit selection; mission objectives and operational constraints also play major roles.

---

# 6️⃣ Launch Success Yearly Trend

## Observations

* Success rates remained relatively low between 2010–2013.
* Significant improvements began around 2014.
* Strong operational consistency emerged after 2015.
* A temporary decline occurred around 2018 before recovering strongly in 2019.

### Insight

The data clearly reflects SpaceX’s technological maturation and improved launch reliability over time.

---

# 7️⃣ Geographic & Infrastructure Insights

## Launch Site Geography

* Launch sites are positioned near coastlines for safety during launch and recovery.
* Florida launch sites benefit from lower latitudes, improving orbital efficiency.
* Major highways and railways are placed close enough for logistics while remaining safely distant from launch hazards.

### Insight

Geographic positioning plays a critical role in launch efficiency, recovery logistics, and operational safety.

---

# 8️⃣ Dashboard Insights

## Site Performance

* KSC LC-39A contributed the highest share of successful launches.
* CCAFS SLC-40 showed higher historical failure ratios during earlier operational phases.

## Payload Analysis

* Payload ranges between 3000–5000 kg showed strong landing success performance.
* Falcon 9 Full Thrust (FT) boosters dominated successful heavy payload missions.

### Insight

Booster upgrades and payload optimization significantly improved landing reliability.

---

# 9️⃣ Machine Learning Findings

## Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 83.33%   |
| SVM                 | 83.33%   |
| Decision Tree       | 83.33%   |
| KNN                 | 55.56%   |

### Key Observations

* Logistic Regression, SVM, and Decision Tree established highly effective decision boundaries.
* KNN underperformed due to sparse feature distributions and categorical encoding complexity.

### Insight

Linear and tree-based models were better suited for this dataset than distance-based approaches.

---

# 🔟 Confusion Matrix Insights

## Observations

* The final model correctly identified all successful landing events in the test sample.
* A few failed landings were incorrectly predicted as successful.

### Insight

The model demonstrates strong success prediction capability but still carries moderate risk when classifying failure cases.

---

# 🏁 Final Conclusion

This project demonstrates how:

* Data Science
* SQL Analytics
* Interactive Visualization
* Geographic Analysis
* Machine Learning

can be combined to solve real-world aerospace prediction problems.

The analysis successfully identified:

* Launch success trends
* Payload behavior patterns
* Orbit-based operational differences
* Geographic launch advantages
* High-performing predictive models

The final classification models achieved up to **83.33% accuracy**, showing that publicly available launch data can effectively predict Falcon 9 booster recovery outcomes.
