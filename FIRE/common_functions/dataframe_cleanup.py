import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable

if os.name == "nt":
    from FIRE.common_functions.common_functions import *


def get_balances_group_by(balances_df, group_by):
    """
    Purpose: This function will agg the dataframe for the various heatmaps we have \n
    Created By: Robert Krall \n
    Created On: 01/02/2024 \n
    :param balances_df: dataframe of balances before they are aggregated
    :param group_by:  A list of values such as ['Owner', 'Type']
    :return: a dataframe aggregated
    :rtype dataframe
    """

    # Initial  Balance
    balances_initial = balances_df.groupby(group_by).agg(
        Date=('Date', 'min')
    ).reset_index()
    balances_initial = pd.merge(balances_initial, balances_df,
                                on=group_by+['Date'],
                                how='inner').groupby(group_by).agg(
        Initial_Balance=('Balance', 'sum'),
        Year=('Year', 'min')
    ).reset_index()

    #  Initial Roll Over
    roll_over_initial = balances_df.groupby(group_by).agg(
        Year=('Year', 'min')
    ).reset_index()
    roll_over_initial = pd.merge(roll_over_initial, balances_df,
                                 on=group_by+['Year'],
                                 how='inner').groupby(group_by).agg(
        Initial_Roll_Over=('Roll Over', 'sum'),
        Year=('Year', 'min')
    ).reset_index()

    # Ending Balance
    balances_yearly_end = balances_df[balances_df['End of Year Flag'] == True]
    balances_yearly_end = balances_yearly_end.groupby(group_by+['Year']).agg(
        Ending_Balance=('Balance', 'sum')
    ).reset_index()

    # Starting Balance (previous ending balance)
    balances_yearly_end['Starting Balance'] = balances_yearly_end.groupby(group_by)['Ending_Balance'].shift(1)

    # Contributions and Roll Over
    balances_yearly_contributions = balances_df.groupby(group_by+['Year']).agg({
        'Total Contributions': 'sum',
        'Roll Over': 'sum'
    }).reset_index()

    # Start to build the balance final data set
    balances_yearly_final_dataset = pd.merge(balances_yearly_contributions, balances_yearly_end,
                                             on=group_by+['Year'], how='left')
    balances_yearly_final_dataset.replace([np.inf, -np.inf, np.nan], 1, inplace=True)
    # re-name columns
    balances_yearly_final_dataset.rename(columns={'Starting_Balance': 'Starting Balance'}, inplace=True)
    balances_yearly_final_dataset.rename(columns={'Ending_Balance': 'Ending Balance'}, inplace=True)
    # re order columns
    balances_yearly_final_dataset = balances_yearly_final_dataset[
        group_by+['Year','Starting Balance', 'Total Contributions', 'Roll Over', 'Ending Balance']]
    # Apply the function to each row and accumulate market gains and the ROR
    balances_yearly_final_dataset = pd.merge(balances_yearly_final_dataset, balances_initial,
                                             on=group_by+['Year'], how='left')
    balances_yearly_final_dataset['Initial_Balance'].fillna(0, inplace=True)

    balances_yearly_final_dataset = pd.merge(balances_yearly_final_dataset, roll_over_initial,
                                             on=group_by+['Year'], how='left')
    balances_yearly_final_dataset['Initial_Roll_Over'].fillna(0, inplace=True)

    balances_yearly_final_dataset['Yearly Market Gains'] = balances_yearly_final_dataset.apply(
        calculate_yearly_market_gains, axis=1)
    balances_yearly_final_dataset['Rate of Return'] = balances_yearly_final_dataset.apply(calculate_yearly_ror, axis=1)

    return balances_yearly_final_dataset


def create_heat_map(yearly_summary_df, map_title: str = 'Investment Type RoR with Gains', include_labels: bool = False):
    """
    Purpose: This function will create the heat map with the dataframe of data we have \n
    Created By: Robert Krall \n
    Created On: 01/02/2025 \n
    :param yearly_summary_df:  Data frame of data
    :type yearly_summary_df: dataframe
    :param map_title: The title of the heat map you want
    :type map_title: str
    :param include_labels: boolean if you wanted to include special label or not
    :type include_labels: bool
    :return:  Nothing; it will output hte heatmap on the screen
    """

    # Getting Years Count
    investment_years = yearly_summary_df.groupby(['full_investment_name']).agg(
        year_count=('Year', 'count'),
        max_year=('Year', 'max')
    ).reset_index()
    # Determine the most recent year and create a mapping
    most_recent_year = investment_years['max_year'].max()
    year_mapping = {most_recent_year - i: chr(65 + i) for i in
                    range(most_recent_year - investment_years['max_year'].min() + 1)}
    investment_years['Year_Letter'] = investment_years['max_year'].map(year_mapping)
    investment_years['heat_map_order'] = investment_years['Year_Letter'] + investment_years['year_count'].astype(str)
    heat_map_ordering = investment_years[['full_investment_name', 'heat_map_order']]

    pivot_ror, pivot_gains, pivot_labels = get_pivoted_data(yearly_summary_df, heat_map_ordering, include_labels=include_labels)

    # Set a mask for NaN values
    mask = pivot_ror.isnull()

    # Custom annotation to display both ROR and Gains
    annot = pivot_ror.copy().astype(str)
    for i in range(pivot_ror.shape[0]):
        for j in range(pivot_ror.shape[1]):
            ror = pivot_ror.iloc[i, j]
            gains = pivot_gains.iloc[i, j]
            if include_labels: labels = pivot_labels.iloc[i, j]

            annot_string = f'{ror:.2%}\n${gains:,.2f}'
            if include_labels:
                annot_string += f'\n\n{labels}'
            else:
                annot_string += f'\n\n'
            annot.iloc[i, j] = annot_string

    # Create the heatmap
    cmap = LinearSegmentedColormap.from_list('custom_cmap', ['red', 'yellow', 'green'])
    cmap.set_bad(color='#ECEABC')  # Set the color for NaN values

    # larger figure size and square =True makes sure the heat box is big enough
    fig = plt.figure(figsize=(30, 20))
    #fig, ax = plt.subplots(figsize=(30,20))
    ax = sns.heatmap(pivot_ror, annot=annot, cmap=cmap, linewidths=.5, fmt='', center=0, square=True, mask=mask, cbar=False)

    # Remove x and y labels
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Set the title
    plt.title(map_title)

    # Create divider for existing axes instance
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)

    # Create colorbar and set it to have the same height as the heatmap
    cbar = fig.colorbar(ax.collections[0], cax=cax)
    cax.set_aspect(20)  # Adjust this value to match your heatmap height

    # Display the plot
    plt.show()
