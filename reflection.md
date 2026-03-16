# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

The game loaded, but it behaved inconsistently as soon as I started testing it through the live Streamlit app. The first obvious bug was that the hint text was backwards: when my guess was below the debug secret, the app told me to go lower instead of higher. I also found that the app converted the secret number to a string on some turns, which made comparisons inconsistent and produced nonsense hint behavior. On top of that, the attempt counter started off by one, the reset flow hard-coded a `1..100` secret even when difficulty changed, and the real logic was still duplicated inside `app.py` instead of being refactored into `logic_utils.py`.

---

## 2. How did you use AI as a teammate?

I used Codex as the main coding assistant and Chrome DevTools MCP to inspect and interact with the running Streamlit app. One correct AI-guided direction was to move the pure game functions into `logic_utils.py` and keep the secret number in `st.session_state` so Streamlit reruns would not replace the game state unexpectedly. I verified that by running the manual test script with `uv run python tests/test_game_logic.py` and by checking the live app's debug panel while submitting guesses. One misleading AI-generated idea was already present in the starter code: it converted the secret number to a string on alternating turns to work around type issues, but that actually broke comparisons, so I rejected that approach after testing the live app and reading the code closely.

---

## 3. Debugging and testing your fixes

I treated a bug as fixed only after I could explain the code path, verify the helper logic directly, and see the expected behavior in the running app. The most useful code-level check was `uv run python tests/test_game_logic.py`, which now runs manual assert-based tests for winning guesses, high/low outcomes, decimal input rejection, range selection, and score updates. I also used the Developer Debug Info section in the Streamlit UI to compare my guesses against the actual secret number and confirm that the corrected hint text matched the real comparison. AI helped most with narrowing the likely failure points, but I still had to verify each suggestion against both the code and the live browser behavior.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script from top to bottom every time the user interacts with a widget, so plain local variables do not behave like persistent game state. If I want values like the secret number, score, or attempt history to survive those reruns, I need to store them in `st.session_state` and reset them intentionally when the game starts over. The project made that concrete because the game only became stable after I treated the secret number and counters as persistent session state instead of temporary variables. I would explain it to a friend as: Streamlit redraws the app on each interaction, and `session_state` is the place where you keep the parts of the program that should survive that redraw.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is separating pure logic from UI code before I start debugging deeply, because it made the helper functions much easier to reason about and test. Next time I work with AI on a coding task, I would ask it for smaller, more targeted changes and verify each one before letting it touch multiple concerns at once. This project changed the way I think about AI-generated code because I saw that "working code" can still hide bad assumptions, inconsistent contracts, and misleading fixes. AI can accelerate debugging, but only if I keep checking the behavior myself instead of trusting the first plausible answer.
