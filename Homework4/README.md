# Machine Learning Homework IV: Clustering & Dimensionality Reduction

This is my solution for **Homework IV** of the **Machine Learning** (Aprendizagem) course at LEIC, Instituto Superior Técnico (2023/2024). This final assignment focuses on unsupervised learning, specifically **k-means clustering** and **Principal Component Analysis (PCA)**.

## Project Structure

The homework explores how to find patterns in unlabeled data and reduce feature dimensionality while preserving information.

### Part I: Pen-and-Paper (Theoretical)
* **Bayesian Clustering**: 
    * Estimating parameters (means, probabilities) for a mixture model using Bernoulli and Multivariate Gaussian distributions.
    * Calculating cluster membership probabilities for new observations.
* **Silhouette Analysis**: Manual calculation of the silhouette coefficient for clusters to assess separation and cohesion using Manhattan distance.
* **Clustering Metrics**: Identifying the number of ground truth classes based on the purity of a given clustering solution.



### Part II: Programming (Practical)
Using the `column_diagnosis.arff` dataset (normalized with `MinMaxScaler`), the following unsupervised tasks were performed:
1.  **k-means Clustering**:
    * Applying k-means for $k \in \{2, 3, 4, 5\}$.
    * Evaluating the quality of clusters using **Silhouette scores** and **Purity metrics**.
2.  **Principal Component Analysis (PCA)**:
    * Identifying the total variability explained by the top two principal components.
    * Inspecting absolute weights (loadings) to rank input variables by their relevance to each component.
3.  **Data Visualization**:
    * Projecting high-dimensional data into a 2D space using PCA.
    * Creating side-by-side plots to compare original ground truth labels (diagnoses) against the $k=3$ cluster assignments.
4.  **Clinical Interpretation**: Discussing how clustering results can characterize distinct populations of healthy and ill individuals based on biomechanical features.
