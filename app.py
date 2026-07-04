from models.trade import Trade


def main():

    trade = Trade(
        trade_id="1",

        strategy="Calendar",

        symbol="NIFTY",

        expiry_type="Weekly",

        entry_date="03-Jul-2025",
        entry_time="09:16",

        exit_date="03-Jul-2025",
        exit_time="15:27",

        pnl=1284.75,

        vix=14.6,

        number_of_legs=2
    )

    print(trade)


if __name__ == "__main__":
    main()