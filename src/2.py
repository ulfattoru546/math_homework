import random

def get_random_number(low: int, high: int) -> int:
    """Generate a random number within the given range (inclusive)."""
    return random.randint(low, high)

def get_random_choice(choices: list[Any]) -> Any:
    """Generate a random choice from the given list of choices."""
    return random.choice(choices)

def get_random_item(items: dict[Any, Any]) -> tuple[Any, Any]:
    """Generate a random item from the given dictionary and its corresponding value."""
    key = random.choice(list(items.keys()))
    return (key, items[key])