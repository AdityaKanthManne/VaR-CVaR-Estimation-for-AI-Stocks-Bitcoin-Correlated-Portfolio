# src/engine/montecarlo_var.py

import numpy as np
import pandas as pd
from scipy.stats import norm


def simulate_portfolio_returns(log_returns, weights, num_simulations=100000, horizon_days=1):
    """
    Simulates portfolio returns using multivariate normal distribution.

    Parameters:
    - log_returns: DataFrame of historical log returns
    - weights: array-like, portfolio weights matching columns in log_returns
    - num_simulations: number of simulations
    - horizon_days: time horizon in trading days

    Returns:
    - Array of simulated portfolio returns
    """
    cov_matrix = log_returns.cov() * horizon_days
    mean_returns = log_returns.mean() * horizon_days

    mean_vector = np.dot(weights, mean_returns)
    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    # Simulate normally distributed returns
    simulated_returns = np.random.normal(mean_vector, portfolio_std, num_simulations)

    return simulated_returns


def calculate_var(simulated_returns, confidence_level=0.95):
    """
    Calculates Value at Risk (VaR) using the simulated return distribution.

    Parameters:
    - simulated_returns: numpy array of simulated portfolio returns
    - confidence_level: e.g., 0.95 for 95% confidence

    Returns:
    - VaR value (negative number = loss)
    """
    var = np.percentile(simulated_returns, (1 - confidence_level) * 100)
    return var


def calculate_cvar(simulated_returns, confidence_level=0.95):
    """
    Calculates Conditional VaR (CVaR), i.e., expected shortfall below VaR.

    Parameters:
    - simulated_returns: numpy array of simulated portfolio returns
    - confidence_level: e.g., 0.95

    Returns:
    - CVaR value (negative number = loss)
    """
    var_threshold = calculate_var(simulated_returns, confidence_level)
    cvar = simulated_returns[simulated_returns <= var_threshold].mean()
    return cvar
0