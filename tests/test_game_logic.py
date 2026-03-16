from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    result, message = check_guess(50, 50)
    assert result == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    result, message = check_guess(60, 50)
    assert result == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    result, message = check_guess(40, 50)
    assert result == "Too Low"
    assert "HIGHER" in message


def test_parse_guess_rejects_decimal_input():
    ok, value, message = parse_guess("12.5")
    assert ok is False
    assert value is None
    assert message == "Use whole numbers only."


def test_update_score_penalizes_incorrect_guesses():
    assert update_score(20, "Too High", 1) == 15
    assert update_score(20, "Too Low", 2) == 15


def test_range_for_normal_mode():
    assert get_range_for_difficulty("Normal") == (1, 100)


def run_all_tests():
    test_winning_guess()
    test_guess_too_high()
    test_guess_too_low()
    test_parse_guess_rejects_decimal_input()
    test_update_score_penalizes_incorrect_guesses()
    test_range_for_normal_mode()
    print("All manual tests passed.")


if __name__ == "__main__":
    run_all_tests()
