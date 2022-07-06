def twice_as_old(dad_years_old, son_years_old): 
    for years in range(0, 100):
        if (dad_years_old + years) == 2 * (son_years_old + years):
            return years
        elif (dad_years_old - years) == 2 * (son_years_old - years):
            return years
