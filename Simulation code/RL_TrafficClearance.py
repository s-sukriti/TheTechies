import time
import random

class TrafficSignal:
    def __init__(self):
        self.congestion_level = "High"
        self.traffic_extension = 0
    
    def update_congestion_level(self, new_level):
        self.congestion_level = new_level
        if self.congestion_level == "High":
            self.traffic_extension = random.randint(550, 850)
        elif self.congestion_level == "Medium":
            self.traffic_extension = random.randint(300, 450)
        elif self.congestion_level == "Low":
            self.traffic_extension = random.randint(50, 150)
        print("Congestion level at traffic signal is", self.congestion_level)
        print("Traffic extends to", self.traffic_extension, "meters from the signal.")

    def clear_traffic(self):
        self.traffic_extension = 0
        print("Traffic cleared at the traffic signal.")

    def update_signal_for_ambulance(self, ambulance_distance):
        if self.traffic_extension == 0:
            return False  # No need to change signal if traffic already cleared
        if ambulance_distance <= 250:  # If ambulance is closer than 250m, clear traffic immediately
            self.clear_traffic()
            return True
        return False

class Ambulance:
    def __init__(self, distance_to_signal):
        self.distance_to_signal = distance_to_signal
        self.slowed_down = False
    
    def move(self):
        if self.distance_to_signal > 0:
            self.distance_to_signal -= 50  # Ambulance movement speed: 50m/s
            print("Ambulance moved. Distance to signal:", self.distance_to_signal)
        else:
            print("Ambulance has reached the traffic signal.")

    def slow_down(self):
        print("Ambulance slowed down by traffic.")
        self.slowed_down = True
    
    def notify_clear(self):
        print("Ambulance notified: Traffic cleared. Moving at 25m/s.")
        self.slowed_down = False

class ReinforcementLearningAgent:
    def __init__(self):
        self.Q_values = {}
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor
    
    def update_Q_value(self, state, action, reward, next_state):
        if state not in self.Q_values:
            self.Q_values[state] = {a: 0 for a in ["High", "Medium", "Low"]}
        if next_state not in self.Q_values:
            self.Q_values[next_state] = {a: 0 for a in ["High", "Medium", "Low"]}
        
        max_next_Q = max(self.Q_values[next_state].values())
        self.Q_values[state][action] += self.alpha * (reward + self.gamma * max_next_Q - self.Q_values[state][action])
    
    def select_action(self, state):
        if state not in self.Q_values:
            return random.choice(["High", "Medium", "Low"])
        else:
            return max(self.Q_values[state], key=self.Q_values[state].get)

def main():
    # Choose random congestion level
    congestion_levels = ["High", "Medium", "Low"]
    random_congestion = random.choice(congestion_levels)
    print("Randomly chosen traffic congestion level:", random_congestion)
    
    traffic_signal = TrafficSignal()
    traffic_signal.update_congestion_level(random_congestion)
    ambulance = Ambulance(1500)  # Starting distance to signal
    agent = ReinforcementLearningAgent()
    
    for _ in range(1000):  # Number of iterations for learning
        current_state = traffic_signal.congestion_level
        action = agent.select_action(current_state)
        reward = random.randint(-10, 10)  # Random reward for demonstration
        
        # Simulate ambulance checking traffic signal congestion level and updating Q-values
        next_state = traffic_signal.congestion_level
        agent.update_Q_value(current_state, action, reward, next_state)
    
    # Simulate ambulance approaching signal
    while ambulance.distance_to_signal > 0:
        if ambulance.distance_to_signal == 1000:
            print("Checking congestion level at 1000m...")
        elif ambulance.distance_to_signal == 500:
            print("Checking congestion level at 500m...")
        elif ambulance.distance_to_signal == 250:
            print("Checking congestion level at 250m...")
        
        if ambulance.distance_to_signal <= traffic_signal.traffic_extension:
            ambulance.slow_down()
            agent.update_Q_value(traffic_signal.congestion_level, "High", -5, traffic_signal.congestion_level)
            agent.update_Q_value(traffic_signal.congestion_level, "Medium", -5, traffic_signal.congestion_level)
            agent.update_Q_value(traffic_signal.congestion_level, "Low", 10, traffic_signal.congestion_level)
        ambulance.move()  # Ensure ambulance moves even if slowed down
        if traffic_signal.update_signal_for_ambulance(ambulance.distance_to_signal):  # Adjust signal if traffic cleared
            ambulance.notify_clear()
        time.sleep(1)  # Wait
if __name__ == "__main__":
    main()
