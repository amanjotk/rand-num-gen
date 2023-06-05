import random


def random_number_generator(lower_limit: int, upper_limit: int) -> int:
    """_summary_

    Args:
        lower_limit (int): _description_
        upper_limit (int): _description_

    Returns:
        int: _description_
    """
    return random.randint(lower_limit, upper_limit)