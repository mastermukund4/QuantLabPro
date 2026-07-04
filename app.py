from importers.algotest import AlgoTestImporter

FILE_PATH = "data/raw/algotest/calendar_trade.csv"

def main():

    print("=" * 60)
    print("QuantLab Pro")
    print("=" * 60)

    importer = AlgoTestImporter(FILE_PATH)

    df = importer.load()

    print("\nFile imported successfully!")

if __name__ == "__main__":
    main()