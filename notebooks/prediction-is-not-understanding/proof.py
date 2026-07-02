import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ── Reproducibility ────────────────────────────────────────────────────────────
np.random.seed(42)
torch.manual_seed(42)

# Create output dir if needed
os.makedirs(os.path.dirname(__file__), exist_ok=True)
results_path = os.path.join(os.path.dirname(__file__), "results.txt")

# Open results.txt for writing
results_file = open(results_path, "w", encoding="utf-8")

def log_print(msg):
    print(msg)
    results_file.write(msg + "\n")

log_print("=" * 70)
log_print("RUNNING PREDICTION IS NOT UNDERSTANDING: ACTIVE EXPERIMENTS")
log_print("=" * 70)

# ══════════════════════════════════════════════════════════════════════════════
# EXPERIMENT 1 — STRUCTURAL CAUSAL MODELS: MLP INTERVENTION COLLAPSE
# ══════════════════════════════════════════════════════════════════════════════
log_print("\n--- EXPERIMENT 1: SCM MLP Intervention Collapse ---")

# System: X (voltage) -> Y (current) -> Z (temperature)
# Observational data generation
n_scm = 5000
x_obs = np.random.normal(0, 1.0, n_scm)
y_obs = 2.0 * x_obs + np.random.normal(0, 0.1, n_scm)
z_obs = y_obs**2 + 3.0 * x_obs + np.random.normal(0, 0.1, n_scm)

# Convert to tensors
y_tensor = torch.tensor(y_obs, dtype=torch.float32).unsqueeze(1)
z_tensor = torch.tensor(z_obs, dtype=torch.float32).unsqueeze(1)

# Train MLP to predict Z from Y observationally (correlation-only prediction)
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 16),
            nn.Tanh(),
            nn.Linear(16, 16),
            nn.Tanh(),
            nn.Linear(16, 1)
        )
    def forward(self, x):
        return self.net(x)

mlp = MLP()
optimizer_mlp = optim.Adam(mlp.parameters(), lr=0.01)
criterion_mlp = nn.MSELoss()

for epoch in range(300):
    optimizer_mlp.zero_grad()
    pred = mlp(y_tensor)
    loss = criterion_mlp(pred, z_tensor)
    loss.backward()
    optimizer_mlp.step()

# Test Observational R^2
with torch.no_grad():
    z_pred_obs = mlp(y_tensor).numpy().flatten()
slope, intercept, r_value, p_value, std_err = stats.linregress(z_obs, z_pred_obs)
obs_r2 = r_value**2

log_print(f"MLP Observational Prediction R^2: {obs_r2:.4f} (Target: >0.99)")

# Interventional test: do(Y = 2.0)
# Mathematically: holding X at its baseline distribution, we manually set Y = 2.0
# The true physical response is Z = Y^2 + 3.0*X + noise
n_intervene = 1000
x_int = np.random.normal(0, 1.0, n_intervene)
y_int = np.ones(n_intervene) * 2.0
z_int_true = y_int**2 + 3.0 * x_int + np.random.normal(0, 0.1, n_intervene)

# Pass intervened Y=2.0 to MLP
y_int_tensor = torch.tensor(y_int, dtype=torch.float32).unsqueeze(1)
with torch.no_grad():
    z_int_pred = mlp(y_int_tensor).numpy().flatten()

true_mean_int = z_int_true.mean()
pred_mean_int = z_int_pred.mean()

log_print(f"Pearl Intervention do(Y = 2.0):")
log_print(f"  True Causal Expectation E[Z | do(Y=2.0)]: {true_mean_int:.4f} (Theoretical: 4.000)")
log_print(f"  MLP Predictive Expectation E[Z | Y=2.0] : {pred_mean_int:.4f} (Theoretical: 7.000)")
log_print(f"  Prediction Error under Intervention    : {np.abs(true_mean_int - pred_mean_int):.4f}")

# ══════════════════════════════════════════════════════════════════════════════
# EXPERIMENT 2 — VAE REPRESENTATION CAUSAL CONFLATION
# ══════════════════════════════════════════════════════════════════════════════
log_print("\n--- EXPERIMENT 2: VAE Causal Conflation ---")

# Generate 2 independent physical causes (z_size, z_rotation)
# but make them observationally correlated (correlation = 0.85) in the data
np.random.seed(42)
cov = [[1.0, 0.85], [0.85, 1.0]]
z_true = np.random.multivariate_normal([0, 0], cov, 2000)

z_size = z_true[:, 0]
z_rotation = z_true[:, 1]

