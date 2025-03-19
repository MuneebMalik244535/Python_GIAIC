# seconds = 365 * 24 * 60 * 60
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def Calculation():
    second = DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    print(f"There are {second} in One Year")

if __name__ == "__main__":
    Calculation()    
    