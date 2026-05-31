import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from evaluate import print_report

FEATURE_COLUMNS = [
    "sepal_length_cm",
    "sepal_width_cm",
    "petal_length_cm",
    "petal_width_cm",
]


def main():
    dataset_path = "iris.csv"
    try:
        df = pd.read_csv(dataset_path)
    except FileNotFoundError:
        print(f"Error: Could not find '{dataset_path}'. Please run 'prepare_data.py' first.")
        return

    X = df[FEATURE_COLUMNS]
    y = df["species"]
    labels = sorted(y.unique())

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    print_report(y_test, y_pred, labels)

    while True:
        try:
            print("Enter flower measurements to predict the species (or type 'exit' to quit):")
            val = input("Sepal Length (cm): ").strip()
            if val.lower() == "exit":
                break
            sepal_length = float(val)

            val = input("Sepal Width (cm): ").strip()
            if val.lower() == "exit":
                break
            sepal_width = float(val)

            val = input("Petal Length (cm): ").strip()
            if val.lower() == "exit":
                break
            petal_length = float(val)

            val = input("Petal Width (cm): ").strip()
            if val.lower() == "exit":
                break
            petal_width = float(val)

            new_flower = pd.DataFrame(
                [[sepal_length, sepal_width, petal_length, petal_width]],
                columns=FEATURE_COLUMNS,
            )
            new_scaled = scaler.transform(new_flower)
            prediction = model.predict(new_scaled)
            print(f"\nPredicted Species: {prediction[0].upper()}")
            print("-" * 30)
        except ValueError:
            print("Invalid input. Please enter numerical values (e.g. 5.1).")


if __name__ == "__main__":
    main()
