# Machine Learning Homework I: Decision Trees & Variable Discrimination

This is my solution for **Homework I** of the **Machine Learning** (Aprendizagem) course at LEIC, Instituto Superior Técnico (2023/2024). The project is divided into a theoretical analysis (Pen-and-paper) and a practical implementation using Python.

## Project Structure

The homework covers the fundamental concepts of supervised learning, specifically focusing on **Decision Trees** and **Feature Selection**.

### Part I: Pen-and-Paper (Theoretical)
* **Information Gain & Entropy**: Calculation of Shannon Entropy and Information Gain to determine optimal splits in a decision tree.
* **Tree Pruning**: Analysis of misclassification error and the impact of pruning on model complexity.
* **Laplace Smoothing**: Application of Laplace estimates to handle probability estimations in leaf nodes.
* **K-Nearest Neighbors (k-NN)**: Manual calculation of distances and classification using different $k$ values and distance metrics.

### Part II: Programming (Practical)
Using the `column_diagnosis.arff` dataset (orthopedic patient data), the following tasks were performed:
1.  **Feature Discrimination**: Using `f_classif` from `sklearn` to identify variables with the highest and lowest discriminative power.
2.  **Model Evaluation**: Assessing training vs. testing accuracy across different tree depths to identify underfitting and overfitting.
3.  **Visual Analytics**:
    * Plotting class-conditional probability density functions.
    * Visualizing the final decision tree structure.
4.  **Clinical Characterization**: Identifying specific feature associations that define conditions like "Disk Hernia" based on the learned model.
