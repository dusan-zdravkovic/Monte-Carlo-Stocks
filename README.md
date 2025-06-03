# 📈 Monte Carlo Stock Price Simulation Using Twelve Data API

This project uses real historical stock data to simulate possible future prices using Monte Carlo methods. The goal is to visualize price uncertainty and understand how well such simulations could have predicted actual prices.

- https://twelvedata.com

---

## 🔧 Tools Used

- **Twelve Data API:** For fetching real historical daily stock prices.
- **Python:** Used for all simulation, analysis, and plotting.
- **NumPy, Pandas, Matplotlib:** Key Python libraries used.
- **VSCode + Jupyter Notebooks:** For development, iteration, and visualization.

---

## 🎯 Project Objective

- Simulate 1-year future stock prices for 8 major stocks based on 2020–2021 data.
- Compare the simulation results to actual prices from March 1, 2022.
- Visualize all simulations and final predicted price distributions.
- Analyze accuracy and prediction error.

---

## 💾 Stock Tickers Simulated

```plaintext
AAPL, MSFT, GOOGL, TSLA, META, AMZN, DIS, PFE
```

---

## 🌐 Real-Time API Integration

This project integrates the **Twelve Data API** to fetch historical stock prices programmatically in **JSON format**. Using HTTP requests, Python retrieves structured data for each ticker, which is then processed using **Pandas DataFrames** for simulation.

This automation ensures accuracy, real-world realism, and scalability for expanding the project with more tickers or timeframes.

---

## 📊 Visual Insights

### 🔹 1. AAPL Single Stock Simulation

Shows 100 Monte Carlo paths simulating Apple's stock price in 2022.

![AAPL Simulation](aapl_simulation.png)

---

### 🔹 2. AAPL Distribution vs Actual Price

Histogram of predicted end prices vs the actual price on 2022-03-01.

![AAPL Distribution](aapl_distribution.png)

---

### 🔹 3. All Stock Simulations

Each stock's simulated 1-year price evolution.

![All Simulations](all_simulations.png)

---

### 🔹 4. All Final Price Distributions

End-of-year predicted price distribution for all 8 stocks, compared to real prices.

![All Distributions](all_distributions.png)

---

## 📌 Theoretical Background

Monte Carlo simulation is a mathematical technique that allows us to account for uncertainty in forecasting models. In this project, we use it to simulate possible future stock prices by generating random price paths based on the **geometric Brownian motion** model.

The simulated price \( S_t \) at time \( t \) is calculated as:

\[
S_t = S_0 \times \exp\left(\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right)
\]

Where:
- \( S_0 \) is the initial stock price
- \( \mu \) is the expected return (mean)
- \( \sigma \) is the volatility (standard deviation of returns)
- \( W_t \) is a Wiener process (standard Brownian motion)

---

## 🧠 Conclusions & Takeaways

- The Monte Carlo method is effective in visualizing possible stock price scenarios under uncertainty.
- It provides a probabilistic range rather than a fixed prediction, which is valuable for understanding risk.
- The comparison to real 2022 prices shows that while the method gives reasonable ranges, high volatility stocks (like TSLA) can still deviate greatly.
- The approach is scalable and could be applied to portfolio simulation, option pricing, or financial risk management in future iterations.