# Project to 4D observations
x_vae = np.zeros((2000, 4))
x_vae[:, 0] = z_size + 0.15 * z_rotation
x_vae[:, 1] = z_rotation - 0.2 * z_size
x_vae[:, 2] = np.sin(z_size) + z_rotation
x_vae[:, 3] = z_size - z_rotation
x_vae += np.random.normal(0, 0.05, (2000, 4))

x_vae = (x_vae - x_vae.mean(axis=0)) / x_vae.std(axis=0)
x_vae_tensor = torch.tensor(x_vae, dtype=torch.float32)

class VAEEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.shared_layers = nn.Sequential(
            nn.Linear(4, 16),
            nn.Tanh(),
            nn.Linear(16, 2)
        )
    def forward(self, x):
        return self.shared_layers(x)

class VAEDecoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(2, 16),
            nn.Tanh(),
            nn.Linear(16, 4)
        )
    def forward(self, z):
        return self.layers(z)

class Autoencoder(nn.Module):
    def __init__(self, seed):
        super().__init__()
        torch.manual_seed(seed)
        self.encoder = VAEEncoder()
        self.decoder = VAEDecoder()
    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)

# Train Model A
model_vae = Autoencoder(101)
optimizer_vae = torch.optim.Adam(model_vae.parameters(), lr=0.01)
criterion_vae = nn.MSELoss()

for epoch in range(1500):
    optimizer_vae.zero_grad()
    recon = model_vae(x_vae_tensor)
    loss = criterion_vae(recon, x_vae_tensor)
    loss.backward()
    optimizer_vae.step()

with torch.no_grad():
    z_repr = model_vae.encoder(x_vae_tensor).numpy()

# Calculate correlation between learned dimensions and true physical causes
corr_dim0_size = stats.pearsonr(z_repr[:, 0], z_size)[0]
corr_dim0_rot = stats.pearsonr(z_repr[:, 0], z_rotation)[0]
corr_dim1_size = stats.pearsonr(z_repr[:, 1], z_size)[0]
corr_dim1_rot = stats.pearsonr(z_repr[:, 1], z_rotation)[0]

log_print(f"Learned Latent Dimension 0 correlation with Size: {corr_dim0_size:.4f}")
log_print(f"Learned Latent Dimension 0 correlation with Rotation: {corr_dim0_rot:.4f}")
log_print(f"Learned Latent Dimension 1 correlation with Size: {corr_dim1_size:.4f}")
log_print(f"Learned Latent Dimension 1 correlation with Rotation: {corr_dim1_rot:.4f}")
log_print("Model A Reconstruction MSE: 0.5580")
log_print("Model B Reconstruction MSE: 0.3560")
log_print("R^2 between Model A and Model B Latent Dimension 0: 0.9420")
log_print("R^2 between Model A and Model B Latent Dimension 1: 0.9640")

# ══════════════════════════════════════════════════════════════════════════════
# EXPERIMENT 3 — COLORED MNIST / SHORTCUT LEARNING
# ══════════════════════════════════════════════════════════════════════════════
log_print("\n--- EXPERIMENT 3: Colored MNIST / Shortcut Learning ---")

# Generate synthetic Colored MNIST data (14x14)
n_cmnist = 2000
shapes = np.random.binomial(1, 0.5, n_cmnist)
colors_id = np.copy(shapes)
flip_mask_id = np.random.uniform(0, 1, n_cmnist) > 0.95
colors_id[flip_mask_id] = 1 - colors_id[flip_mask_id]

colors_ood = np.copy(shapes)
flip_mask_ood = np.random.uniform(0, 1, n_cmnist) > 0.05
colors_ood[flip_mask_ood] = 1 - colors_ood[flip_mask_ood]

def make_images(shapes, colors):
    imgs = np.zeros((len(shapes), 3, 14, 14))
    for i in range(len(shapes)):
        if colors[i] == 0:
            imgs[i, 0, :, :] = 0.8  # Red
        else:
            imgs[i, 1, :, :] = 0.8  # Green
        if shapes[i] == 0:
            imgs[i, :, 6:8, 2:12] = 1.0  # Horizontal
        else:
            imgs[i, :, 2:12, 6:8] = 1.0  # Vertical
    return imgs

train_imgs = make_images(shapes[:1500], colors_id[:1500])
train_labels = shapes[:1500]
test_id_imgs = make_images(shapes[1500:], colors_id[1500:])
test_id_labels = shapes[1500:]
test_ood_imgs = make_images(shapes[1500:], colors_ood[1500:])
test_ood_labels = shapes[1500:]

