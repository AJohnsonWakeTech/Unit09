from changedoc.full_retirement_calc import full_retirement_age, full_retirement_date, EARLIEST_YEAR, CURRENT_YEAR


def calculator():
    print("Social Security Full Retirement Age Calculator")
    year_valid = False
    birth_year_str = "Invalid"
    birth_year = -1
    while not year_valid:
        birth_year_str = str(input("Enter the year of birth or <enter> to exit ")).strip()
        if birth_year_str.isdigit() or birth_year_str == '':
            if birth_year_str.isdigit():
                birth_year = int(birth_year_str)
                if EARLIEST_YEAR <= birth_year < CURRENT_YEAR:
                    year_valid = True
                else:
                    print("Enter a year between 1900 and " + str(CURRENT_YEAR))
            else:
                year_valid = True
        else:
            print("Enter a whole number for the year.")
    while birth_year_str != '':
        birth_year = int(birth_year_str)
        month_valid = False
        birth_month = -1
        while not month_valid:
            birth_month_str = str(input("Enter the month of birth (<Enter> implies 0)"))
            if birth_month_str.isdigit():
                birth_month = int(birth_month_str)
                if 1 <= birth_month <= 12:
                    month_valid = True
                else:
                    print("Enter a whole number for the month from 1 to 12.")
            else:
                print("Enter a whole number for the month from 1 to 12.")
        fra_age_years, fra_age_months = full_retirement_age(birth_year)
        fra_date_year, fra_date_month = full_retirement_date(birth_year, birth_month)
        print("Your full retirement age is ", fra_age_years, " and ", fra_age_months, " months")
        print("This will be in ", fra_date_month, " of ", fra_date_year, "\n")
        birth_year_str = input("Enter the year of birth or <enter> to exit ")


def main():
    calculator()


main()

