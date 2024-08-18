from collections import defaultdict
from enum import Enum

categories = [
    ["2021 albums", "Taylor Swift albums", "Albums produced by Taylor Swift"],
    [
        "2020 albums",
        "Taylor Swift albums",
        "Albums produced by Taylor Swift",
        "Republic Records albums",
    ],
    [
        "2020 albums",
        "Taylor Swift albums",
        "Albums produced by Taylor Swift",
        "Republic Records albums",
    ],
]


class VALID_STRATEGIES(Enum):
    IN_ONE_OR_MORE = "in_one_or_more"
    CROSSES_THRESHOLD = "crosses_threshold"
    IN_LAST_N_DAYS = "in_last_n_days"
    UNANIMOUS = "unanimous"


def consensus(items: list, strategy: VALID_STRATEGIES, n=5, threshold=0.5) -> set:
    """
    Given a list of lists, returns the consensus of the lists.

    This function accepts the following strategies:

    - IN_ONE_OR_MORE: An item must be in one or more entries.
    - CROSSES_THRESHOLD: An item must be in more than a certain percentage of entries.
    - IN_LAST_N_DAYS: An item must be in the last n entries.
    - UNANIMOUS: An item must be in all entries.
    """
    unique_items = set()
    membership_counts_in_total = defaultdict(int)

    for list_num, item in enumerate(items):
        for i in item:
            unique_items.add(i)

            membership_counts_in_total[i] = membership_counts_in_total[i] + 1

    if strategy == VALID_STRATEGIES.IN_ONE_OR_MORE:
        return unique_items

    if strategy == VALID_STRATEGIES.IN_LAST_N_DAYS:
        return set.intersection(*[set(i) for i in items[-n:]])

    if strategy == VALID_STRATEGIES.UNANIMOUS:
        return set.intersection(*[set(i) for i in items])

    if strategy == VALID_STRATEGIES.CROSSES_THRESHOLD:
        return set(
            [
                i
                for i in membership_counts_in_total
                if membership_counts_in_total[i] / len(items) * 100 > threshold
            ]
        )

    raise ValueError(
        "strategy is not in VALID_STRATEGIES. Choose from: "
        + ", ".join(VALID_STRATEGIES.__annotations__.values())
    )

def order_alphabetically(categories):
    return sorted(categories)

# print(
#     order_alphabetically(consensus(categories, "in_one_or_more"))
# )  # {'Albums produced by Taylor Swift', '2020 albums', 'Republic Records albums', 'Taylor Swift albums'}

print(
    order_alphabetically(consensus(categories, VALID_STRATEGIES.IN_ONE_OR_MORE))
)  # {'Albums produced by Taylor Swift', '2020 albums', 'Republic Records albums', 'Taylor Swift albums'}
print(
    order_alphabetically(consensus(categories, VALID_STRATEGIES.CROSSES_THRESHOLD, threshold=50))
)  # {'2020 albums', 'Taylor Swift albums', 'Albums produced by Taylor Swift'}
print(
    order_alphabetically(consensus(categories, VALID_STRATEGIES.IN_LAST_N_DAYS, n=3))
)  # {'2020 albums', 'Taylor Swift albums', 'Albums produced by Taylor Swift'}
print(
    order_alphabetically(consensus(categories, VALID_STRATEGIES.UNANIMOUS))
)  # {'2020 albums', 'Taylor Swift albums', 'Albums produced by Taylor Swift'}
