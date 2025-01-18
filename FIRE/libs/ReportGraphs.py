
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
        'SwineTech': 'pink',
        'Rocket Software': 'blue',
        'Farm Credit': 'purple',
        'Personal': 'brown',
        'Vanguard': 'orange',
        'UHS': '#016667'
}

retirement_type_colors = {
        '401k': 'green',
        'HSA': 'blue',
        'Roth IRA': 'brown',
        'Post': 'blue',
        'Pre': 'green'
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


def yearly_balance_stacked_bar_graph(
        df, selected_years, title='Company Balances Over Years',
        group_by=['Year', 'Company'], width=0.5, money_type: str = 'Balance'
):
    """
    Purpose: This function will stack the yearly retirement balance by category, employer, or type
    :param money_type:
    :param width:
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
    grouped = selected_data.groupby(group_by)[money_type].sum().unstack().fillna(0)

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
                plt.text(indices[j], bottoms[j] + balance / 2, f'{locale.currency(balance, grouping=True)}', ha='center' ,va='center', color='white')

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
    colors = {'Employee': '#016667', 'Employer': '#670201'}

    # Plotting each year's contributions for each owner
    for i, year in enumerate(years):
        for j, owner in enumerate(owners):
            owner_data = filtered_df[(filtered_df['Owner'] == owner) & (filtered_df['Year'] == year)]
            if not owner_data.empty:
                employee_contributions = owner_data['Employee'].values[0]
                employer_contributions = owner_data['Employer'].values[0]

                bar_position = i + (j - 0.5) * bar_width
                ax1.bar(bar_position, employee_contributions, width=bar_width, color=colors['Employee']
                        ,label='Employee Contributions' if i == 0 and j == 0 else "")
                ax1.bar(bar_position, employer_contributions, width=bar_width, bottom=employee_contributions
                        ,color=colors['Employer'], label='Employer Contributions' if i == 0 and j == 0 else "")

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
    relevant_labels = {'Employee Contributions': '#016667', 'Employer Contributions': '#670201', 'Employee Limit': 'red'}
    relevant_handles = [unique_labels[key] for key in relevant_labels.keys()]
    ax1.legend(relevant_handles, relevant_labels.keys(), loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()


def get_current_goal(current_balance, goal_balances):
    for goal in goal_balances:
        if current_balance < goal:
            return goal
    return goal_balances[-1]


def fire_progress_bar(current_balance, previous_balance, goal_balances, goal_dates, goal_ages):
    """
    Purpose: This function will create the FIRE progresses bar \n
    Created On: 01/11/2025 \n
    Created By: Robert Krall \n
    :param current_balance:
    :param previous_balance:
    :param goal_balances:
    :param goal_dates:
    :param goal_ages:
    :return:
    """

    # Determine the current target goal
    current_target_goal = get_current_goal(current_balance, goal_balances)
    current_target_index = goal_balances.index(current_target_goal)

    # Calculate progress towards the current target goal
    previous_goal = previous_balance if current_target_index == 0 else goal_balances[current_target_index - 1]
    progress = current_balance / current_target_goal * 100 if current_target_index == 0 else (current_balance - previous_goal) / (current_target_goal - previous_goal) * 100

    # Ensure the progress line does not go beyond the current target goal
    if progress > 100:
        progress = 100

    # Normalize goal positions to prevent overlap
    goal_positions = [(goal - previous_balance) / (goal_balances[-1] - previous_balance) * 100 for goal in goal_balances]

    # Create gradient for the progress bar
    fig, ax = plt.subplots(figsize=(8, 3))
    gradient = np.linspace(1, 0, 256)
    gradient = np.vstack((gradient, gradient))

    # Calculate the actual position of the progress bar within the goal range
    if current_target_index == 0:
        progress_position = (progress / 100) * goal_positions[current_target_index]
    else:
        progress_position = (current_balance - previous_goal) / (goal_balances[current_target_index] - previous_goal) * \
                            (goal_positions[current_target_index] - goal_positions[current_target_index - 1]) + \
                            goal_positions[current_target_index - 1]

    # Plot gradient only up to the progress percentage
    ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap('Greens'), extent=[0, progress_position, 0, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1)

    # Change the progress line color to blue
    ax.axvline(progress_position, color='blue', linestyle='-', linewidth=2, alpha=0.7)
    ax.text(progress_position, -0.1, f'{progress:.2f}%', horizontalalignment='center', fontsize=12, color='blue')

    # Add vertical lines for each goal balance with dates
    for i, (goal_balance, goal_position) in enumerate(zip(goal_balances, goal_positions)):

        # Determine color based on whether the goal has a date (met) or not (unmet)
        if current_balance >= goal_balance:
            goal_color = 'green'
            goal_text = f'Goal: {goal_balance // 1000000}M'
            if i < len(goal_dates): goal_text += f'\nMet: {goal_dates[i].strftime("%Y")}'
            if i < len(goal_ages): goal_text += f'\nAge: {goal_ages[i]}'
        else:
            goal_color = 'red'
            goal_text = f'Goal: {goal_balance // 1000000}M'

        ax.axvline(goal_position, color=goal_color, linestyle='--', linewidth=2)
        ax.text(goal_position, 1.1, goal_text, horizontalalignment='center', fontsize=12, fontweight='bold', color=goal_color)

    # Add text for current balance and change to the right of the progress bar
    ax.text(105, 0.75, f'Current Balance: ${current_balance:,.2f}', horizontalalignment='left', fontsize=14, fontweight='bold')
    change = current_balance - previous_balance
    change_percentage = (change / previous_balance) * 100
    if change >= 0:
        change_text = f'YoY Increase: ${change:,.2f} ({change_percentage:.2f}%)'
    else:
        change_text = f'YoY Decrease: ${change:,.2f} ({change_percentage:.2f}%)'
    ax.text(105, 0.4, change_text, horizontalalignment='left', fontsize=12, color='black')

    # Hide axes
    ax.axis('off')

    # Display the plot
    plt.show()


def pie_chart_balance_breakdown(df, by_column: str = 'Type'):
    """
    Purpose: This function will output a pie chart of the current breakdown of balances
    :param df:
    :return:
    """

    # Data for the pie chart
    labels = df[by_column]
    sizes = df['Balances']
    colors = [retirement_type_colors[t] for t in df[by_column]]
    explode = [0.1] + [0] * (len(df) - 1)  # Dynamic explode list

    # Create the pie chart with custom percentage text color
    wedges, texts, autotexts = plt.pie(
        sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140
    )

    # Set percentage text color to white
    for autotext in autotexts:
        autotext.set_color('white')

    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')

    # Add a title
    plt.title(f'Current Retirement Balance Breakdown by {by_column}')

    # Display the pie chart
    plt.show()


def bar_chart_contributions_left(
        df,
        current_year: str,
        previous_year: str,
        contribution_type: str = 'HSA',
        owner: str = None
):

    current_year = float(current_year)
    previous_year = float(previous_year)

    # Convert 'Year' and 'year_sort' to strings to handle fractional years
    df['Year'] = df['Year'].astype(str)
    df['year_sort'] = df['year_sort'].astype(str)

    # Get xticks and xticklabels from the dataframe
    xticklabels = df['year_label'].to_list()
    xticks = df['year_sort'].to_list()

    # Plot the contributions comparison using a stacked bar graph
    fig, ax = plt.subplots()

    # Bar graph for each year
    for i, row in df.iterrows():
        bar = ax.bar(row['year_sort'], row['Contributions'], label=f'{row["Year"]} Contributed So Far',
                     color='blue' if row['year_sort'] in ('2', '4') else (
                         'green' if row['year_sort'] in ('1', '3') else 'orange'))
        ax.bar(row['year_sort'], row['Remaining Contribution'], bottom=row['Contributions'], label='_nolegend_',
               color='lightgray')  # Use '_nolegend_' for no label

        # Calculate the percentage of contributions
        percentage = (row['Contributions'] / row['yearly_contributions']) * 100

        # Add white labels for contributions formatted as currency with two decimal places and percentage
        ax.text(row['year_sort'], row['Contributions'] / 2, f'${row["Contributions"]:.2f}\n({percentage:.2f}%)',
                color='white', ha='center', va='center')

    # Add labels and title
    ax.set_ylabel('Amount ($)')
    if owner is not None:
        ax.set_title(f'{owner} - {contribution_type} Contributions Comparison: Various Years')
    else:
        ax.set_title(f'{contribution_type} Contributions Comparison: Various Years')

    # Set x-ticks to the sorted years
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)

    # Only add legend once to avoid duplicates
    handles, labels = ax.get_legend_handles_labels()
    unique_labels = []
    unique_handles = []
    for handle, label in zip(handles, labels):
        if label not in unique_labels:
            unique_labels.append(label)
            unique_handles.append(handle)
    ax.legend(unique_handles, unique_labels)

    # Display the graph
    plt.show()
