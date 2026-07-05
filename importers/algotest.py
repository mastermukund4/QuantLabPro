from pathlib import Path

import pandas as pd

from cleaners.data_cleaner import DataCleaner


class AlgoTestImporter:

    def __init__(self, filepath):
        self.filepath = Path(filepath)

    def load(self):
        """
        Reads an AlgoTest CSV file and returns
        a cleaned pandas DataFrame.
        """

        if not self.filepath.exists():

            raise FileNotFoundError(
                f"File not found: {self.filepath}"
            )

        # Read CSV
        df = pd.read_csv(self.filepath)

        # Clean Data
        cleaner = DataCleaner()

        df = cleaner.clean(df)

        return df