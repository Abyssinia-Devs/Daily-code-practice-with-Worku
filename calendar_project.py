# --- Constants
JDN_ETHIOPIAN_EPOCH = 1723856
GREGORIAN_MONTHS = [
    "", "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
ETHIOPIAN_MONTH_ABBREVIATIONS = [
        "","መስከረም", "ጥቅምት", "ህዳር", 
        "ታህሳስ", "ጥር", "የካቲት",
        "መጋቢት", "ምያዚያ", "ግንቦት", 
        "ሰኔ", "ሃምሌ", "ነሃሴ", "ጳጉሜ"
]

WEEKDAY_ABBREVIATIONS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# --- Helper Functions: Leap Years & Days in Month ---

def is_gregorian_leap(year):
    """
    Returns True if year is a leap year according to Gregorian rules.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_julian_leap(year):
    """
    Returns True if year is a leap year according to Julian rules.
    """
    return year % 4 == 0

def get_days_in_g_month(year, month):
    """
    Returns the number of days in a specific Gregorian/Julian month.
    Handles the 1752 switch explicitly.
    """
    # 30 days hath September... logic
    if month in [4, 6, 9, 11]:
        days = 30
    elif month == 2:
        # Check leap year rules based on history
        if year > 1752:
            days = 29 if is_gregorian_leap(year) else 28
        elif year < 1752:
            days = 29 if is_julian_leap(year) else 28
        else: # Year 1752
            days = 29 # 1752 was a leap year in the Julian calendar (transition happened in Sept)
    else:
        days = 31

    # SPECIAL CASE: September 1752  
    # Sept 1752 had only 19 days.
    if year == 1752 and month == 9:
        return 19 
    
    return days

# -- Ethiopian Conversion ---

def to_ethiopian(g_year, g_month, g_day):
    """
    Converts a Gregorian/Julian date to Ethiopian Date.
    Uses Julian Day Number (JDN) as the common bridge.
    """
    # 1. Calculate JDN (Julian Day Number)
    # Algorithm based on Meeus for Gregorian/Julian switch
    y = g_year
    m = g_month
    d = g_day

    # Adjust months for algorithm (Jan/Feb become 13/14 of previous year)
    if m <= 2:
        y -= 1
        m += 12

    
    # Calculate A and B for Gregorian reform adjustment
    is_gregorian = False
    if g_year > 1752:
        is_gregorian = True
    elif g_year == 1752:
        if g_month > 9: is_gregorian = True
        elif g_month == 9 and g_day >= 14: is_gregorian = True
    
    if is_gregorian:
        A = y // 100
        B = 2 - A + (A // 4)
    else:
        B = 0 # Julian Calendar has no correction B

    jdn = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + d + B - 1524

    # 2. Convert JDN to Ethiopian
    JD_eth = jdn - JDN_ETHIOPIAN_EPOCH
    
    # Ethiopian arithmetic
    r = (JD_eth % 1461)
    n = (r % 365) + 365 * (r // 1460)
    
    e_year = 4 * ((JD_eth - 1) // 1461) + (r // 365) - (r // 1460)
    e_month = (n // 30) + 1
    e_day = (n % 30) + 1
    
    return e_year, e_month, e_day

# --- Day of Week ---

def get_start_day_of_week(year, month):
    """
    Returns 0=Sun, 1=Mon, ..., 6=Sat for the 1st of the month.
    """
    y = year
    m = month
    d = 1
    
    if m <= 2:
        y -= 1
        m += 12
        
    is_gregorian = False
    if year > 1752:
        is_gregorian = True
    elif year == 1752:
        if month > 9: is_gregorian = True
        elif month == 9 and 1 >= 14: is_gregorian = True # 1st is never >= 14
    
    if is_gregorian:
        A = y // 100
        B = 2 - A + (A // 4)
    else:
        B = 0

    jdn = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + d + B - 1524
    dow = (jdn + 1) % 7
    return dow

# --- Display ---

def print_month(year, month):
    print(f"\n{GREGORIAN_MONTHS[month]}")
    
    # Find start and end Ethiopian months for the header
    start_eth = to_ethiopian(year, month, 1)
    # Find last day of this month
    last_day_g = get_days_in_g_month(year, month)
    
    # Handle the 1752 Sep edge case for end date
    last_day_actual = last_day_g
    if year == 1752 and month == 9:
        last_day_actual = 30 # The loop logic handles the jump, but we need the date for conversion
    
    end_eth = to_ethiopian(year, month, last_day_actual)
    
    eth_month_str = ETHIOPIAN_MONTH_ABBREVIATIONS[start_eth[1]]
    if start_eth[1] != end_eth[1]:
        eth_month_str += f"-{ETHIOPIAN_MONTH_ABBREVIATIONS[end_eth[1]]}"
        
    print(f"{eth_month_str}")
    
    # Print Border
    print("-" * 64)
    # Print Days Header
    header = "|"
    for day in WEEKDAY_ABBREVIATIONS:
        header += f"{day:<8}|"
    print(header)
    print("-" * 64)

    # Get start day of week (0=Sun, ... 6=Sat)
    start_dow = get_start_day_of_week(year, month)
    
    days_in_m = get_days_in_g_month(year, month)
    
    # Prepare Grid Data
    cells = []
    
    for _ in range(start_dow):
        cells.append(None)
        
    # Logic for Sept 1752 specific loop
    if year == 1752 and month == 9:
        range_days = [1, 2] + list(range(14, 31))
    else:
        range_days = range(1, days_in_m + 1)
        
    for d in range_days:
        ey, em, ed = to_ethiopian(year, month, d)
        cells.append((d, ed))
        
    while len(cells) % 7 != 0:
        cells.append(None)
        
    # PRINTING THE GRID
    total_weeks = len(cells) // 7
    
    for w in range(total_weeks):
        week_data = cells[w*7 : (w+1)*7]
        
        # Line 1: Gregorian (Top)
        line_g = "|"
        for cell in week_data:
            if cell:
                line_g += f"    {str(cell[0]):>4}|" # Right aligned top
            else:
                line_g += "        |"
        print(line_g)
        
        # Line 2: Ethiopian (Bottom)
        line_e = "|"
        for cell in week_data:
            if cell:
                line_e += f"{str(cell[1]):<4}    |" # Left aligned top
            else:
                line_e += "        |"
        print(line_e)
        
        # line_e = "|"
        # for cell in week_data:
        #     if cell:
        #         line_e += f"    {str(cell[1]):<4}|" # Left aligned bottom
        #     else:
        #         line_e += "        |"
        # print(line_e)
        
        print("-" * 64)

def print_calendar_program():
    print("Program to Display Gregorian/Julian and Ethiopian Calendar")
    
    while True:
        try:
            user_input = input("Enter a year (Julian or Gregorian) [or 'q' to quit]: ")
            if user_input.lower() == 'q':
                break
                
            year = int(user_input)
            
            if year < 1:
                print("Please enter a year greater than 0.")
                continue

            start_eth_y = to_ethiopian(year, 1, 1)[0]
            end_eth_y = to_ethiopian(year, 12, 31)[0]
            
            print(f"\nGregorian Year: {year}\tEthiopian Years: {start_eth_y} - {end_eth_y}")
            
            for m in range(1, 13):
                print_month(year, m)
                
            
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print_calendar_program()