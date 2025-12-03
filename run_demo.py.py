from src.guardian import GuardianAI
import time

def simulate_demo():
    ai = GuardianAI()

    # Example GPS paths (user + follower)
    alice_path = [(12.9716 + i*0.0001, 77.5946 + i*0.0001) for i in range(6)]
    follower_path = [(12.9715 + i*0.0001, 77.5945 + i*0.0001) for i in range(6)]
    other_path = [(12.9700 + i*0.0001, 77.5900 + i*0.0001) for i in range(6)]

    for i in range(6):
        ai.feed_gps("alice", alice_path[i])
        ai.feed_gps("follower", follower_path[i])
        ai.feed_gps("other", other_path[i])

        if i == 2:
            ai.feed_text("Stop following me!")

        ai.feed_frame(f"frame_{i}")

        ai.check_following("alice")

        time.sleep(0.1)

    ai.save_memory("incidents.csv")
    print("Simulation complete → incidents.csv created!")

simulate_demo()
