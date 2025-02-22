
def get_column_names():
    tab_cruise_data_column_names = {
        0: 'Booking #', 1: 'Cruise Date', 2: 'Year', 3: 'Month', 4: 'Brand', 5: 'Ship',
        6: 'Itinerary', 7: 'Itinerary Category',
        8: 'Port', 9: 'Class', 10: 'Days',
        11: 'Room #', 12: 'Floor', 13: 'Room Type', 14: 'Room Rank', 15: 'Room Category', 16: 'Room Classification',
        17: 'Cruise Amount', 18: 'Cruise Amount Minus Savings', 19: 'Daily Person Costs',
        20: 'Gratuities', 21: 'Airfare', 22: 'Drink Package', 23: 'Drink Package/Day', 24: 'Total Cruise Amount',
        25: 'Costco Rebate', 26: 'Shareholder', 27: 'OBC', 28: 'AARP Rebate', 29: 'Total Savings',
        30: 'Final Trip Price',
        31: 'Ports', 32: 'Excursions', 33: 'Notes', 34: 'Who Went', 35: 'Who Went Count', 36: 'Number of Ports',
        37: 'Boat Maiden Voyage', 38: 'Cruise Boat Age Bucket'
    }

    tab_cpi_column_names = {
        0: 'Year', 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',
        6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }

    tab_ship_data_column_names = {
        0: "Brand", 1: "Ship", 2: "Ship Class", 3: "Boat Maiden Voyage",  4: "Ship Age", 5:  "Size Category",
        6: "Ship Age Bucket", 7: "Previous Name", 8: "Size Ranking", 9: "Ship Class Rank"
    }

    output_dict = {
        "tab_cruise_data_column_names": tab_cruise_data_column_names,
        "tab_cpi_column_names": tab_cpi_column_names,
        "tab_ship_data_column_names": tab_ship_data_column_names
    }

    return output_dict