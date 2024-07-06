"""
Module: Random utilities

This module provides utilities related to random number generation
and random choices using the random module.
"""

import random

from typing import List

def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> List[int]:
    """
    Generate a sorted list of unique random numbers for a ticket.

    Parameters:
    min (int): The minimum possible value of the random number (must be at least 1).
    max (int): The maximum possible value of the random number (must be at most 1000).
    quantity (int): The number of unique random numbers to generate (must be between min and max).

    Returns:
    List[int]: A sorted list of unique random numbers, or an empty list if parameters are invalid.
    """

    if not 1 <= min_number <= max_number <= 1000 or not min_number <= quantity <= max_number - min_number + 1:
        return []

    picking = set()
    while len(picking) < quantity:
        picking.add(random.randint(min_number, max_number))

    return sorted(picking)

# Example usage
print(get_numbers_ticket(1, 50, 5))
print(get_numbers_ticket(-1, 50, 5))
print(get_numbers_ticket(1, 1001, 5))
print(get_numbers_ticket(1, 5, 6))
