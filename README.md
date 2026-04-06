---
title: Pricing Environment
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_port: 8000
---

---

---
title: Pricing Environment
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_port: 8000
-------------

# 📈 Dynamic Pricing RL Environment

## 🧠 Overview

This project implements a **real-world reinforcement learning environment** for:

> **Dynamic Pricing + Multi-Period Inventory Management**

An agent must dynamically set product prices over time to **maximize total profit**, while adapting to:

* Changing demand
* Competitor pricing
* Inventory constraints
* Market uncertainty

---

## 🎯 Motivation

Pricing is a core real-world decision problem in:

* E-commerce platforms
* Airline ticketing systems
* Retail inventory management

Unlike toy RL environments, this environment introduces:

* **Partial observability** (hidden demand factors)
* **Stochastic demand** (randomness)
* **Multi-step dependencies** (decisions affect future states)

---

## ⚙️ Environment Design

### 🟢 Action Space

```python
price: float
```

The agent selects a price at each timestep.

---

### 🔵 Observation Space

```python
{
  "day": int,
  "inventory": int,
  "last_sales": int,
  "last_price": float,
  "competitor_price": float,
  "demand_trend": str
}
```

The agent observes:

* Current day
* Remaining inventory
* Previous sales
* Competitor pricing
* Demand trend

---

### 🔒 Hidden State (Not Visible to Agent)

```python
{
  "base_demand": float,
  "demand_volatility": float
}
```

These hidden variables make the environment realistic and non-trivial.

---

## 🔁 API Endpoints

| Endpoint | Method | Description         |
| -------- | ------ | ------------------- |
| `/reset` | POST   | Reset environment   |
| `/step`  | POST   | Execute action      |
| `/state` | GET    | Full internal state |

---

## 🧪 Tasks (Difficulty Levels)

### 🟢 Easy

* High demand
* Low volatility
* Short time horizon

### 🟡 Medium

* Moderate uncertainty
* Balanced conditions

### 🔴 Hard

* High volatility
* Competitive pricing pressure
* Long horizon

---

## 🧮 Evaluation / Grading

Each agent is evaluated using a deterministic grading function:

```python
def compute_score(total_profit, max_possible_profit):
    score = total_profit / max_possible_profit
    return max(0.0, min(score, 1.0))
```

### ✔ Properties:

* Normalized score (0 → 1)
* Comparable across tasks
* Reproducible evaluation

---

## 💰 Reward Function

At each timestep:

```python
reward = price * sales
```

### Why this works:

* Encourages profit maximization
* Penalizes poor pricing decisions
* Provides continuous learning signal

---

## 🤖 Baseline Agent

A simple heuristic agent:

* Adjusts price based on demand trend
* Reacts to competitor price
* Demonstrates environment usage

---

## 📊 Baseline Results

| Task   | Profit | Score |
| ------ | ------ | ----- |
| Easy   | ~5700  | ~0.57 |
| Medium | ~4800  | ~0.48 |
| Hard   | ~3900  | ~0.39 |

---

## 🚀 How to Run Locally

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd Trinity_RL_Environment
```

---

### 2. Start Server

```bash
uvicorn Server.app:app --reload
```

Open API docs:

👉 http://127.0.0.1:8000/docs

---

### 3. Test Environment

```bash
python client_test.py
```

---

### 4. Run Baseline Agent

```bash
python inference.py
```

---

## 🐳 Docker Setup

### Build

```bash
docker build -t pricing-env .
```

### Run

```bash
docker run -p 8000:8000 pricing-env
```

---

## 🌐 Deployment

Live deployed environment:

👉 https://vedant-10-pricing-environment.hf.space/docs

---

## 🧩 OpenEnv Compliance

This environment fully satisfies:

* Typed models (Pydantic)
* step(), reset(), state() API
* openenv.yaml specification
* Multi-task setup (easy → medium → hard)
* Deterministic grading
* Dockerized deployment

---

## 💡 Key Highlights

* Real-world RL problem (not a toy environment)
* Partial observability
* Stochastic demand modeling
* Multi-task evaluation
* API-first design

---

## 🏁 Conclusion

This project demonstrates how reinforcement learning can be applied to **real-world economic decision-making**, specifically pricing optimization.

It provides a scalable and realistic benchmark for evaluating intelligent agents.

---

