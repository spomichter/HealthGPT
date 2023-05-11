import json
import random
from datetime import datetime, timedelta

def generate_data(start_date):
    activities = ["Meditation", "Run", "Bike", "Alcohol", "Drugs", "Exam"]
    activity_impact = {"Meditation": -10, "Run": -15, "Bike": -20, "Alcohol": 30, "Drugs": 50, "Exam": 40}
    data = []
    brain_burn = 50  # initial brain burn score

    # Generating sleep data
    sleep_start = datetime(start_date.year, start_date.month, start_date.day, random.randint(21, 23), random.randint(0, 59))
    sleep_duration = timedelta(hours=random.randint(6, 8))
    sleep_end = sleep_start + sleep_duration
    data.append({"timestamp": str(sleep_start), "activity": "sleep", "sleep_start": str(sleep_start), "sleep_end": str(sleep_end)})

    # Generating activities and eye tracking tests
    activity_start = sleep_end
    for _ in range(random.randint(5, 10)):  # reasonable number of activities in a day
        activity_start += timedelta(hours=random.randint(1, 2), minutes=random.randint(0, 59))  # assuming a gap between activities
        activity = random.choice(activities)
        brain_burn = max(0, min(100, brain_burn + activity_impact[activity]))  # update brain burn score
        data.append({"timestamp": str(activity_start), "activity": activity})

        # Eye tracking test after each activity
        test_time = activity_start + timedelta(minutes=random.randint(5, 45))
        activity_start = test_time
        data.append({"timestamp": str(test_time), "activity": "eye_tracking_test", "score": brain_burn})

    # Saving data to a .txt file
    with open(f"data/{start_date.strftime('%Y-%m-%d')}_wellness_data.txt", "w") as outfile:
        for entry in data:
            json.dump(entry, outfile)
            outfile.write("\n")

if __name__ == "__main__":
    start_date = datetime.now()
    for _ in range(100):  # generate 100 days of data
        generate_data(start_date)
        start_date += timedelta(days=1)  # increment day
