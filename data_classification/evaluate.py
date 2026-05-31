from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
)


def print_report(y_test, y_pred, labels):
    print("\n" + "=" * 50)
    print("DIAGNOSTIC REPORT")
    print("=" * 50)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {accuracy * 100:.1f}%")

    cm = confusion_matrix(y_test, y_pred, labels=labels)
    print("\nConfusion Matrix (rows = actual, columns = predicted):")
    header = " " * 12 + "  ".join(f"{label[:8]:>8}" for label in labels)
    print(header)
    for i, label in enumerate(labels):
        row = "  ".join(f"{value:8d}" for value in cm[i])
        print(f"{label[:12]:<12} {row}")

    print("\nPer-Class Breakdown (one-vs-rest):")
    print(f"{'Class':<12} {'TP':>6} {'FP':>6} {'FN':>6} {'TN':>6}")
    print("-" * 42)
    for i, label in enumerate(labels):
        tp = cm[i, i]
        fp = cm[:, i].sum() - tp
        fn = cm[i, :].sum() - tp
        tn = cm.sum() - tp - fp - fn
        print(f"{label:<12} {tp:6d} {fp:6d} {fn:6d} {tn:6d}")

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, y_pred, labels=labels, zero_division=0
    )
    print("\nMetrics:")
    print(f"{'Class':<12} {'Precision':>10} {'Recall':>10} {'F1-Score':>10}")
    print("-" * 44)
    for i, label in enumerate(labels):
        print(f"{label:<12} {precision[i]:10.3f} {recall[i]:10.3f} {f1[i]:10.3f}")

    print("\nSklearn Classification Report:")
    print(classification_report(y_test, y_pred, labels=labels, zero_division=0))

    avg_precision = precision.mean()
    avg_recall = recall.mean()
    print("Trade-off Summary:")
    if avg_precision > avg_recall + 0.05:
        print(
            "Precision is stronger than recall. The model is cautious — "
            "fewer wrong labels, but it may miss some true cases."
        )
    elif avg_recall > avg_precision + 0.05:
        print(
            "Recall is stronger than precision. The model catches more true cases, "
            "but may produce more false alarms."
        )
    else:
        print(
            "Precision and recall are balanced. The model is stable for this dataset."
        )

    weak = f1.argmin()
    print(
        f"Lowest F1: {labels[weak]} ({f1[weak]:.3f}). "
        f"This class has the most overlap with others."
    )
    print("=" * 50 + "\n")
