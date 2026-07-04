from importers.algotest import AlgoTestImporter

FILE_PATH = "data/raw/algotest/calendar_trade.csv"


def main():

    importer = AlgoTestImporter(FILE_PATH)

    df = importer.load()

    print("=" * 50)
    print("QuantLab Pro")
    print("=" * 50)

    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    print("\nFirst five rows:\n")

    print(df.head())


if __name__ == "__main__":
    main()