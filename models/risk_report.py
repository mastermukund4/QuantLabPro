from dataclasses import dataclass


@dataclass
class RiskReport:

    standard_deviation: float

    downside_deviation: float

    sharpe_ratio: float

    sortino_ratio: float

    calmar_ratio: float

    ulcer_index: float

    recovery_factor: float

    value_at_risk_95: float

    conditional_var_95: float

    kelly_percent: float

    half_kelly_percent: float