import pandas as pd


class DataCleaner:
    """
    Cleans and normalizes raw AlgoTest data before parsing.
    """

    def clean(self, df):

        # ----------------------------------------
        # Date Columns
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
        # Time Columns
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

        # ----------------------------------------
        # Numeric Columns
        # ----------------------------------------

        numeric_columns = [
            "Strike",
            "Qty",
            "Entry Price",
            "Exit Price",
            "P/L",
            "Vix"
        ]

        for col in numeric_columns:

            if col in df.columns:

                df[col] = pd.to_numeric(
                    df[col],
                    errors="coerce"
                )

        return df