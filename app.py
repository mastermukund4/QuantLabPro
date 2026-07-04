from services.trade_service import TradeService

FILE_PATH = "data/raw/algotest/calendar_trade.csv"


def main():

    service = TradeService(FILE_PATH)

    service.run()


if __name__ == "__main__":
    main()