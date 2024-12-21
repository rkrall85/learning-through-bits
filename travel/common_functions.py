import os
import pandas as pd


def get_level_info(days, levels, names):
    # Function to determine the current level, days until the next level, and the next level
    for i in range(len(levels) - 1):
        if levels[i] <= days < levels[i + 1]:
            current_level = names[i]
            days_to_next = levels[i + 1] - days
            next_level = names[i + 1] if i < len(names) else None
            return current_level, days_to_next, next_level
    # If days are beyond the last threshold
    return names[-1], 0


def get_column_names():
    """
    Getting column names from sheets
    :return: dict of column names
    :rtype: dict
    """
    tab_cruise_data_column_names = {
        0: 'Booking #', 1: 'Cruise Date', 2: 'Year', 3: 'Month', 4: 'Brand', 5: 'Ship',
        6: 'Itinerary', 7: 'Itinerary Category',
        8: 'Port', 9: 'Class', 10: 'Days',
        11: 'Room #', 12: 'Floor', 13: 'Room Type', 14: 'Room Rank', 15: 'Room Category', 16: 'Room Classification',
        17: 'Cruise Amount', 18: 'Cruise Amount Minus Savings', 19: 'Daily Person Costs',
        20: 'Gratuities', 21: 'Airfare', 22: 'Drink Package', 23: 'Drink Package/Day', 24: 'Total Cruise Amount',
        25: 'Costco Rebate', 26: 'Shareholder', 27: 'OBC', 28: 'AARP Rebate', 29: 'Total Savings',
        30: 'Final Trip Price',
        31: 'Ports', 32: 'Excursions', 33: 'Notes', 34: 'Who Went', 35: 'Who Went Count', 36: 'Number of Ports'
    }

    tab_cpi_column_names = {
        0: 'Year', 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',
        6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }

    output_dict = {
        "tab_cruise_data_column_names": tab_cruise_data_column_names,
        "tab_cpi_column_names": tab_cpi_column_names
    }

    return output_dict


def get_pricing_list():
    pricing_agg = {
        "Itinerary": ["Itinerary Category"],
        "Ship": ["Ship"],
        "Port": ["Port"],
        "Room Type": ["Room Type"],
        "Room Classification": ["Room Classification"],

        "ship_by_room": ["Ship", "Room Type"],
        "ship_by_room_classification": ["Ship", "Room Classification"],
        "ship_by_month": ["Ship", "Month"],
        "ship_by_itinerary": ["Ship", "Itinerary Category"],
        "ship_by_room_ports": ["Ship", "Room Type", "Number of Ports"],

        "ship_by_month_itinerary": ["Ship", "Month", "Itinerary Category"],
        "ship_by_month_room": ["Ship", "Month", "Room Type"],
        "ship_by_month_room_classification": ["Ship", "Month", "Room Classification"],
        "ship_by_month_floor_room": ["Ship", "Month", "Floor", 'Room Type'],

        "class_by_room_classification": ['Class', 'Room Classification'],
        "class_by_room_type": ['Ship', 'Room Type'],


        "floor_by_room": ["Floor", "Room Type"],
        "floor_by_room_classification": ["Floor", "Room Classification"],

        "month_by_room_type": ["Month", "Room Type"],
        "month_by_room_Classification": ["Month", "Room Classification"],
        "month_by_floor": ["Month", "Floor"],
        "month_by_port": ["Month", "Port"],
        "month_by_room_num_ports": ['Month', 'Room Type', 'Number of Ports'],

        "itinerary_by_ship_room_type": ["Itinerary Category", "Ship", "Room Type"],
        "itinerary_by_ship_room_classification": ["Itinerary Category", "Ship", "Room Classification"],
        "itinerary_by_port": ["Itinerary Category", "Port"],
        "itinerary_by_month": ["Itinerary Category", "Month"],
        "itinerary_by_room_type": ["Itinerary Category", "Room Type"],
        "itinerary_by_room_classification": ["Itinerary Category", "Room Classification"],

        
        "room_type_by_port_floor_itinerary": ["Room Type", "Port", "Floor", "Itinerary Category"],
        "room_type_by_itinerary_by_day": ["Room Type", "Itinerary Category", "Days"],
        "room_type_by_itinerary_by_month": ["Room Type", "Itinerary Category", "Month"],

        "port_ship_room": ["Port", "Ship", "Room Type"],
        "port_ship_month": ["Port", "Ship", "Month"],
        "port_ship_room_month": ["Port",  "Ship", "Room Type", "Month"],

       
    }
    return pricing_agg



