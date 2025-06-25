from sympy import symbols, Eq, solve

class ZAScience:
    def __init__(self):
        self.logs = []

    def antimatter_containment(self):
        B, q, r, v = symbols('B q r v')
        eq = Eq(B * r, q * v)
        result = solve(eq, B)
        self.logs.append(f"Antimatter solver: {result}")
        return str(result)

    def cryosleep_decay(self, temp_celsius):
        rate = 0.0003 * (37 - temp_celsius)
        self.logs.append(f"Cryosleep decay @ {temp_celsius}°C: {rate:.4f}")
        return rate
