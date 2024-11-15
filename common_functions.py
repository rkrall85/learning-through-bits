
# Function to determine the current level, days until the next level, and the next level
def get_level_info(days, levels, names):
    for i in range(len(levels) - 1):
        if levels[i] <= days < levels[i + 1]:
            current_level = names[i]
            days_to_next = levels[i + 1] - days
            next_level = names[i + 1] if i < len(names) else None
            return current_level, days_to_next, next_level
    # If days are beyond the last threshold
    return names[-1], 0


def get_column_names():
    tab_cruise_data_column_names = {
        0: 'Booking #', 1: 'Cruise Date', 2: 'Year', 3: 'Month', 4: 'Brand', 5: 'Ship', 6: 'Itinerary', 7: 'Itinerary Category',
        8: 'Home Port', 9: 'Class', 10: 'Days',
        11: 'Room #', 12: 'Floor',  13: 'Type', 14: 'Rank', 15: 'Category', 16: 'Grouping',
        17: 'Cruise Amount', 18: 'Gratuities', 19: 'Room Price',
        20: 'Room Price Per Day', 21: 'Cruise Amount Per Day',
        22: 'Airfare', 23: 'Drink Package', 24: 'Total Cruise Amount',
        25: 'Costco Rebate', 26: 'Shareholder', 27: 'OBC', 28: 'AARP Rebate', 29: 'Total Savings', 30: 'Final Cruise Price',
        31: 'Ports', 32: 'Excursions', 33: 'Notes', 34: 'Who Went', 35: "Room Classification"
    }
    output_dict = {
        "tab_cruise_data_column_names": tab_cruise_data_column_names,
    }

    return output_dict