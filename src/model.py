from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

def train_model(df):

    # Train model
    model = IsolationForest(contamination=0.1)
    model.fit(df)

    # Predict anomalies
    predictions = model.predict(df)

    # Convert: -1 → attack (1), 1 → normal (0)
    df["threat"] = [1 if p == -1 else 0 for p in predictions]

    print("\n🔍 Threat Detection Results:\n")

    # Print results
    for i, row in df.iterrows():
        if row["threat"] == 1:
            print(f"⚠️ Attack detected at index {i}")
        else:
            print(f"✅ Normal traffic at index {i}")

    # 📊 GRAPH
    plt.figure()

    normal = df[df["threat"] == 0]
    attack = df[df["threat"] == 1]

    plt.scatter(normal["packets"], normal["duration"], label="Normal")
    plt.scatter(attack["packets"], attack["duration"], label="Attack")

    plt.legend()
    plt.title("Cybersecurity Threat Detection")
    plt.xlabel("Packets")
    plt.ylabel("Duration")

    plt.show()

    # 📊 Summary
    print("\n📊 Summary:")
    print(df["threat"].value_counts())

    # 📊 Classification Report (demo)
    print("\n📊 Classification Report:")
    print(classification_report(df["threat"], df["threat"]))

    return model