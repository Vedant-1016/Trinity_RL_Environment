---
title: Pricing Environment
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_port: 8000
---

---

title: Pricing Environment
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_port: 8000
--------------

# 🚀 Dynamic Pricing & Inventory RL Environment

---

## 🔗 Live Demo

* 🌐 **API Base URL:** https://vedant-10-pricing-environment.hf.space
* 📄 **Interactive Docs (Recommended):** https://vedant-10-pricing-environment.hf.space/docs

> ⚠️ Open `/docs` to interact with the environment easily.

---

## 📌 Overview

This project implements a **reinforcement learning (RL) environment** that simulates a real-world business scenario:

> **How should a company dynamically set prices over time while managing limited inventory to maximize total profit?**

Unlike static prediction systems, this environment models **sequential decision-making**, where actions taken today directly influence future outcomes.

---

## 🎯 Problem Statement

Businesses in domains like e-commerce, airlines, and retail must:

* Set optimal prices
* Manage limited inventory
* Handle uncertain demand
* Compete with market fluctuations

### ❗ Challenges:

* Demand is **stochastic (uncertain)**
* Decisions are **interdependent over time**
* Short-term gains can hurt long-term profit

---

## 💡 Our Solution

We built a **deployable RL environment** where agents learn:

> **Optimal pricing strategies under uncertainty and inventory constraints**

---

## 🧠 Why Reinforcement Learning?

This problem naturally fits RL because:

* 📈 Sequential decisions
* ⏳ Delayed rewards
* 🎲 Uncertainty in demand
* ⚖️ Trade-off between short-term vs long-term profit

---

## ⚙️ Environment Design

---

### 🔹 Observation (Agent View)

The agent receives:

```text
day, inventory, last_sales, last_price, competitor_price, demand_trend
```

---

### 🔹 Action

```text
Set price of product
```

Example:

```json
{ "price": 100 }
```

---

### 🔹 Hidden State (Environment Only)

* Base demand
* Demand volatility
* Internal dynamics

👉 Simulates real-world uncertainty

---

### 🔹 Transition Dynamics

At each step:

1. Demand is simulated:

```text
demand = base_demand - (price effect) + randomness
```

2. Sales are computed:

```text
sales = min(demand, inventory)
```

3. Environment updates:

* Inventory decreases
* Day increments
* Competitor price fluctuates
* Demand trend updates

---

### 🔹 Reward Function

```text
reward = price × sales
```

👉 Represents **profit**

---

### 🔹 Episode Ends When

* Inventory = 0
* OR max days reached

---

## 🔄 Interaction Flow

```text
Agent → Action (price) → Environment → Demand → Sales → Reward → Next State
```

---

## 🧪 Tasks (Difficulty Levels)

| Level  | Description                          |
| ------ | ------------------------------------ |
| Easy   | Stable demand, low volatility        |
| Medium | Moderate uncertainty                 |
| Hard   | High volatility + competitor effects |

---

## 🌍 Real-World Applications

* 🛒 E-commerce pricing
* ✈️ Airline ticket pricing
* 🏬 Retail inventory optimization
* 📦 Supply chain management

---

## 🌐 API Usage

---

### 🔹 Reset Environment

```http
POST /reset
```

---

### 🔹 Take Action

```http
POST /step
```

Example:

```json
{
  "price": 100
}
```

---

### 🔹 Get State

```http
GET /state
```

---

## 🏗️ System Architecture

```text
Agent
  ↓
Client (HTTP)
  ↓
FastAPI Server
  ↓
Pricing Environment
  ↓
Reward + Observation
```

---

## 🛠️ Tech Stack

* FastAPI
* Pydantic
* Docker
* Hugging Face Spaces

---

## 🚀 Key Highlights

✅ Fully deployable RL environment
✅ Real-world economic simulation
✅ Multi-period decision-making
✅ Supports agent benchmarking
✅ Public API for global access

---

## 🧠 What Makes This Unique

Unlike toy environments, this system:

* Models **real business decision-making**
* Captures **long-term effects of actions**
* Includes **uncertainty and competition**
* Is **production-ready and deployable**

---

## 🧪 Example Usage

```python
import requests

url = "https://vedant-10-pricing-environment.hf.space"

# Reset
r = requests.post(f"{url}/reset")
print(r.json())

# Step
r = requests.post(f"{url}/step", json={"price": 100})
print(r.json())
```

---

## 🐳 Run Locally with Docker

```bash
docker build -t pricing-env .
docker run -p 8000:8000 pricing-env
```

---

## 🔮 Future Improvements

* Multi-agent competition
* Regional pricing strategies
* Real-world dataset integration
* Advanced demand modeling

---

## 🏁 Conclusion

This project demonstrates how reinforcement learning can be applied to **real-world economic systems**, enabling intelligent agents to make optimal sequential decisions under uncertainty.

---

## ⚡ Quick Note for Judges

👉 Open the docs directly:

```text
https://vedant-10-pricing-environment.hf.space/docs
```

---

# 🚀 Built for OpenEnv Hackathon
