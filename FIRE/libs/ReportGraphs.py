

import matplotlib.pyplot as plt
import numpy as np
import locale


company_colors = {
        'Associated Bank': 'green',
        'Charles Schwab': 'orange',
        'Fidelity': 'blue',
        'John Hancock': 'purple',
        'M1': 'brown',
        'Vanguard': 'pink'
}

employer_colors = {
        'Associated Bank': 'green',
        'SwineTech': 'orange',
        'Rocket Software': 'blue',
        'Farm Credit': 'purple',
        'Personal': 'brown',
        'Vanguard': 'pink',
        'UHS': 'red'
}

retirement_type_colors = {
        '401k': 'green',
        'HSA': 'blue',
        'Roth IRA': 'brown'
}


def yearly_balance_bar_graph_with_predictions(df, selected_years, title, future_years_count):
    """
    Purpose: This Function will create a bar graph from the data frame of years and balances with future prediction \n
    Created By: Robert Krall \n
    Created On: 01/05/2024 \n
    :param df:
    :param selected_years:
    :param title:
    :param future_years_count:
    :return:
    """
    width = 0.5
    selected_years = sorted(selected_years)  # Sort the selected years
    selected_data = df[df['Year'].isin(selected_years)]
    indices = np.arange(len(selected_years))

    plt.figure(figsize=(10, 6))

    balances = []

    for i, year in enumerate(selected_years):
        year_data = selected_data[selected_data['Year'] == year]
        balance_value = round(year_data['Balance'].values[0])
        balances.append(balance_value)
        plt.bar(indices[i], balance_value, width, color='blue')

        # Add label of the value on each bar formatted as currency
        plt.text(indices[i], balance_value + 1, locale.currency(balance_value, grouping=True), ha='center',
                 va='bottom')

    # Only fit and add trendline if there are at least 2 years selected
    if len(selected_years) > 1:
        z = np.polyfit(indices, balances, 1)
        p = np.poly1d(z)
        plt.plot(indices, p(indices), color='red', linestyle='--', label='Trendline')

        # Predict next 3 years
        future_years = np.arange(len(selected_years), len(selected_years) + future_years_count)
        future_balances = p(future_years)
        future_year_labels = [df['Year'].max() + i + 1 for i in range(future_years_count)]

        # Plot future predictions
        for i, year in enumerate(future_years):
            plt.bar(year, future_balances[i], width, color='green', alpha=0.5)
            plt.text(year, future_balances[i] + 1, locale.currency(future_balances[i], grouping=True), ha='center',
                     va='bottom')

        # Update x-ticks
        all_year_labels = selected_years + future_year_labels
        plt.xticks(list(indices) + list(future_years), all_year_labels)
    else:
        plt.xticks(indices, selected_years)

    plt.xlabel('Year')
    plt.ylabel('Balance')
    plt.title(title)
    plt.show()


def yearly_balance_stacked_bar_graph(df, selected_years, title='Company Balances Over Years', group_by=['Year', 'Company'], width=0.5 ):
    """
    Purpose: This function will stack the yearly retirement balance by category, employer, or type
    :param df:
    :param selected_years:
    :param title:
    :return:
    """
    # Filter the DataFrame based on selected years
    selected_data = df[df['Year'].isin(selected_years)]
    selected_years = sorted(selected_years)
    indices = np.arange(len(selected_years))

    # Plotting
    plt.figure(figsize=(10, 6))

    # Group data by Year and Company
    grouped = selected_data.groupby(group_by)['Balance'].sum().unstack().fillna(0)

    bottoms = np.zeros(len(selected_years))
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']  # Add more colors if needed

    if 'Company' in group_by:
        colors = company_colors
    elif 'Employer' in group_by:
        colors = employer_colors
    elif 'Type' in group_by:
        colors = retirement_type_colors
    else:
        colors = company_colors

    for i, g in enumerate(grouped.columns):
        balances = grouped[g].values
        color = colors.get(g, 'gray') # colors[i % len(colors)]
        plt.bar(indices, balances, width, bottom=bottoms, color=color, label=g)

        # Add labels
        for j, balance in enumerate(balances):
            if balance != 0:
                plt.text(indices[j], bottoms[j] + balance / 2, f'{locale.currency(balance, grouping=True)}', ha='center',va='center', color='white')

        bottoms += balances

    # Update x-ticks
    plt.xticks(indices, selected_years)

    plt.xlabel('Year')
    plt.ylabel('Balance')
    plt.title(title)
    plt.legend()
    plt.show()


def yearly_contributions_stacked_bar_graph(df, selected_years, title, bar_width=0.5):
    """

    :param df:
    :param selected_years:
    :param title:
    :param width:
    :return:
    """

    # Filter the DataFrame based on selected years
    filtered_df = df[df['Year'].isin(selected_years)]

    # Unique years and owners
    years = sorted(filtered_df['Year'].unique())
    owners = filtered_df['Owner'].unique()

    # Indices for bar positions
    indices = np.arange(len(years))

    # Set up the figure and axis
    fig, ax1 = plt.subplots(figsize=(12, 8))

    # Plotting colors for employee and employer contributions
    colors = {'Employee': 'green', 'Employer': 'orange'}

    # Plotting each year's contributions for each owner
    for i, year in enumerate(years):
        for j, owner in enumerate(owners):
            owner_data = filtered_df[(filtered_df['Owner'] == owner) & (filtered_df['Year'] == year)]
            if not owner_data.empty:
                employee_contributions = owner_data['Employee'].values[0]
                employer_contributions = owner_data['Employer'].values[0]

                bar_position = i + (j - 0.5) * bar_width
                ax1.bar(bar_position, employee_contributions, width=bar_width, color=colors['Employee'],label='Employee Contributions' if i == 0 and j == 0 else "")
                ax1.bar(bar_position, employer_contributions, width=bar_width, bottom=employee_contributions,color=colors['Employer'], label='Employer Contributions' if i == 0 and j == 0 else "")

                # Add labels for Employee contributions
                ax1.text(bar_position, employee_contributions / 2, f'{locale.currency(employee_contributions, grouping=True)}', ha='center', color='white')
                # Add labels for Employer contributions
                ax1.text(bar_position, employee_contributions + employer_contributions / 2, f'{locale.currency(employer_contributions, grouping=True)}', ha='center', color='white')

    # Plot the Employee Limit as a line on the same axis
    df_grouped = filtered_df.groupby('Year')['Employee Limit'].max().reindex(years)
    ax1.plot(indices, df_grouped.values, color='red', linestyle='--', marker='o', label='Employee Limit')

    # Set labels
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Contributions')
    ax1.set_title(title)

    # Update x-ticks to show all years with space for owner names
    ax1.set_xticks(indices)
    ax1.set_xticklabels([f'{year}' for year in years])

    # Add owner labels below the x-ticks
    for i, year in enumerate(years):
        for j, owner in enumerate(owners):
            bar_position = i + (j - 0.5) * bar_width
            ax1.text(bar_position, -2000, f'{owner}', ha='center', va='top', rotation=45, fontsize=10, color='black')

    # Add customized legend
    handles, labels = ax1.get_legend_handles_labels()
    unique_labels = dict(zip(labels, handles))
    relevant_labels = {'Employee Contributions': 'green', 'Employer Contributions': 'orange', 'Employee Limit': 'red'}
    relevant_handles = [unique_labels[key] for key in relevant_labels.keys()]
    ax1.legend(relevant_handles, relevant_labels.keys(), loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()