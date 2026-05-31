import pandas as pd
from sklearn.datasets import load_iris

def main():
    print("Fetching the Iris dataset...")
    iris = load_iris()

    df = pd.DataFrame(data=iris.data, columns=[
        'sepal_length_cm',
        'sepal_width_cm',
        'petal_length_cm',
        'petal_width_cm'
    ])

    species_names = [iris.target_names[target] for target in iris.target]
    df['species'] = species_names

    csv_filename = "iris.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Dataset successfully saved as '{csv_filename}' with {df.shape[0]} rows and {df.shape[1]} columns!")

if __name__ == "__main__":
    main()
