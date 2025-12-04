"""Train a simple scikit-learn regressor on the synthetic dataset and save the model.

Usage:
  python scripts/train_model.py --data data/synthetic/sample_synthetic.csv --output models/rf_model.joblib
"""
import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def load_data(path):
    df = pd.read_csv(path)
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    df = load_data(args.data)
    X = df[[c for c in df.columns if c not in ("shape_id", "yearly_energy_kwh")]].values
    y = df["yearly_energy_kwh"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    pred = model.predict(X_test[:2])
    print("Example predictions:", pred)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, out_path)
    print(f"Saved model to {out_path}")


if __name__ == "__main__":
    main()
