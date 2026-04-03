import random
from model import PricingAction, PricingObservation, PricingState


class PricingEnv:

    def __init__(self):
        self.state = None

    # -------------------------
    # RESET
    # -------------------------
    def reset(self, config=None):

        if config is None:
            config = {
                "inventory": 100,
                "base_demand": 80,
                "max_days": 30,
                "competitor_price": 100,
                "demand_volatility": 5
            }

        self.state = PricingState(
            day=1,
            inventory=config["inventory"],
            max_days=config["max_days"],
            last_sales=0,
            last_price=100.0,
            competitor_price=config["competitor_price"],
            demand_trend="stable",
            base_demand=config["base_demand"]
        )

        self.volatility = config["demand_volatility"]

        return self._get_observation()
    # -------------------------
    # STEP
    # -------------------------
    def step(self, action: PricingAction):

        price = action.price

        # --- simulate demand ---
        demand = self.state.base_demand

        # price effect (higher price → lower demand)
        demand -= 0.5 * price

        # competitor effect
        if price < self.state.competitor_price:
            demand += 10
        else:
            demand -= 5

        # randomness
        demand += random.uniform(-self.volatility, self.volatility)

        demand = max(0, demand)

        # --- sales ---
        units_sold = min(int(demand), self.state.inventory)

        # --- profit ---
        cost_price = 50
        profit = (price - cost_price) * units_sold

        # --- update state ---
        self.state.inventory -= units_sold
        self.state.last_sales = units_sold
        self.state.last_price = price

        # update day
        self.state.day += 1

        # update competitor price randomly
        self.state.competitor_price += random.uniform(-5, 5)

        # update trend
        if units_sold > 20:
            self.state.demand_trend = "increasing"
        elif units_sold < 10:
            self.state.demand_trend = "decreasing"
        else:
            self.state.demand_trend = "stable"

        # --- done condition ---
        done = (
            self.state.day > self.state.max_days or
            self.state.inventory <= 0
        )

        return self._get_observation(), profit, done, {}

    # -------------------------
    # OBSERVATION
    # -------------------------
    def _get_observation(self):
        return PricingObservation(
            day=self.state.day,
            inventory=self.state.inventory,
            last_sales=self.state.last_sales,
            last_price=self.state.last_price,
            competitor_price=self.state.competitor_price,
            demand_trend=self.state.demand_trend
        )