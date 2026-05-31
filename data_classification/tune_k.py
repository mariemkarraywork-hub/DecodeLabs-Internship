import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

FEATURE_COLUMNS = [
    "sepal_length_cm",
    "sepal_width_cm",
    "petal_length_cm",
    "petal_width_cm",
]


def main():
    try:
        df = pd.read_csv("iris.csv")
    except FileNotFoundError:
        print("Error: Could not find 'iris.csv'. Please run 'prepare_data.py' first.")
        return

    X = df[FEATURE_COLUMNS]
    y = df["species"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("\nK Optimization (error rate vs K)")
    print("-" * 40)
    print(f"{'K':>4} {'Accuracy':>10} {'Error Rate':>12}")
    print("-" * 40)

    best_k = 5
    best_accuracy = 0.0

    for k in range(1, 21):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        acc = accuracy_score(y_test, y_pred)
        error = 1 - acc
        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k
        print(f"{k:4d} {acc * 100:9.1f}% {error * 100:11.1f}%")

    print("-" * 40)
    print(f"Best K in range 1-20: {best_k} (accuracy {best_accuracy * 100:.1f}%)")
    print("Look for the elbow where error stops dropping sharply.\n")


if __name__ == "__main__":
    main()
