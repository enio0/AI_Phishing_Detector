
import matplotlib.pyplot as plt
import os

# Our model evaluation results
datasets = ["CEAS_08", "Nazario_5"]
accuracy = [99.37, 59.74]

# Create the chart
plt.figure(figsize=(8, 5))

bars = plt.bar(datasets, accuracy, color=["#2E8B57", "#D97732"], width=0.5)
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f"{height:.2f}%",
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

# Chart title and labels
plt.title("Phishing Detector - Model Accuracy Comparison", fontsize=14)
plt.ylabel("Accuracy (%)")
plt.ylim(0, 110)

# Add horizontal grid lines
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.gca().set_axisbelow(True)

# Save the chart
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/model_accuracy.png", dpi=300, bbox_inches="tight")

# Display the chart
plt.show()
