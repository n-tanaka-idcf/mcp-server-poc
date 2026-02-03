import itertools

import pytest
from mcp_servers.sample import roll_dice_impl


def test_roll_dice_returns_expected_length() -> None:
    results = roll_dice_impl(5)
    assert isinstance(results, list)
    assert len(results) == 5


def test_roll_dice_values_are_in_1_to_6(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "mcp_servers.sample.random.randint",
        lambda a, b: 6,
    )
    results = roll_dice_impl(3)
    assert results == [6, 6, 6]


def test_roll_dice_calls_randint_n_times(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[int, int]] = []

    def fake_randint(a: int, b: int) -> int:
        calls.append((a, b))
        return 1

    monkeypatch.setattr("mcp_servers.sample.random.randint", fake_randint)

    results = roll_dice_impl(4)
    assert results == [1, 1, 1, 1]
    assert calls == [(1, 6), (1, 6), (1, 6), (1, 6)]


@pytest.mark.parametrize("n_dice", [0, -1, -10])
def test_roll_dice_non_positive_returns_empty_list(n_dice: int) -> None:
    # Current implementation uses range(n_dice), which yields no iterations for n_dice <= 0.
    assert roll_dice_impl(n_dice) == []


def test_roll_dice_can_return_mixed_values(monkeypatch: pytest.MonkeyPatch) -> None:
    seq = itertools.cycle([1, 2, 3, 4, 5, 6])
    monkeypatch.setattr("mcp_servers.sample.random.randint", lambda a, b: next(seq))
    assert roll_dice_impl(6) == [1, 2, 3, 4, 5, 6]
