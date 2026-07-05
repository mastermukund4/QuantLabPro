from pathlib import Path
import pandas as pd


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

        df = pd.read_csv(self.filepath)

        # ----------------------------------------
        # Convert Date Columns
        # ----------------------------------------

        date_columns = [
            "Entry Date",
            "Exit Date"
        ]

        for col in date_columns:

            if col in df.columns:

                df[col] = pd.to_datetime(
                    df[col],
                    errors="coerce"
                ).dt.date

        # ----------------------------------------
        # Convert Time Columns
        # Supports:
        # 09:20:00 AM
        # 15:20:00
        # ----------------------------------------

        time_columns = [
            "Entry Time",
            "Exit Time"
        ]

        for col in time_columns:

            if col in df.columns:

                df[col] = pd.to_datetime(
                    df[col],
                    format="mixed",
                    errors="coerce"
                ).dt.time

        return df