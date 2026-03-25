# Machine Learning Homework III: Regression & Neural Networks

This is my solution for **Homework III** of the **Machine Learning** (Aprendizagem) course at LEIC, Instituto Superior Técnico (2023/2024). This assignment focuses on regression models, specifically **Radial Basis Functions (RBF)** and **Multi-Layer Perceptrons (MLP)**.

## Project Structure

The homework explores advanced regression techniques and the optimization of neural network hyperparameters.

### Part I: Pen-and-Paper (Theoretical)
* **Radial Basis Function (RBF) Network**: 
    * Transforming bivariate observations into a high-dimensional space using Gaussian kernels.
    * Calculating the optimal weight vector using the Moore-Penrose pseudo-inverse.
    * Predicting target values for new observations in the transformed space.
* **Multi-Layer Perceptron (MLP) Backpropagation**:
    * Manual execution of the backpropagation algorithm.
    * Computing gradients for weights and biases across hidden and output layers.
    * Updating parameters using a specific learning rate ($\eta$) and the Squared Error loss function.



### Part II: Programming (Practical)
Using the `winequality-red.csv` dataset, the task is to estimate wine quality based on physicochemical properties using MLP regressors:
1.  **MLP Architecture**:
    * Implementation of an MLP with 2 hidden layers (10 nodes each) and ReLU activation.
    * Use of **Early Stopping** (20% validation split) to prevent overfitting.
    * Analysis of residue distributions (absolute errors) via histograms.
2.  **Integer Regression Refinement**:
    * Assessing the impact of rounding and bounding estimates to valid quality scores (integers within a specific range).
    * Measuring performance changes using **Mean Absolute Error (MAE)**.
3.  **Iteration vs. Early Stopping**:
    * Comparing model performance (RMSE) when using fixed iteration counts (20, 50, 100, 200) versus dynamic early stopping.
    * Critical analysis of how the number of batches impacts convergence and generalization.
