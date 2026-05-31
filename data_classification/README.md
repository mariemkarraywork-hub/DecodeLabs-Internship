# P2 — Data Classification (Iris KNN)

Supervised learning pipeline: scale features, train KNN, evaluate, predict.

## Run

```powershell
cd C:\Users\karra\.gemini\antigravity\scratch\IA\data_classification
pip install pandas scikit-learn
python prepare_data.py
python tune_k.py
python classify.py
```

Browser demo: open `chatbot.html`

## Files

| File | Role |
|------|------|
| `prepare_data.py` | Creates `iris.csv` |
| `classify.py` | Train, report, interactive predict |
| `tune_k.py` | K optimization loop |
| `evaluate.py` | Confusion matrix + metrics |
| `chatbot.html` | Browser demo |

## Walkthrough

Full guide: [../walkthrough/walkthrough2.md](../walkthrough/walkthrough2.md)
