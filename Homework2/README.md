# Machine Learning Homework II: Probabilistic & Instance-Based Learning

This is my solution for **Homework II** of the **Machine Learning** (Aprendizagem) course at LEIC, Instituto Superior Técnico (2023/2024). This assignment focuses on comparing different classification paradigms, specifically **k-Nearest Neighbors (k-NN)** and **Naive Bayes**, through both mathematical analysis and cross-validation.

## Project Structure

The homework explores the trade-offs between instance-based learning and probabilistic graphical models.

### Part I: Pen-and-Paper (Theoretical)
* **Probability Estimation**: Calculating prior and conditional probabilities for a given dataset to perform Naive Bayes classification.
* **Feature Binarization**: Applying binning and binarization techniques to continuous variables for discrete model compatibility.
* **k-NN Regression**: Manual calculation of a distance-weighted k-NN regressor (using Hamming distance and $1/d$ weighting) to predict continuous outcomes.
* **Cross-Validation Mechanics**: Tracing the observations and features used in specific folds of a cross-validation procedure.

### Part II: Programming (Practical)
Using the `column_diagnosis.arff` dataset, the following tasks were implemented in Python:
1.  **Statistical Comparison**:
    * Implementing a **10-fold stratified cross-validation**.
    * Comparing k-NN ($k=5$) against Gaussian Naive Bayes using **boxplots** of fold accuracies.
    * Using `scipy` to perform hypothesis testing to determine if one model is statistically superior to the other.
2.  **Confusion Matrix Analysis**:
    * Computing and visualizing the difference between cumulative confusion matrices for $k=1$ and $k=5$ to observe the impact of neighborhood size on classification errors.
3.  **Critical Analysis**: Identifying the limitations of the Naive Bayes "independence assumption" when applied to biomechanical features that may be highly correlated.
