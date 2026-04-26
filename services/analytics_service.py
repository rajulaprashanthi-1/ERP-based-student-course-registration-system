import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.data_store import students, courses

def analytics():
    if not students:
        print("No data")
        return

    credits = np.array([s.credits for s in students.values()])
    print("Average Credits:", np.mean(credits))

    df = pd.DataFrame({
        "Course": [c.title for c in courses.values()],
        "Enrollments": [c.enrolled for c in courses.values()]
    })

    print(df)

    plt.figure()
    plt.bar(df["Course"], df["Enrollments"])
    plt.title("Enrollments")
    plt.xticks(rotation=45)
    plt.show()