from enum import Enum

# Automata ==> State
class TrafficLightState(Enum):
    Merah = "Merah"
    Kuning = "Kuning"
    Hijau = "Hijau"

# Automata ==> State atau Perubahan atau Transisi
# Map<Key, Value> Key => State Awal, Value => State Tujuan
state_transition = {
    TrafficLightState.Merah: TrafficLightState.Hijau,
    TrafficLightState.Kuning: TrafficLightState.Kuning,
    TrafficLightState.Hijau: TrafficLightState.Merah
}

state_duration = {
    TrafficLightState.Merah: 6,
    TrafficLightState.Kuning: 4,
    TrafficLightState.Hijau: 1
}

# current_state = TrafficLightState.Merah
# next_state = state_transition[current_state] # Hijau, Kuning, Merah
# print(next_state)

curerent_state = TrafficLightState.Merah
while True:
    print(f"Traffic Light: {curerent_state.value}")
    time.sleep(state_duration)
    next_state = [state_transition[current_state]]
    curerent_state = next_state


