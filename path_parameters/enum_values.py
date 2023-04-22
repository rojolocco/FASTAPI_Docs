# Imports
from enum import Enum


# Predifined string values
class DaysOfTheWeek(str, Enum):
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"


# Predifined int values
class MonthOfYear(int, Enum):
    january = 1
    febraury = 2
    march = 3
    april = 4
    may = 5
    june = 6
    july = 7
    august = 8
    september = 9
    october = 10
    november = 11
    december = 12
