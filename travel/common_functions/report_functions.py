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
    return names[-1], 0


def get_booking_price_breakdown(booking_dict, pricing_breakdown):
    booking_row = 0
    booking_price = booking_dict['Price']
    booking_obc = booking_dict['OBC']
    booking_costco_rebate = booking_dict['Costco Rebate']
    booking_aarp_discount = booking_dict['AARP Discount']
    booking_days = booking_dict['Days']
    booking_travelers = booking_dict['Travelers']

    # Get shareholder credits
    if booking_days <= 4: booking_shareholder = 50
    elif 4 < booking_days <= 10: booking_shareholder = 100
    else: booking_shareholder = 250

    aarp_discount = 0
    # ticket(5) add logic after 12/21/24 then its 5%; after 07/05/2024 its 8% otherwise 10%
    if booking_aarp_discount: aarp_discount = booking_price * .08
    else:
        if booking_costco_rebate > 0: booking_costco_rebate = booking_costco_rebate + (booking_price*.05)

    booking_savings = (booking_shareholder + booking_obc + booking_costco_rebate + aarp_discount)
    booking_price_with_savings = booking_price - booking_savings
    booking_price_per_person = booking_price_with_savings/booking_days/booking_travelers

    booking_pricing = {}
    df_columns = ['Pricing By', 'Pricing Filter', 'Pricing Category', 'Min', 'Mean', 'Max', 'Mock Booking']
    booking_report = pd.DataFrame(columns=df_columns)

    for p in pricing_breakdown:
        agg_data = pricing_breakdown[p]['data_agg']
        prim_agg = agg_data[0]
        prim_booking = booking_dict[prim_agg]
        bookings = [prim_booking] # Create a list to hold the bookings

        # Loop through the remaining items in agg_data (if any) and add to the bookings list
        for i in range(1, len(agg_data)): bookings.append(booking_dict[agg_data[i]])

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

                row_list = temp_df.loc[0, :].values.flatten().tolist()
                booking_report.loc[booking_row] = row_list
                booking_row = booking_row + 1

    return booking_report
