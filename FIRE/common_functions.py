

def get_column_names():
    """
    Purpose: Getting column names from sheets \n
    Created By Robert Krall \n
    Created On: 12/22/2024 \n
    :return: dict of column names
    :rtype: dict
    """
    tab_yearly_contributions = {
        0: 'Year', 1: 'Self Contributions', 2: 'Income', 3: 'Self Investing', 4: 'Total Contributions', 5: 'Total %',
        6: '15% Goal', 7: 'How Much Behind',
        8: 'Empty',
        9: 'Owner', 10: 'Year', 11: 'Type', 12: 'Employee Contributions', 13: 'Employer Contributions',
        14: 'Total Contributions', 15: 'Employee Limit',
        16: 'Empty',
        17: 'Company', 18: 'Employer', 19: 'Owner', 20: 'Year', 21: 'Type', 22: 'Employee Contributions',
        23: 'Employer Contributions', 24: 'Total Contributions', 25: 'Roll Over'
    }
    yearly_by_type = [
        'Owner', 'Year.1', 'Type', 'Employee Contributions', 'Employer Contributions',
        'Total Contributions.1', 'Employee Limit'
    ]
    yearly_by_company_by_type = ['Company', 'Employer', 'Owner.1', 'Year.2', 'Type.1', 'Total Contributions.2', 'Roll Over']

    tab_yearly_balances = {
        0: 'Company', 1: 'Employer', 2: 'Owner', 3: 'Type', 4: 'Year', 5: 'Balance',
        6: '401k Flag', 7: 'Fire Flag', 8: 'HSA Flag', 9: 'Total Retirement Flag'
    }
    yearly_balance = ['Company', 'Employer', 'Owner', 'Type', 'Year', 'Balance']

    pk_by_type = ['Company', 'Employer', 'Owner', 'Type', 'Year']

    output_dict = {
        "tab_yearly_contributions": tab_yearly_contributions,
        "yearly_by_type": yearly_by_type,
        "yearly_by_company_by_type": yearly_by_company_by_type,
        "tab_yearly_balances": tab_yearly_balances,
        "yearly_balance": yearly_balance,
        "pk_by_type": pk_by_type
    }

    return output_dict