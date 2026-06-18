from decision import decide

def test_decision():
    assert decide("Obstacle detected") == "STOP"