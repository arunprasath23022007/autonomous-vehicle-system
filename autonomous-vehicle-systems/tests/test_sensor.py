from sensor import get_sensor_data

def test_sensor_data():
    assert get_sensor_data() == "Obstacle detected"
    