from logic_utils import check_guess, reset_game_state, validate_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_validate_guess_out_of_bounds_low():
    ok, guess, err = validate_guess("0", 1, 100)
    assert not ok
    assert guess == 0
    assert "between 1 and 100" in err


def test_validate_guess_out_of_bounds_high():
    ok, guess, err = validate_guess("101", 1, 100)
    assert not ok
    assert guess == 101
    assert "between 1 and 100" in err


def test_reset_game_state(monkeypatch):
    # Ensure reset_game_state sets all expected fields and uses the provided bounds.
    state = {
        "attempts": 99,
        "secret": 999,
        "status": "won",
        "history": [1, 2, 3],
        "score": 123,
    }

    # Force deterministic secret generation
    monkeypatch.setattr("random.randint", lambda low, high: 42)

    reset_game_state(state, low=1, high=10)

    assert state["attempts"] == 1
    assert state["secret"] == 42
    assert state["status"] == "playing"
    assert state["history"] == []
    assert state["score"] == 0
