# Data Classification — Simple Walkthrough

Train a machine to guess Iris flower species from 4 measurements. No if-else rules — the model learns from past data.

---

## What each file does

| File | What it does | Command |
|------|--------------|---------|
| `prepare_data.py` | Creates `iris.csv` | `python prepare_data.py` |
| `tune_k.py` | Tests different K values | `python tune_k.py` |
| `classify.py` | Trains model, prints report, lets you predict | `python classify.py` |
| `evaluate.py` | Prints metrics (used by `classify.py`) | runs automatically |
| `chatbot.html` | Browser demo (optional) | open in browser |

---

## How it works (3 steps — IPO)

**1. INPUT** — Load data, split 80% train / 20% test, scale numbers so all features are fair.

**2. PROCESS** — Train KNN (K=5). It finds the 5 closest flowers and votes on the species.

**3. OUTPUT** — Print accuracy, confusion matrix, precision, recall, F1. Then you can type measurements and get a prediction.

```
INPUT          →    PROCESS         →    OUTPUT
load + scale        train KNN            metrics + predict
```

---

## Commands to run

Open PowerShell:

```powershell
cd C:\Users\karra\.gemini\antigravity\scratch\IA\data_classification
```

Install once (if needed):

```powershell
pip install pandas scikit-learn
```

Run in this order:

```powershell
python prepare_data.py
python tune_k.py
python classify.py
```

Optional browser demo:

```powershell
Start-Process .\chatbot.html
```

Type `exit` to quit the prediction loop in `classify.py`.

---

## The dataset

150 flowers. Each row has 4 numbers + 1 species name.

| Column | What it is |
|--------|------------|
| `sepal_length_cm` | Sepal length |
| `sepal_width_cm` | Sepal width |
| `petal_length_cm` | Petal length |
| `petal_width_cm` | Petal width |
| `species` | setosa, versicolor, or virginica |

50 flowers per species.

---

## What happens in each script

### `prepare_data.py`
- Downloads Iris data from scikit-learn (works offline)
- Saves it as `iris.csv`
- Run this first. Run again if you delete `iris.csv`.

### `tune_k.py`
- Tries K = 1, 2, 3 … up to 20
- Prints accuracy and error rate for each K
- Helps you see if K=5 is a good choice
- **K=1** = too sensitive | **K=5** = our default | **K too high** = too vague

### `classify.py` (main file)
1. Loads `iris.csv`
2. Splits: 120 rows to learn, 30 rows to test
3. Scales features with `StandardScaler` (so petal length does not overpower petal width)
4. Trains `KNeighborsClassifier(n_neighbors=5)`
5. Prints the full report (from `evaluate.py`)
6. Asks you for 4 measurements and predicts the species

Example:

```
Sepal Length (cm): 5.1
Sepal Width (cm): 3.5
Petal Length (cm): 1.4
Petal Width (cm): 0.2

Predicted Species: SETOSA
```

### `evaluate.py`
Runs inside `classify.py`. You do not run it separately.

**Simple meanings:**

| Term | Plain English |
|------|---------------|
| **Accuracy** | How many guesses were correct overall |
| **Confusion matrix** | Table showing correct vs wrong guesses per species |
| **Precision** | When the model says "versicolor", how often is it right? |
| **Recall** | Of all real versicolor flowers, how many did we catch? |
| **F1-Score** | Balance between precision and recall |
| **TP** | Correct positive guess |
| **FP** | Wrong alarm (said yes, but was no) |
| **FN** | Missed detection (said no, but was yes) |
| **TN** | Correct negative guess |

---

## Test values (copy these in classify.py)

| Measurements (SL / SW / PL / PW) | Should predict |
|----------------------------------|----------------|
| 5.1 / 3.5 / 1.4 / 0.2 | setosa |
| 6.0 / 2.9 / 4.5 / 1.5 | versicolor |
| 6.3 / 3.3 / 6.0 / 2.5 | virginica |

---

## Folder layout

```
data_classification/
├── prepare_data.py
├── classify.py
├── tune_k.py
├── evaluate.py
├── iris.csv
├── chatbot.html
└── ../walkthrough/walkthrough2.md
```

---

## P2 checklist (what your project covers)

| Required | Done in |
|----------|---------|
| Iris dataset | `prepare_data.py` |
| StandardScaler | `classify.py` |
| 80/20 split | `classify.py` |
| KNN with K=5 | `classify.py` |
| fit → predict | `classify.py` |
| K tuning loop | `tune_k.py` |
| Confusion matrix + metrics | `evaluate.py` |
| Live predictions | `classify.py` |

---

## Ideas to level up later

Easy first, harder later:

1. **Plot K vs error** — add a chart in `tune_k.py` with matplotlib
2. **Save the model** — use `joblib.dump()` so you do not retrain every time
3. **Flask API** — connect `chatbot.html` to the real Python model
4. **Try other algorithms** — Decision Tree, Random Forest, compare scores
5. **Auto-tune K** — use `GridSearchCV` instead of a manual loop

---

## If something breaks

| Problem | Fix |
|---------|-----|
| Missing `iris.csv` | `python prepare_data.py` |
| `No module named sklearn` | `pip install scikit-learn pandas` |
| Bad input error | Use numbers like `5.1`, not text |
| 100% accuracy | Normal on Iris — the dataset is easy |
| chatbot ≠ Python result | HTML uses its own logic; use `classify.py` for the real project |

---

## Quick viva script (30 seconds)

> "I load the Iris dataset, scale features, split 80/20, train KNN with K=5, evaluate with precision/recall/F1, then predict new flowers interactively. K tuning is in a separate script."

That is the whole project in one sentence.