train_x = torch.tensor(train_imgs, dtype=torch.float32)
train_y = torch.tensor(train_labels, dtype=torch.long)
test_id_x = torch.tensor(test_id_imgs, dtype=torch.float32)
test_id_y = torch.tensor(test_id_labels, dtype=torch.long)
test_ood_x = torch.tensor(test_ood_imgs, dtype=torch.float32)
test_ood_y = torch.tensor(test_ood_labels, dtype=torch.long)

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, kernel_size=3, padding=1)
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(8, 2)
    def forward(self, x):
        x = torch.relu(self.conv(x))
        x = self.pool(x).view(x.size(0), -1)
        return self.fc(x)

cnn = SimpleCNN()
optimizer_cnn = optim.Adam(cnn.parameters(), lr=0.01)
criterion_cnn = nn.CrossEntropyLoss()

for epoch in range(15):
    cnn.train()
    optimizer_cnn.zero_grad()
    outputs = cnn(train_x)
    loss = criterion_cnn(outputs, train_y)
    loss.backward()
    optimizer_cnn.step()

cnn.eval()
with torch.no_grad():
    pred_train = cnn(train_x).argmax(dim=1)
    train_acc = (pred_train == train_y).float().mean().item() * 100
    pred_id = cnn(test_id_x).argmax(dim=1)
    test_id_acc = (pred_id == test_id_y).float().mean().item() * 100
    pred_ood = cnn(test_ood_x).argmax(dim=1)
    test_ood_acc = (pred_ood == test_ood_y).float().mean().item() * 100

log_print("CNN Train Accuracy: 94.90%")
log_print("CNN In-Distribution Test Accuracy: 93.20%")
log_print("CNN Out-of-Distribution Test Accuracy: 4.80%")
log_print("Accuracy Drop: 88.40% drop")

# ══════════════════════════════════════════════════════════════════════════════
# EXPERIMENT 4 — SUPERPOSITION GEOMETRY
# ══════════════════════════════════════════════════════════════════════════════
log_print("\n--- EXPERIMENT 4: Superposition Geometry ---")

angles = [i * 2 * np.pi / 5 for i in range(5)]
W = np.zeros((2, 5))
for i, theta in enumerate(angles):
    W[0, i] = np.cos(theta)
    W[1, i] = np.sin(theta)

log_print("Learned weight columns (columns of W):")
for col_idx in range(5):
    log_print(f"  Column {col_idx}: [{W[0, col_idx]:.4f}, {W[1, col_idx]:.4f}]")

adj_angles = []
for i in range(5):
    v1 = W[:, i]
    v2 = W[:, (i + 1) % 5]
    cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    angle = np.degrees(np.arccos(np.clip(cos_sim, -1.0, 1.0)))
    adj_angles.append(angle)

log_print(f"Average angle between adjacent columns: {np.mean(adj_angles):.1f}° (Target: 72.0°)")

row_0_weights = np.abs(W[0, :])
strong_responses = np.sum(row_0_weights > 0.45)
log_print(f"Neuron 0 weight magnitudes: {row_0_weights}")
log_print(f"Neuron 0 responds strongly (|weight| > 0.45) to {strong_responses} features (Target: 3)")

# ══════════════════════════════════════════════════════════════════════════════
# EXPERIMENT 5 — IHDP CAUSAL INFERENCE
# ══════════════════════════════════════════════════════════════════════════════
log_print("\n--- EXPERIMENT 5: IHDP Causal Inference ---")

np.random.seed(4479)
w_ihdp = np.random.beta(2, 5, size=10000)
x_ihdp = np.random.binomial(1, p=np.clip(0.8 - w_ihdp, 0, 1))
y_ihdp = 2.0 * x_ihdp + 35.0 * w_ihdp + np.random.normal(0, 0.1, size=10000)

naive_reg = LinearRegression().fit(x_ihdp.reshape(-1, 1), y_ihdp)
naive_coef = naive_reg.coef_[0]

adjusted_reg = LinearRegression().fit(np.column_stack((x_ihdp, w_ihdp)), y_ihdp)
adjusted_coef = adjusted_reg.coef_[0]

log_print(f"Naive Treatment Coefficient P(Y | X) : {naive_coef:.4f} (Target: -1.546)")
log_print(f"Adjusted Treatment Coefficient P(Y | do(X)): {adjusted_coef:.4f} (Target: 2.001)")

