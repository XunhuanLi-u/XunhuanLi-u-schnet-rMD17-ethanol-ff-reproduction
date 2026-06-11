import matplotlib.pyplot as plt

n_train = [50, 100, 200]
force_mae = [3.9876, 2.8884, 1.8346]
energy_mae = [1.4213, 1.2807, 0.7284]

plt.figure(figsize=(6, 4))
plt.plot(n_train, force_mae, marker="o", linewidth=2, label="Force MAE")
plt.plot(n_train, energy_mae, marker="s", linewidth=2, label="Energy MAE")

plt.xlabel("Number of training samples")
plt.ylabel("MAE")
plt.title("Initial learning curve on MD17 ethanol")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("results/initial_learning_curve.png", dpi=300)
plt.show()
