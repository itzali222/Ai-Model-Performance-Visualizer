# ============ Ai Model Perfromance Visualizer =========== 



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# 1. SAMPLE TRAINING HISTORY
# --------------------------------
# Demo values only: baad mein actual model history use karna

history = {
    "epoch": [1, 2, 3, 4, 5, 6],
    "train_accuracy": [0.60, 0.70, 0.78, 0.84, 0.89, 0.93],
    "val_accuracy":   [0.58, 0.67, 0.73, 0.79, 0.82, 0.84],
    "train_loss":     [0.90, 0.70, 0.55, 0.40, 0.30, 0.22],
    "val_loss":       [0.95, 0.76, 0.63, 0.52, 0.48, 0.50]
}

history_df = pd.DataFrame(history)

# Save training history
history_df.to_csv("training_history.csv", index=False)

# --------------------------------
# 2. TRAINING VS VALIDATION ACCURACY
# --------------------------------
plt.figure(figsize=(8, 5))

plt.plot(
    history_df["epoch"],
    history_df["train_accuracy"],
    marker="o",
    label="Training Accuracy"
)

plt.plot(
    history_df["epoch"],
    history_df["val_accuracy"],
    marker="s",
    label="Validation Accuracy"
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Training vs Validation Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------
# 3. TRAINING VS VALIDATION LOSS
# --------------------------------
plt.figure(figsize=(8, 5))

plt.plot(
    history_df["epoch"],
    history_df["train_loss"],
    marker="o",
    label="Training Loss"
)

plt.plot(
    history_df["epoch"],
    history_df["val_loss"],
    marker="s",
    label="Validation Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------
# 4. CONFUSION MATRIX
# --------------------------------
# Demo actual labels aur predicted labels

y_true = np.array([0, 0, 1, 1, 0, 1, 0, 1])
y_pred = np.array([0, 1, 1, 1, 0, 0, 0, 1])

classes = ["Class 0", "Class 1"]

cm = np.zeros((2, 2), dtype=int)

np.add.at(cm, (y_true, y_pred), 1)

plt.figure(figsize=(6, 5))
plt.imshow(cm)

plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.xticks([0, 1], classes)
plt.yticks([0, 1], classes)

for i in range(2):
    for j in range(2):
        plt.text(
            j, i, str(cm[i, j]),
            ha="center",
            va="center"
        )

plt.colorbar()
plt.tight_layout()
plt.show()

# --------------------------------
# 5. MODEL COMPARISON
# --------------------------------
# Demo values only

model_comparison = pd.DataFrame({
    "model_name": ["Model A", "Model B", "Model C"],
    "accuracy": [0.84, 0.89, 0.86]
})

model_comparison.to_csv(
    "model_comparison.csv", index=False
)

plt.figure(figsize=(7, 5))

plt.bar(
    model_comparison["model_name"],
    model_comparison["accuracy"]
)

plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.ylim(0, 1)
plt.tight_layout()
plt.show()

# --------------------------------
# 6. PERFORMANCE SUMMARY
# --------------------------------

best_epoch = history_df.loc[
    history_df["val_accuracy"].idxmax()
]

print("Best Validation Accuracy:",
      best_epoch["val_accuracy"])

print("Best Epoch:", best_epoch["epoch"])

print("Minimum Validation Loss:",
      history_df["val_loss"].min())

print("\nConfusion Matrix:")
print(cm)

print("\nModel Comparison:")
print(model_comparison)

print("\nCSV files saved successfully.")

