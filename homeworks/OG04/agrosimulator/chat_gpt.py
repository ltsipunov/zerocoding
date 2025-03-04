import random


# Function to calculate the reproduction rate based on the farmers-to-farms ratio
def reproduction_rate(farmers, farms):
    ratio = farmers / farms
    if ratio < 10:
        return 1.25 - 0.025 * (ratio - 1) ** 2  # Gradually approaching 1 as ratio reaches 10
    else:
        return max(1 / ratio, 0.1)  # Cannot drop below 0.1


# Function to calculate the new amount of farmers based on reproduction rate
def calculate_new_farmers(farmers, farms):
    rate = reproduction_rate(farmers, farms)
    return int(farmers * rate)


# Function to generate the grain price for the year
def grain_price():
    return round(random.gauss(10, 2), 2)  # Random price with mean 10 and standard deviation 2


# Main simulation
def agrarian_simulator(initial_farms, initial_farmers, initial_grain, initial_gold):
    # Initialize resources
    year = 1
    farms = initial_farms
    farmers = initial_farmers
    grain = initial_grain
    gold = initial_gold

    # Store previous year's values for tracking differences
    prev_farms, prev_farmers, prev_grain, prev_gold = farms, farmers, grain, gold

    print("Welcome to the Agrarian Simulator Game!")
    print("Your goal is to manage your farms and resources wisely.")

    while True:
        # Grain production for the year
        grain_produced = farmers * 10
        grain += grain_produced

        # Farmer reproduction
        new_farmers = calculate_new_farmers(farmers, farms)
        max_farmers = farms * 10  # Maximum capacity for farmers based on farms
        if new_farmers > max_farmers:
            new_farmers = max_farmers
        farmers_diff = new_farmers - farmers
        farmers = new_farmers

        # Generate grain price for the year
        price = grain_price()

        # Ask the player how much grain to sell
        print(f"\nYear {year}")
        print(f"Grain price this year: {price} gold per ton.")
        print(f"Resources: Farms: {farms}, Farmers: {farmers}, Grain: {grain}, Gold: {gold}")
        sell_amount = input("Enter the amount of grain to sell (or press Enter to end the game): ")

        # End the game if the player enters an empty string
        if sell_amount.strip() == "":
            print("Game over! Thanks for playing.")
            break

        # Ensure valid input
        try:
            sell_amount = int(sell_amount)
            if sell_amount < 0 or sell_amount > grain:
                print("Invalid amount. Please enter a number between 0 and the available grain.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Update grain and gold based on the sale
        grain -= sell_amount
        gold += sell_amount * price

        # Report resources and differences
        print(
            f"End of Year {year}: "
            f"Farms: {farms} (0), "
            f"Farmers: {farmers} ({farmers_diff}), "
            f"Grain: {grain} ({sell_amount - grain_produced}), "
            f"Gold: {gold} (+{sell_amount * price})"
        )

        # Update year and previous year's resources
        year += 1
        prev_farms, prev_farmers, prev_grain, prev_gold = farms, farmers, grain, gold


# Start the game with initial parameters
agrarian_simulator(
    initial_farms=10,  # Initial number of farms
    initial_farmers=50,  # Initial number of farmers
    initial_grain=1000,  # Initial amount of grain
    initial_gold=500,  # Initial amount of gold
)