def get_booking_price_breakdown(booking_dict, pricing_breakdown):

    booking_row = 0
    booking_price = booking_dict['Price']
    booking_obc = booking_dict['OBC']
    booking_costco_rebate = booking_dict['Costco Rebate']
    booking_aarp_discount = booking_dict['AARP Discount']
    booking_days = booking_dict['Days']
    booking_travelers = booking_dict['Travelers']

    # Get shareholder credits
    if booking_days <= 4:
        booking_shareholder = 50
    elif 4 < booking_days <= 10:
        booking_shareholder = 100
    else:
        booking_shareholder = 250

    aarp_discount = 0
    # ticket(5) add logic after 12/21/24 then its 5%; after 07/05/2024 its 8% otherwise 10%
    if booking_aarp_discount:
        aarp_discount = booking_price * .08
    else:
        if booking_costco_rebate > 0:
            booking_costco_rebate = booking_costco_rebate + (booking_price*.05)

    booking_savings = (booking_shareholder + booking_obc + booking_costco_rebate + aarp_discount)
    booking_price_with_savings = booking_price - booking_savings
    booking_price_per_person = booking_price_with_savings/booking_days/booking_travelers

    booking_pricing = {}
    df_columns = ['Pricing By', 'Pricing Filter', 'Pricing Category', 'Min', 'Mean', 'Max', 'Mock Booking']
    booking_report = pd.DataFrame(
        columns=df_columns,
        # index=range(len(booking_pricing)*4)
    )

    for p in pricing_breakdown:
        agg_data = pricing_breakdown[p]['data_agg']
        prim_agg = agg_data[0]
        prim_booking = booking_dict[prim_agg]

        # Create a list to hold the bookings
        bookings = [prim_booking]

        # Loop through the remaining items in agg_data (if any) and add to the bookings list
        for i in range(1, len(agg_data)):
            bookings.append(booking_dict[agg_data[i]])

        # Convert the list to a tuple (if needed) for pricing_filter
        pricing_filter = tuple(bookings) if len(bookings) > 1 else bookings[0]

        agg_breakdown = ['daily_person_costs']

        booking_pricing[f'Price By {prim_agg}'] = {}
        for a_id, a in enumerate(agg_breakdown):
            temp_df = pd.DataFrame(
                columns=df_columns,
                index=range(1)
            )

            df_1 = pricing_breakdown[p]['price_breakdown'][a]
            index = df_1.index.values
            index_list = df_1.index.tolist()
            if pricing_filter in index_list:
                df_filtered = df_1[df_1.index.isin([pricing_filter])]
                temp_df['Pricing By'] = p
                temp_df['Pricing Filter'] = str(pricing_filter)
                filter_data = df_filtered.loc[pricing_filter]
                temp_df['Min'] = filter_data['min']
                temp_df['Max'] = filter_data['max']
                temp_df['Mean'] = filter_data['mean']

                if a == 'daily_person_costs':
                    temp_df['Pricing Category'] = 'Price/Day/Person'
                    temp_df['Mock Booking'] = booking_price_per_person

                '''
                if a == 'cruise_amount':
                    temp_df['Pricing Category'] = 'Cruise Price'
                    temp_df['Mock Booking'] = booking_price
                el'''


                row_list = temp_df.loc[0, :].values.flatten().tolist()
                booking_report.loc[booking_row] = row_list
                booking_row = booking_row + 1

    return booking_report
