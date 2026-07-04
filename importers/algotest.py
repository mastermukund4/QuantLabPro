from pathlib import Path
import pandas as pd


class AlgoTestImporter:

    def __init__(self, filepath):
        self.filepath = Path(filepath)

    def load(self):
        """
        Reads an AlgoTest CSV file and returns a pandas DataFrame.
        """

        if not self.filepath.exists():
            raise FileNotFoundError(
                f"File not found: {self.filepath}"
            )

        df = pd.read_csv(self.filepath)

        return df