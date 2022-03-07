def my_datetime(num_sec):
    """Takes in an integer value that represents the number of seconds since the epoch (January 1st, 1970)"""

    def leap_year(years):
        """Tests if the month is a leap year or not by using mod, a leap year is every 4 years, if the year is
         divisible by 100 and not divisible by 400"""
        if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
            return years

    def days_into_months(years, months):
        """Adds an extra day to account for leap year in February and otherwise returns days"""
        days_from_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # 12 months and how many days in each month, using 0 as month 0 to offset the range
        used_day = days_from_months[months]
        if leap_year(years) and months == 2:
            return used_day + 1
        else:
            return used_day

    num_days = num_sec // (24*60*60)
    # uses floor division for the largest value when multiplying 24 hours in a day, 60 minutes in an hour, and 60
    # seconds in 1 hour
    used_month = 1
    used_day = 1
    used_year = 1970
    # starting values from the epoch (January 1st, 1970)

    while num_days > 0:
        # while loop from num_days which is given from num_sec divided by hours, minutes, and seconds and
        # continuously subtracts num_days and adding a used_day everytime the loop continues
        num_days -= 1
        used_day += 1
        if used_day > days_into_months(used_year, used_month):
            # checks the starting day from the epoch and compares if its greater than the amount of days in a month
            # resets used_days back to 1 if its greater and sets used_months to +1 than it previously was and goes
            # to the next if statement
            used_day = 1
            used_month += 1
            if used_month > 12:
                # used_month cant be greater than 12 months since their are only 12 months in a year so it adds 1 to
                # year and changes used_months back to 1 to continue the while loop
                used_month = 1
                used_year += 1
    used_day = str(used_day)
    used_month = str(used_month)
    used_year = str(used_year)
    dash = "-"
    month_date_time = used_month + dash + used_day + dash + used_year
    month_date_time = int(month_date_time)
    return month_date_time
