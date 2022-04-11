import csv
import time


MAX_AMOUNT = 500


def get_actions():
    """Get actions data, remove corrupt data, and return it."""
    actions = []
    with open("dataset1_Python+P7.csv", newline="") as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            try:
                row["price"] = float(row["price"])
                row["profit"] = float(row["profit"])
                if row["price"] >= 1 and row["profit"] >= 1:
                    actions.append(row)
            except ValueError:
                print("corrupted data")
    return actions


def calculation_action_profit_amount(actions):
    """Add 'profit' value to every actions.
    Caculate with price * %.
    """
    for action in actions:
        action["profit_amount"] = truncate(action["price"] * (action["profit"] / 100), 2)

    return actions


def sort_price_and_profit_amount(actions):
    """Sort by ratio price action and profit amount."""
    actions = sorted(actions, key=ratio_price_profit_amount, reverse=False)
    return actions


def show_actions(actions):
    """Show every actions."""
    for action in actions:
        print(
            f"- Nom : {action['name']}, Prix : {action['price']},"
            f" Pourcentage : {action['profit']},"
            f" Montant des gains : {action['profit_amount']}"
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
    profit_amount = 0
    result = 0
    actions_build = []
    actions_with_amount = calculation_action_profit_amount(actions)
    actions_sorted = sort_price_and_profit_amount(actions_with_amount)
    for action in actions_sorted:
        if action["price"] < MAX_AMOUNT - result and action["profit_amount"] >= 1:
            result += action["price"]
            profit_amount += action["profit_amount"]
            actions_build.append(action)
    print(
        f"\n- La meilleure combinaison d'actions"
        f" pour un maximum de {MAX_AMOUNT} euros : "
        f"\n- Pour {truncate(result, 2)} euros placés, en 2 ans vous gagnez :"
        f" {truncate(profit_amount, 2)} euros de bénéfice."
    )
    return actions_build


def profit(action):
    """get 'action' key"""
    return action["profit"]


def ratio_price_profit_amount(action):
    """get 'action' key"""
    return action["price"] / action["profit_amount"]


def main():
    """Launch program."""
    actions = get_actions()
    show_actions(best_actions(actions))

def truncate(num, n):
    """ truncate number. """
    integer = int(num * (10**n))/(10**n)
    return float(integer)

start = time.perf_counter()
main()
end = time.perf_counter()
print(f"\n- Temps de calcul : {truncate((end - start), 4)} secondes.")