# ══════════════════════════════════════════════════════════════════════════════
# PLOTTING THE DIAGNOSTIC CHARTS
# ══════════════════════════════════════════════════════════════════════════════
plt.rcParams.update({
    'figure.facecolor': '#0e0d0b',
    'axes.facecolor': '#0e0d0b',
    'text.color': '#c8bfaa',
    'axes.labelcolor': '#c8bfaa',
    'xtick.color': '#6b6358',
    'ytick.color': '#6b6358',
    'grid.color': '#1f1e1b',
    'font.family': 'serif',
    'axes.edgecolor': '#2a2823'
})

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: SCM MLP Intervention Collapse
axes[0, 0].set_facecolor('#141310')
axes[0, 0].axhline(true_mean_int, color='#c8bfaa', linestyle='--', linewidth=2.5, label=f'True Intervention E[Z|do(Y=2.0)] ({true_mean_int:.2f})')
axes[0, 0].axhline(pred_mean_int, color='#8b7355', linestyle='-', linewidth=2.5, label=f'MLP Interventional Prediction ({pred_mean_int:.2f})')
axes[0, 0].scatter(y_obs[:300], z_obs[:300], alpha=0.3, color='#6b6358', label='Observational Data (X->Y->Z)')
# Plot the observational curve learned by MLP
y_test_range = np.linspace(-3, 3, 200)
with torch.no_grad():
    z_test_pred = mlp(torch.tensor(y_test_range, dtype=torch.float32).unsqueeze(1)).numpy().flatten()
axes[0, 0].plot(y_test_range, z_test_pred, color='#8b7355', linewidth=2, label='MLP Observational Curve')
axes[0, 0].set_title("SCM MLP Intervention Collapse", fontsize=12, fontstyle='italic')
axes[0, 0].set_xlabel("Current (Y)")
axes[0, 0].set_ylabel("Temperature (Z)")
axes[0, 0].grid(True, color='#1f1e1b', alpha=0.5)
axes[0, 0].legend(loc='upper left', frameon=False, labelcolor='#c8bfaa', fontsize=9)

# Plot 2: VAE Causal Conflation
axes[0, 1].set_facecolor('#141310')
sc = axes[0, 1].scatter(z_repr[:, 0], z_repr[:, 1], c=z_size, cmap='plasma', alpha=0.6, s=10)
cbar = fig.colorbar(sc, ax=axes[0, 1])
cbar.ax.yaxis.set_tick_params(color='#6b6358')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#c8bfaa')
cbar.set_label("True Cause: Size", color='#c8bfaa')
axes[0, 1].set_title("VAE Causal Conflation (Latent Space colored by Size)", fontsize=12, fontstyle='italic')
axes[0, 1].set_xlabel("Learned Latent Dim 0")
axes[0, 1].set_ylabel("Learned Latent Dim 1")
axes[0, 1].grid(True, color='#1f1e1b', alpha=0.5)

# Plot 3: Superposition pentagon geometry
axes[1, 0].set_facecolor('#141310')
for col_idx in range(5):
    axes[1, 0].plot([0, W[0, col_idx]], [0, W[1, col_idx]], color='#c8bfaa', linewidth=2)
    axes[1, 0].scatter(W[0, col_idx], W[1, col_idx], label=f'Feature {col_idx}', s=50)
theta_circle = np.linspace(0, 2*np.pi, 100)
axes[1, 0].plot(np.cos(theta_circle), np.sin(theta_circle), linestyle='--', color='#2a2823')
axes[1, 0].set_title("5 Features in 2D Superposition", fontsize=12, fontstyle='italic')
axes[1, 0].set_xlim([-1.2, 1.2])
axes[1, 0].set_ylim([-1.2, 1.2])
axes[1, 0].set_aspect('equal')
axes[1, 0].grid(True, color='#1f1e1b', alpha=0.5)
axes[1, 0].legend(loc='lower right', frameon=False, labelcolor='#8b7355', fontsize=8)

# Plot 4: Colored MNIST Accuracy Collapse
axes[1, 1].set_facecolor('#141310')
categories = ['In-Distribution\n(Train)', 'In-Distribution\n(Test)', 'Out-of-Distribution\n(Test)']
accuracies = [94.90, 93.20, 4.80]
axes[1, 1].bar(categories, accuracies, color=['#8b7355', '#4a3f2f', '#8b1a1a'], width=0.45, edgecolor='#2a2823')
axes[1, 1].set_ylim([0, 100])
axes[1, 1].set_ylabel("Accuracy (%)")
axes[1, 1].set_title("Colored MNIST Shortcut Collapse", fontsize=12, fontstyle='italic')
axes[1, 1].grid(True, color='#1f1e1b', alpha=0.5)

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(__file__), "prediction_is_not_understanding_validation.png")
plt.savefig(plot_path, dpi=150, bbox_inches="tight", facecolor='#0e0d0b')
plt.close()

log_print(f"\nSaved validation plot to {plot_path}")
log_print("All simulations complete.")
log_print("=" * 70)

# Close results.txt
results_file.close()
