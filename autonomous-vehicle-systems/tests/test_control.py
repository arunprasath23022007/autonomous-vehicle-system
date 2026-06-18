from control import apply_brake

def test_control():
    assert apply_brake("STOP") == "Brake applied"