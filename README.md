# Flight-Delay-Prediction
___

## Problem Statement

Analyze the airline's comprehensive dataset and develop a predictive model to accurately forecast flight delays. The goal is to create a reliable tool that can predict whether a given flight will be delayed based on the scheduled departure information. Ensuring passenger satisfaction and managing expectations are critical, so minimizing false negatives should be important.

I also deployed the prediction model on Huggingface

link: https://huggingface.co/spaces/aliaufa/Flight-Delay-Prediction?logs=build

## Methods used

1. Data Visualization
2. Feature Engineering
3. Machine Learning
    - Logistic Regression
    - KNN
    - Decision Tree
    - Random Forest
    - Gradient Boosting
4. Cross Validation
5. Hyperparameter Tuning

## Technologies
1. Python
2. Pandas
3. Seaborn
4. Scikit-Learn
5. Streamlit
6. Huggingface

---

## Findings

1. Flight Departure Time: Most flights depart between 6 to 8 AM, with a peak around 1 PM. Afternoon to evening flights have a higher likelihood of experiencing delays.

2. Flight Duration: The majority of flights have a duration of approximately 2 hours, with some outliers representing long-haul flights lasting over 10 hours.

3. Airlines and Delays: Continental Airlines (CO) and Southwest Airlines (WN) have a higher proportion of delayed flights. Southwest Airlines has the highest number of total flights, while Delta Airlines (DL) has the highest number of not delayed flights. Airlines with the lowest delay ratios include US Airways (US), Hawaiian Airlines (HA), PSA Airlines (OH), Mesa Airlines (YV), and AirTran Airways (FL).

4. Busiest Airport: Hartsfield-Jackson Atlanta International Airport (ATL) in Georgia appears to be the busiest airport, with the most frequent destinations.

5. Weekly Distribution: Wednesday to Friday observe higher flight frequencies compared to other days. Additionally, Friday experiences fewer delayed flights.

6. Model Evaluation: The Random Forest model yielded the best recall with a validation score of 56%. However, the model demonstrates signs of overfitting, as the training set scores are significantly higher than the test set scores.

7. Performance Metrics: The model performs better on class 0 (Not Delay) compared to class 1 (Delay) in terms of precision, recall, and F1-score. The test set scores indicate lower overall performance compared to the training set, suggesting the need for addressing overfitting.

8. The model has an accuracy of 64%.

## Conclusion

the model shows a tendency to be conservative in predicting delayed flights, resulting in a higher false negative rate. Further improvements are needed to increase the model's ability to accurately identify delayed flights.

To address the overfitting issue, various approaches can be considered, such as different feature engineering, regularization techniques, and potentially acquiring more diverse data.