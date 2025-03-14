from enum import Enum, unique
from typing import Dict


@unique
class CountryCode(Enum):
    DE = "DE"
    FR = "FR"
    GB = "GB"
    NL = "NL"


@unique
class Granularity(Enum):
    HOURLY = "h"
    HALF_HOURLY = "hh"


countryCodeMeanPrices: Dict[CountryCode, int] = {
    CountryCode.DE: 57,
    CountryCode.FR: 58,
    CountryCode.GB: 61,
    CountryCode.NL: 52,
}
