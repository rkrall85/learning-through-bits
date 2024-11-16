import os;
import pandas as pd;


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
        0: 'Booking #', 1: 'Cruise Date', 2: 'Year', 3: 'Month', 4: 'Brand', 5: 'Ship', 6: 'Itinerary',
        7: 'Itinerary Category',
        8: 'Port', 9: 'Class', 10: 'Days',
        11: 'Room #', 12: 'Floor', 13: 'Type', 14: 'Rank', 15: 'Category', 16: 'Grouping',
        17: 'Cruise Amount', 18: 'Gratuities', 19: 'Room Price',
        20: 'Room Price Per Day', 21: 'Cruise Amount Per Day',
        22: 'Airfare', 23: 'Drink Package', 24: 'Total Cruise Amount',
        25: 'Costco Rebate', 26: 'Shareholder', 27: 'OBC', 28: 'AARP Rebate', 29: 'Total Savings',
        30: 'Final Cruise Price',
        31: 'Ports', 32: 'Excursions', 33: 'Notes', 34: 'Who Went', 35: "Room Classification"
    }
    output_dict = {
        "tab_cruise_data_column_names": tab_cruise_data_column_names,
    }

    return output_dict


def get_pricing_list():
    pricing_agg = {
        "itinerary": ["Itinerary Category"],
        "room_type_by_ship": ["Type", "Ship"],
        "room_type_by_port": ["Type", "Port"],
        "room_type_by_month": ["Type", "Month"],
        "room_type_by_floor": ["Type", "Floor"],
        "room_type_by_day": ["Type", "Days"],
        "room_type_by_class": ["Type", "Class"],
        "room_type_by_itinerary_by_day": ["Type", "Itinerary Category", "Days"],
        "room_type_by_itinerary_by_month": ["Type", "Itinerary Category", "Month"],
        "itinerary_by_port": ["Itinerary Category", "Port"],
        "itinerary_by_days": ["Itinerary Category", "Days"],
        "itinerary_by_month": ["Itinerary Category", "Month"],
        "itinerary_by_class": ["Itinerary Category", "Class"]
    }
    return pricing_agg


def get_booking_price_breakdown(booking_dict, pricing_breakdown):

    booking_row = 0
    booking_price = booking_dict['Price']
    booking_price_per_day = booking_dict['Price Per Day']
    #booking_room_price = booking_dict['Room Price']
    #booking_room_price_per_day = booking_dict['Room Price Per Day']

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
        if len(agg_data) == 2:
            sec_booking = booking_dict[agg_data[1]]
            pricing_filter = (prim_booking, sec_booking)
        else:
            pricing_filter = prim_booking

        agg_breakdown = [
            'cruise_amount', 'cruise_amount_per_day'#, 'room_price', 'room_price_per_day'
        ]

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

                if a == 'cruise_amount':
                    temp_df['Pricing Category'] = 'Cruise Price'
                    temp_df['Mock Booking'] = booking_price
                elif a == 'cruise_amount_per_day':
                    temp_df['Pricing Category'] = 'Cruise Price Per Day'
                    temp_df['Mock Booking'] = booking_price_per_day
                '''
                elif a == 'room_price':
                    temp_df['Pricing Category'] = 'Room Amount'
                    temp_df['Mock Booking'] = booking_room_price
                elif a == 'room_price_per_day':
                    temp_df['Pricing Category'] = 'Room Amount Per Day'
                    temp_df['Mock Booking'] = booking_room_price_per_day
                '''
                row_list = temp_df.loc[0, :].values.flatten().tolist()
                booking_report.loc[booking_row] = row_list
                booking_row = booking_row + 1

    return booking_report
