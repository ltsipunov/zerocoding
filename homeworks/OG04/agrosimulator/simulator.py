import random


class AgrarianSimulator:
    def __init__(self, farms, farmers, grain, gold):
        self.farms = farms
        self.farmers = farmers
        self.grain = grain
        self.gold = gold
        self.previous_farms = farms
        self.previous_farmers = farmers
        self.previous_grain = grain
        self.previous_gold = gold
        self.year = 1  # Track the current year

    def calculate_reproduction_rate(self):
        farmer_to_farm_ratio = self.farmers / self.farms
        if farmer_to_farm_ratio >= 10:
            return 0.9  # Reproduce rate below 1 if over capacity
        else:
            return 1.25 - (0.25 * (farmer_to_farm_ratio / 10))

    def simulate_year(self):
        # Calculate reproduction rate
        reproduction_rate = self.calculate_reproduction_rate()

        # Update farmers
        new_farmers = int(self.farmers * reproduction_rate)
        self.farmers = min(new_farmers, self.farms * 10)  # Cap farmers at 10 per farm

        # Produce grain
        grain_produced = self.farmers * 10
        self.grain += grain_produced

        # Generate grain price
        grain_price = random.normalvariate(10, 2)
        grain_price = max(1, grain_price)  # Ensure price is not negative

        # Report current state
        print(f"\n--- Year {self.year} Report ---")
        print(f"Farms: {self.farms} (Difference: {self.farms - self.previous_farms})")
        print(f"Farmers: {self.farmers} (Difference: {self.farmers - self.previous_farmers})")
        print(f"Grain: {self.grain} tons (Difference: {self.grain - self.previous_grain})")
        print(f"Gold: {self.gold} (Difference: {self.gold - self.previous_gold})")
        print(f"Grain Price: {grain_price:.2f} gold per ton")

        # Update previous values
        self.previous_farms = self.farms
        self.previous_farmers = self.farmers
        self.previous_grain = self.grain
        self.previous_gold = self.gold

        # Increment year
        self.year += 1

        return grain_price

    def sell_grain(self, grain_price):
        while True:
            try:
                grain_to_sell = input(
                    f"How much grain do you want to sell? (Available: {self.grain} tons, or press Enter to quit): ").strip()
                if grain_to_sell == "":
                    return False  # Break the loop if empty string is entered

                grain_to_sell = float(grain_to_sell)
                if 0 <= grain_to_sell <= self.grain:
                    break
                else:
                    print("Invalid amount. Please enter a value between 0 and your available grain.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Sell grain
        gold_earned = grain_to_sell * grain_price
        self.gold += gold_earned
        self.grain -= grain_to_sell

        print(f"You sold {grain_to_sell} tons of grain for {gold_earned:.2f} gold.")
        return True  # Continue the game

    def play(self):
        print("Welcome to the Agrarian Simulator!")
        print("You are a landlord managing farms, farmers, grain, and gold.")
        print("Each turn represents a year. Manage your resources wisely!")
        print("To quit the game, press Enter when asked how much grain to sell.")

        while True:
            grain_price = self.simulate_year()
            if not self.sell_grain(grain_price):
                break  # Exit the game if the player enters an empty string

        # Final stats
        print("\n--- Game Over ---")
        print(f"Final stats after {self.year - 1} years:")
        print(f"Farms: {self.farms}, Farmers: {self.farmers}, Grain: {self.grain} tons, Gold: {self.gold}")


# Initial parameters
initial_farms = 5
initial_farmers = 20
initial_grain = 100
initial_gold = 50

# Start the game
game = AgrarianSimulator(initial_farms, initial_farmers, initial_grain, initial_gold)
game.play()