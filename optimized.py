import csv
import time


MAX_AMOUNT = 500


def get_actions():
    """Get actions data, remove corrupt data, and return it."""
    actions = []
    with open("dataset2_Python+P7.csv", newline="") as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            try:
                row["price"] = float(row["price"])
                row["profit"] = float(row["profit"])
                if row["price"] > 0 and row["profit"] > 0:
                    actions.append(row)
            except ValueError:
                print("corrupted data")
    return actions


def calculation_action_profit_amount(actions):
    """Add 'profit' value to every actions.
    Caculate with price * %.
    """
    for action in actions:
        action["profit_amount"] = float(
            f'{action["price"] * (action["profit"] / 100):.2f}'
        )
    actions = sorted(actions, key=profit_amount, reverse=True)
    return actions


def show_actions(actions):
    """Show every actions."""
    for action in actions:
        print(
            f"- Nom : {action['name']}, Prix : {action['price']},"
            f" Pourcentage : {action['profit']}, Montant des gains : {action['profit_amount']}"
        )


def all_combinaisons(actions):
    """get all possibilities of combinations."""
    combinations = [[]]
    for action in actions:
        newset = [i + [action] for i in combinations]
        combinations.extend(newset)
    return combinations


def best_actions(actions):
    """Calculate the best actions, thanks to best 'profit'
    for a maximum amount to 500 euros.
    """
    profit = 0
    result = 0
    actions_build = []
    actions_sorted = calculation_action_profit_amount(actions)
    for action in actions_sorted:
        if action["price"] < MAX_AMOUNT - result and action["price"] >= 1:
            result += action["price"]
            profit += action["profit_amount"]
            actions_build.append(action)
    print(
        f"\n- La meilleure combinaison d'actions pour un maximum de {MAX_AMOUNT} euros : "
        f"\n- Pour {result} euros placés, en 2 ans vous gagnez :"
        f" {round(profit, 2)} euros de bénéfice."
    )
    return actions_build


def price(action):
    """get 'price' key"""
    return action["price"]


def profit_amount(action):
    """get 'action' key"""
    return action["profit_amount"]


def main():
    """Launch program."""
    actions = get_actions()
    show_actions(best_actions(actions))


start = time.perf_counter()
main()
end = time.perf_counter()
print(f"- Temps de calcul : {round(end - start, 4)} secondes.")
