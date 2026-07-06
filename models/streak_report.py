from dataclasses import dataclass


@dataclass
class StreakStats:

    streak_type: str

    length: int

    pnl: float


@dataclass
class StreakReport:

    longest_winning_streak: int

    longest_losing_streak: int

    average_winning_streak: float

    average_losing_streak: float

    total_winning_streaks: int

    total_losing_streaks: int

    current_streak_type: str

    current_streak_length: int

    largest_winning_streak_pnl: float

    largest_losing_streak_pnl: float

    streaks: list[StreakStats]