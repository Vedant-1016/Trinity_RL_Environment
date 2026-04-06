---
title: Pricing Environment
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_port: 8000
---

---


# 🚀 Pricing Environment (OpenEnv RL Benchmark)

## 📌 Overview

This project implements a **real-world Reinforcement Learning environment** for:

> **Dynamic Pricing with Multi-Period Inventory Management**

The goal is to simulate how an intelligent agent adjusts product pricing over time to **maximize total profit** under:

* Inventory constraints
* Demand fluctuations
* Competitor pricing
* Market volatility

---

## 🎯 Motivation

Dynamic pricing is a core problem in:

* E-commerce platforms (Amazon, Flipkart)
* Airline ticket pricing
* Ride-sharing (Uber surge pricing)
* Retail inventory management

This environment provides a **structured benchmark** to evaluate agents on such real-world decision-making tasks.

---

## ⚙️ Environment Design

### 📊 State (Observation)

Each step returns:

```json
{
  "day": int,
  "inventory": int,
  "last_sales": int,
  "last_price": float,
  "competitor_price": float,
  "demand_trend": "increasing" | "decreasing" | "stable"
}
```

---

### 🎮 Action Space

```json
{
  "price": float
}
```

* Range: `[10, 200]`
* Agent decides product price at each timestep

---

### 💰 Reward Function

```text
reward = price × units_sold
```

Where demand depends on:

* Price elasticity
* Competitor price
* Demand trend
* Random volatility

✔ Encourages profit maximization
✔ Provides **dense reward signal**
✔ Penalizes poor pricing strategies

---

### ⛔ Episode Termination

Episode ends when:

* Inventory = 0
* OR max_days reached

---

## 🧠 Tasks & Difficulty Levels

| Task   | Description                                     |
| ------ | ----------------------------------------------- |
| Easy   | High demand, low volatility                     |
| Medium | Moderate demand & volatility                    |
| Hard   | Low demand, high volatility, strong competition |

Each task has different:

* Inventory
* Demand
* Competitor behavior
* Volatility

---

## 🧮 Scoring (Grader)

Score is normalized:

```text
score = total_profit / max_profit
```

Where:

```python
max_profit = {
    "easy": 15000,
    "medium": 12000,
    "hard": 8000
}[task_name]
```

✔ Ensures score ∈ [0, 1]
✔ Allows fair comparison across tasks

---

## 🤖 Baseline Agent

A simple **rule-based agent** is provided:

```text
- Increase price if sales are high
- Decrease price if sales are low
```

✔ No LLM required
✔ Deterministic & reproducible
✔ Serves as baseline for evaluation

---

## 🧪 Inference Script

The `inference.py` script:

* Runs all 3 tasks: easy → medium → hard
* Interacts with deployed API
* Logs structured outputs

---

### 📤 Required Output Format

```text
[START] task=<task_name> env=pricing-env model=<model_name>

[STEP] step=<n> action=price(x) reward=0.00 done=false error=null

[END] success=true steps=<n> score=<score> rewards=r1,r2,...
```

✔ Strictly follows OpenEnv spec
✔ Used for automated evaluation

---

## 🌐 API Endpoints

Base URL:

```text
https://vedant-10-pricing-environment.hf.space
```

---

### 🔹 Reset

```http
POST /reset
```

Resets environment and returns initial state.

---

### 🔹 Step

```http
POST /step
```

Takes action:

```json
{
  "price": 100
}
```

Returns:

```json
{
  "observation": {...},
  "reward": float,
  "done": bool,
  "info": {}
}
```

---

### 🔹 State

```http
GET /state
```

Returns current environment state.

---

### 🔹 Interactive Docs

👉 Visit:

```text
https://vedant-10-pricing-environment.hf.space/docs
```

---

## 🐳 Docker Support

The project includes a working Dockerfile.

### Build:

```bash
docker build -t pricing-env .
```

### Run:

```bash
docker run -p 8000:8000 pricing-env
```

---

## 📦 Project Structure

```text
server/
  ├── app.py
  ├── pricing_env.py

client.py
inference.py
grader.py
tasks.py
model.py
openenv.yaml
requirements.txt
Dockerfile
README.md
```

---

## 📄 OpenEnv Compliance

✔ Typed models (Pydantic)
✔ step / reset / state endpoints
✔ openenv.yaml specification
✔ Structured logging
✔ 3 tasks with graders
✔ Score normalized in [0, 1]

---

## 🔧 Environment Variables

```python
API_BASE_URL = os.getenv("API_BASE_URL", "https://vedant-10-pricing-environment.hf.space")
MODEL_NAME = os.getenv("MODEL_NAME", "pricing-agent")
HF_TOKEN = os.getenv("HF_TOKEN")
```

---

## ⚠️ Notes

* Baseline agent is **rule-based (no LLM required)**
* API is publicly accessible
* All tasks are deterministic given same conditions

---

## 🧪 Sample Output

```text
[START] task=easy env=pricing-env model=pricing-agent
[STEP] step=1 action=price(95) reward=2745.00 done=false error=null
[STEP] step=2 action=price(100) reward=2900.00 done=false error=null
[STEP] step=3 action=price(105) reward=55.00 done=true error=null
[END] success=true steps=3 score=0.570 rewards=2745.00,2900.00,55.00
```

---

## 🏁 Conclusion

This project provides a **realistic RL benchmark** for pricing strategies with:

* Economic realism
* Clear reward signals
* Scalable difficulty
* Full API-based interaction

It is designed for:

✔ Evaluating RL agents
✔ Benchmarking decision-making systems
✔ Extending to advanced learning algorithms

---

## 🚀 Future Work

* RL-based agents (Q-learning / PPO)
* Multi-product pricing
* Demand forecasting integration
* Real-time dashboards

---

## 👨‍💻 Author

Vedant Shah
AI / ML | RL | Systems Design

---
