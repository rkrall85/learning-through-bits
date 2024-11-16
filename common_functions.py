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
        11: 'Room #', 12: 'Floor', 13: 'Type', 14: 'Room Rank', 15: 'Room Category', 16: 'Room Classification',
        17: 'Cruise Amount', 18: 'Cruise Amount Minus Savings',
        19: 'Gratuities', 20: 'Airfare', 21: 'Drink Package', 23: 'Total Cruise Amount',
        24: 'Costco Rebate', 25: 'Shareholder', 26: 'OBC', 27: 'AARP Rebate', 28: 'Total Savings',
        29: 'Final Trip Price',
        30: 'Ports', 31: 'Excursions', 32: 'Notes', 33: 'Who Went'
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
        "room_type_by_port_floor_itinerary": ["Type", "Port", "Floor", "Itinerary Category"],
        "room_type_by_itinerary_by_day": ["Type", "Itinerary Category", "Days"],
        "room_type_by_itinerary_by_month": ["Type", "Itinerary Category", "Month"],
        "room_type_by_month_by_days": ["Type", "Month", "Days"],
        "itinerary_by_port": ["Itinerary Category", "Port"],
        "itinerary_by_days": ["Itinerary Category", "Days"],
        "itinerary_by_month": ["Itinerary Category", "Month"],
        "itinerary_by_class": ["Itinerary Category", "Class"]
    }
    return pricing_agg


def get_booking_price_breakdown(booking_dict, pricing_breakdown):

    booking_row = 0
    booking_price = booking_dict['Price']
    booking_obc = booking_dict['OBC']
    booking_costco_rebate = booking_dict['Costco Rebate']
    booking_aarp_discount = booking_dict['AARP Discount']
    booking_days = booking_dict['Days']

    # Get shareholder credits
    if booking_days <= 4:
        booking_shareholder = 50
    elif 4 < booking_days <= 10:
        booking_shareholder = 100
    else:
        booking_shareholder = 250

    aarp_discount = 0
    if booking_aarp_discount:
        aarp_discount = booking_price * .10

    booking_savings = (booking_shareholder + booking_obc + booking_costco_rebate + aarp_discount)
    booking_price_with_savings = booking_price - booking_savings

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

        agg_breakdown = ['cruise_amount', 'cruise_amount_minus_savings']

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
                elif a == 'cruise_amount_minus_savings':
                    temp_df['Pricing Category'] = 'Cruise Price Minus Savings'
                    temp_df['Mock Booking'] = booking_price_with_savings

                row_list = temp_df.loc[0, :].values.flatten().tolist()
                booking_report.loc[booking_row] = row_list
                booking_row = booking_row + 1

    return booking_report
