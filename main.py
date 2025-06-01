# main.py

import numpy as np
import matplotlib.pyplot as plt
from src.data.yfinance_loader import fetch_price_data, calculate_log_returns
from src.engine.montecarlo_var import simulate_portfolio_returns, calculate_var, calculate_cvar

# Define portfolio tickers and weights
tickers = ['NVDA', 'META', 'AMD', 'BTC-USD']
weights = np.array([0.25, 0.25, 0.25, 0.25])  # Equal-weighted

# Load historical prices and compute returns
price_df = fetch_price_data(tickers, start_date="2018-01-01")
log_returns = calculate_log_returns(price_df)

# Simulate portfolio returns (e.g., 10-day horizon)
simulated_returns = simulate_portfolio_returns(log_returns, weights, num_simulations=100000, horizon_days=10)

# Calculate VaR and CVaR
var_95 = calculate_var(simulated_returns, 0.95)
var_99 = calculate_var(simulated_returns, 0.99)
cvar_95 = calculate_cvar(simulated_returns, 0.95)
cvar_99 = calculate_cvar(simulated_returns, 0.99)

# Display results
print("Portfolio Risk Estimates (10-day horizon)")
print("------------------------------------------")
print(f"VaR (95%):  {var_95:.4f}")
print(f"VaR (99%):  {var_99:.4f}")
print(f"CVaR (95%): {cvar_95:.4f}")
print(f"CVaR (99%): {cvar_99:.4f}")

# Plot distribution
plt.figure(figsize=(10, 6))
plt.hist(simulated_returns, bins=100, color='lightgray', edgecolor='black')
plt.axvline(var_95, color='red', linestyle='--', label='VaR 95%')
plt.axvline(var_99, color='blue', linestyle='--', label='VaR 99%')
plt.axvline(cvar_95, color='darkred', linestyle=':', label='CVaR 95%')
plt.axvline(cvar_99, color='darkblue', linestyle=':', label='CVaR 99%')
plt.title("Simulated Portfolio Return Distribution")
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure before showing
output_path = r"C:\Users\adity\OneDrive\Documents\GitHub\VaR-CVaR-Estimation-for-AI-Stocks-Bitcoin-Correlated-Portfolio\var_cvar_distribution.png"
plt.savefig(output_path, dpi=300)
print("Plot saved as var_cvar_distribution.png")

plt.show()
