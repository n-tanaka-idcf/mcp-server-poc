import random

from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")


def roll_dice_impl(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results.

    This is a pure implementation function so it can be unit-tested without
    involving FastMCP's tool wrapping.
    """
    return [random.randint(1, 6) for _ in range(n_dice)]


@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return roll_dice_impl(n_dice)


if __name__ == "__main__":
    mcp.run()
