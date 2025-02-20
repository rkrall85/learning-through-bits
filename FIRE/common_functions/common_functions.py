import pandas as pd


def get_column_names():
    """
    Purpose: Getting column names from sheets \n
    Created By Robert Krall \n
    Created On: 12/22/2024 \n
    :return: dict of column names
    :rtype: dict
    """
    balance_columns_names = {
        0: 'Company', 1: 'Employer', 2: 'Owner', 3: 'Type',
        4: 'Date', 5: 'Month', 6: 'Quarter', 7: 'Year', 8: 'YQ Key',
        9: 'Balance', 10: 'Contributions - Employee', 11: 'Contributions - Employer', 12: 'Total Contributions',
        13: 'Roll Over', 14: '401k Flag', 15: 'Fire Flag', 16: 'HSA Flag', 17: 'End of Year Flag', 18: 'Total Retirement Flag'
    }
    events_column_names = {
        0: 'Event', 1: 'Date', 2: 'Year', 3: 'Summary', 4: 'Label', 5: 'Type', 6: 'Owner', 7: 'HeatMapLabel'
    }

    pk_all_investment_types = ['Company', 'Employer', 'Owner', 'Type']
    pk_investment_types = ['Owner', 'Type']

    balances = pk_all_investment_types + ['Year', 'Balance']
    contributions = pk_all_investment_types + ['Year', 'Total Contributions', 'Roll Over']

    output_dict = {
        "balance_columns_names": balance_columns_names,
        "events_column_names": events_column_names,
        "pk_all_investment_types": pk_all_investment_types,
        "pk_investment_types":pk_investment_types,
        "balances": balances,
        "contributions": contributions
    }

    return output_dict


def get_pivoted_data(yearly_summary, heat_map_ordering, include_labels: bool = False):
    """
    Purpose: This will pivot the dataframe data to get data setup for heat map \n
    Created By: Robert Krall \n
    Created On: 12/26/2024 \n
    :param yearly_summary: dataframe of yearly summary
    :type yearly_summary: dataframe
    :return:
    """
    pivot_ror = yearly_summary.pivot(index='full_investment_name', columns='Year', values='Rate of Return')
    pivot_gains = yearly_summary.pivot(index='full_investment_name', columns='Year', values='Yearly Market Gains')
    years_list = sorted(yearly_summary['Year'].unique(), reverse=True)

    update_ror = order_pivot_data(pivot_ror, heat_map_ordering, years_list)
    updated_gains = order_pivot_data(pivot_gains, heat_map_ordering, years_list)

    if include_labels:
        pivot_labels = yearly_summary.pivot(index='full_investment_name', columns='Year', values='Label')
        updated_labels = order_pivot_data(pivot_labels, heat_map_ordering, years_list)
        return update_ror, updated_gains, updated_labels
    else:
        return update_ror, updated_gains, None


def order_pivot_data(pivot_df, heat_map_ordering, years_list):
    """
    Purpose: Re-order the datafame so its columns are years desc and rows are investment based on those years \n
    Created By: Robert Krall \n
    Created On: 12/26/2024 \n
    :param pivot_df:
    :return:
    """
    # heat map columns
    distinct_years = ['full_investment_name'] + sorted(years_list, reverse=True)
    # Remove years from heat map df
    # join the 2 dataframes to oder the set
    pivot_df = pd.merge(pivot_df, heat_map_ordering, on=['full_investment_name'], how='left')
    # Sort based on the created 'rank' column
    pivot_df.sort_values(by='heat_map_order', ascending=True, inplace=True)
    # re order columns
    pivot_df = pivot_df[distinct_years]
    pivot_df.set_index('full_investment_name', inplace=True)

    return pivot_df


def calculate_yearly_market_gains(row):
    """
    Purpose: This function will calc the row(yearly) market gains \n
    Created On: 01/01/2025 \n
    Created By: Robert Krall \n
    :param row: The row in the dataframe.
    :return: market gains value
    :rtype: float
    """
    return (
        row['Ending Balance'] - row['Total Contributions'] - row['Initial_Balance']
        - row['Initial_Roll_Over'] - row['Starting Balance']
    )


def calculate_yearly_ror(row):
    """
    Purpose: This function will calc the row(yearly) rate of return \n
    Created By: Robert Krall \n
    Created On: 01/01/2025 \n
    :param row: the row for the dataframe
    :return: the ror calc
    :rtype float
    """
    return row['Yearly Market Gains'] / row['Ending Balance']