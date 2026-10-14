# AI Model Performance Visualizer

## Project Overview

**AI Model Performance Visualizer** is a Python-based data visualization project designed to analyze and visualize machine learning model performance using training accuracy, validation accuracy, training loss, validation loss, confusion matrices, and model accuracy comparisons.

The project uses numerical computing, data analysis, and visualization libraries to transform model performance metrics into understandable charts and summary reports.

Currently, the project uses sample demonstration data. It can be extended to work with actual training histories and predictions from trained machine learning models.

## Features

- **Training vs. Validation Accuracy:** Visualizes accuracy across training epochs to help understand model learning performance.
- **Training vs. Validation Loss:** Compares training and validation loss to help identify potential overfitting.
- **Confusion Matrix:** Displays the number of correct and incorrect predictions for a binary classification example.
- **Model Accuracy Comparison:** Compares the accuracy scores of multiple hypothetical models using a bar chart.
- **Performance Summary:** Identifies the epoch with the highest validation accuracy and reports the minimum validation loss.
- **CSV Export:** Saves training history and model comparison data into CSV files for further analysis.
- **Automated Visualizations:** Generates charts programmatically using Matplotlib.

## Technologies and Libraries Used

### 1. Python
The primary programming language used to build the project, process data, calculate metrics, and generate visualizations.

### 2. NumPy
Used for numerical computing and array operations.

**Main responsibilities:**
- Creating and manipulating numerical arrays.
- Initializing the confusion matrix.
- Counting actual and predicted class combinations using `np.add.at()`.
- Supporting numerical calculations efficiently.

### 3. Pandas
Used for data organization, analysis, and CSV file handling.

**Main responsibilities:**
- Converting dictionaries into DataFrames.
- Organizing training and validation metrics.
- Identifying the epoch with the highest validation accuracy.
- Calculating the minimum validation loss.
- Exporting training history and model comparison data to CSV files.

### 4. Matplotlib
Used to create visual representations of model performance.

**Main responsibilities:**
- Plotting training and validation accuracy curves.
- Plotting training and validation loss curves.
- Visualizing the confusion matrix.
- Creating a bar chart for model accuracy comparison.
- Adding chart titles, labels, legends, grid lines, and numerical annotations.

## Visualizations Included

| Visualization | Purpose |
|---|---|
| Accuracy Curves | Compare training and validation accuracy |
| Loss Curves | Compare training and validation loss |
| Confusion Matrix | Examine correct and incorrect class predictions |
| Model Comparison | Compare accuracy scores across multiple models |

## Output Files

The project generates the following CSV files:

- `training_history.csv` — Stores epoch-wise training accuracy, validation accuracy, training loss, and validation loss.
- `model_comparison.csv` — Stores model names and their corresponding accuracy scores.

The program also displays four visualizations and prints a performance summary in the terminal.

## Installation

Make sure Python is installed on your system.

Install the required libraries using:

```bash
pip install numpy pandas matplotlib
```

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code or another Python IDE.
3. Install the required libraries.
4. Run the Python script:

```bash
python main.py
```

5. View the generated charts and performance summary.
6. Find the exported CSV files in the working directory.

## Current Limitations

- The current implementation uses demonstration data rather than metrics collected from actual trained models.
- The confusion matrix demonstrates binary classification with two classes.
- Model comparison currently uses predefined accuracy scores.
- The project does not train machine learning models itself.

## Future Improvements

- Integrate trained models using Scikit-learn, TensorFlow, or PyTorch.
- Collect actual training and validation metrics automatically.
- Add precision, recall, F1-score, and other evaluation metrics.
- Support multiclass confusion matrices.
- Compare multiple trained models using consistent test data.
- Export charts and complete performance reports.
- Develop an interactive dashboard using Streamlit.

## Project Purpose

This project demonstrates practical applications of Python, NumPy, Pandas, and Matplotlib in machine learning performance analysis. It provides a foundation for building more advanced model evaluation and reporting tools.

## Author

**Author:** [Ali hussain shah]

**GitHub:** [https://github.com/itzali222]

## License

This project is available for educational and portfolio purposes. Add an appropriate open-source license, such as the MIT License, if you want to permit others to use, modify, and distribute the code under its terms.

