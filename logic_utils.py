def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for the selected difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse user input into an integer guess.

    Returns a tuple of:
    - ok: whether parsing succeeded
    - guess_int: parsed integer when ok is True, otherwise None
    - error_message: user-facing validation error when ok is False
    """
    if raw is None:
        return False, None, "Enter a guess."

    text = raw.strip()
    if text == "":
        return False, None, "Enter a guess."

    if "." in text:
        return False, None, "Use whole numbers only."

    try:
        value = int(text)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare a guess to the secret number.

    Returns:
    - outcome: "Win", "Too High", or "Too Low"
    - message: matching hint text for the UI
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Too high. Go LOWER."

    return "Too Low", "📈 Too low. Go HIGHER."


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Return the updated score after a guess."""
    if outcome == "Win":
        points = max(10, 110 - 10 * attempt_number)
        return current_score + points

    if outcome in {"Too High", "Too Low"}:
        return current_score - 5

    return current_score
