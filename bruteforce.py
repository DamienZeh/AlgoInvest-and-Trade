import csv
import time


MAX_AMOUNT = 500


def get_actions():
    """Get actions data, remove corrupt data, and return it."""
    actions = []
    with open("twenty_actions.csv", newline="") as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            try:
                row["price"] = float(row["price"])
                row["profit"] = float(row["profit"])
                if row["price"] > 0.1 and row["profit"] > 0:
                    actions.append(row)
            except ValueError:
                print("corrupted data")
    return actions


def calculation_action_profit_amount(actions):
    """Add 'profit' value to every actions.
    Caculate with price * %.
    """
    for action in actions:
        action["profit_amount"] = truncate(
            float(action["price"] * (action["profit"] / 100)), 2
        )
    return actions


def show_actions(actions):
    """Show every actions."""
    total_amount = actions[-2]
    total_profit = actions[-1]
    print(
        f"\n- La meilleure combinaison d'actions pour un maximum de {MAX_AMOUNT} euros : "
    )
    for action in actions[0]:
        print(
            f"- Nom : {action['name']}, Prix : {action['price']},"
            f" Pourcentage : {action['profit']}, Montant des gains : {action['profit_amount']}"
        )
    print(
        f"\n- Pour un placement de {truncate(total_amount, 2)} euros,"
        f" vous gagnez au bout de deux ans {truncate(total_profit, 2)} euros."
    )


def all_combinaisons(actions):
    """get all possibilities of combinations."""
    combinations = [[]]
    for action in actions:
        newset = [i + [action] for i in combinations]
        combinations.extend(newset)
    return combinations


def actions_choose(actions, max_price):
    """Calculate the best actions, thanks to best 'profit'
    for a maximum amount to 500 euros.
    """
    action_with_profit = calculation_action_profit_amount(actions)
    best_actions = []
    best_price = 0
    best_profit = 0
    for action_set in all_combinaisons(action_with_profit):
        set_price = sum(map(price, action_set))
        set_profit = sum(map(profit_amount, action_set))
        if set_profit > best_profit and set_price <= max_price:
            best_price = set_price
            best_profit = set_profit
            best_actions = action_set
    return best_actions, best_price, best_profit


def price(action):
    """get 'price' key"""
    return action["price"]


def profit_amount(action):
    """get 'action' key"""
    return action["profit_amount"]


def truncate(num, n):
    """ truncate number. """
    integer = int(num * (10**n))/(10**n)
    return float(integer)


def main():
    """Launch program."""
    actions = get_actions()
    show_actions(actions_choose(actions, MAX_AMOUNT))


start = time.perf_counter()
main()
end = time.perf_counter()
print(f"\n- Temps de calcul : {truncate(end - start, 4)} secondes.")
