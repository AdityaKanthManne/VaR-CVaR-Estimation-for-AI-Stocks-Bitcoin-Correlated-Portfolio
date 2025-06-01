# VaR-CVaR Estimation for AI Stocks and Bitcoin Correlated Portfolio

This project estimates Value-at-Risk (VaR) and Conditional Value-at-Risk (CVaR) for a multi-asset portfolio consisting of top AI-related tech stocks (e.g., NVDA, META, AMD) and Bitcoin. Using historical data, copulas, and Monte Carlo simulations, it quantifies portfolio-level downside risk under various confidence levels and time horizons.

---

## Key Objectives

- Compute Parametric VaR, Historical Simulation VaR, and Monte Carlo VaR
- Estimate CVaR (Expected Shortfall) using tail loss averaging
- Preserve correlation and tail dependencies using t-copulas
- Run simulations for 1-day and 10-day VaR at 95 percent and 99 percent confidence levels
- Visualize portfolio distribution and loss tails

---

## Assets in Portfolio

- NVIDIA (NVDA)
- Meta Platforms (META)
- Advanced Micro Devices (AMD)
- Bitcoin (BTC-USD)

---

## Architecture

```
[ Yahoo Finance Price Feed ]
        ↓
[ Returns Calculator ]
        ↓
[ Simulation Engine (MC, Historical, Parametric) ]
        ↓
[ Risk Metrics (VaR, CVaR) ]
        ↓
[ Visualizations and Report ]
```

---

## Techniques Used

| Method                      | Description                          |
|----------------------------|--------------------------------------|
| Geometric Brownian Motion  | For simulating asset returns         |
| Multivariate Normal & t-Copulas | For dependency modeling        |
| Cholesky Decomposition     | For correlated asset paths           |
| Monte Carlo Simulation     | 100,000 or more portfolio return paths |
| Historical Simulation      | Non-parametric VaR
