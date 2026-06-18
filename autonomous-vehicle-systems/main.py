from sensor import get_sensor_data
from decision import decide
from control import apply_brake

data = get_sensor_data()
action = decide(data)
result = apply_brake(action)

print(result)