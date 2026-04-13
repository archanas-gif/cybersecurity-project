import pandas as pd
import numpy as np

def load_data():
    np.random.seed(42)

    # Normal traffic
    normal = np.random.normal(loc=50, scale=10, size=(100, 2))

    # Anomalies (attacks)
    anomalies = np.random.uniform(low=100, high=200, size=(10, 2))

    data = np.vstack([normal, anomalies])

    df = pd.DataFrame(data, columns=["packets", "duration"])

    print("Realistic Data Loaded ✅")
    return df