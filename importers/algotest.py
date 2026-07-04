from pathlib import Path
import pandas as pd


class AlgoTestImporter:

    def __init__(self, filepath):
        self.filepath = Path(filepath)

    def load(self):

        if not self.filepath.exists():
            raise FileNotFoundError(
                f"File not found: {self.filepath}"
            )

        print("=" * 60)
        print("Loading AlgoTest File...")
        print("=" * 60)

        df = pd.read_csv(self.filepath)

        print(f"Rows Loaded    : {len(df)}")
        print(f"Columns Loaded : {len(df.columns)}")

        print("\nColumns:")

        for col in df.columns:
            print(f" • {col}")

        print("\nPreview:\n")

        print(df.head())

        return df