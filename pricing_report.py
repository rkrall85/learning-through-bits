import pandas as pd;
import os;
import shutil;
from datetime import datetime, timedelta;
import math;

if os.name == "nt":
    from common_functions import *


def get_env_vars(copy_file=False):
    if os.name == "nt":
        source_path = "C:\\Users\\rober\\OneDrive\\Documents\\life_events\\Cruise Life.xlsx";
        destination_path = "C:\\dev\\data_learning\\travel\\Cruise Life.xlsx";
        if copy_file: shutil.copy(source_path, destination_path);
        return {
            "cruise_data": pd.read_excel(destination_path, sheet_name="cruise_data"),
            "cpi": pd.read_excel(destination_path, sheet_name="CPI Index")
        }
    else:
        return {
            "cruise_data": pd.DataFrame(xl("cruise_data")),
            "cpi": pd.DataFrame(xl("CPI"))
        }


def get_report_params():
    if os.name == "nt":
        return {
            'Itinerary Category': 'Caribbean - Eastern',
            'Port': 'Galveston',
            'Number of Ports': 4,
            'Use CPI Index': True,

            'Ship': 'Dream',
            'Class': 'Dream',

            'Room Type': 'Balcony',
            'Room Classification': 'Balcony',
            'Floor': 10,
            'Room Category': '8E',

            'Price': 4816,
            'OBC': 150,
            'Costco Rebate': 0,
            'AARP Discount': True,

            'Month': 'Jul',
            'Days': 8,
            'Travelers': 4
        }
    else:
        return {
            'Itinerary Category': xl("'Pricing Report'!B1"),
            'Port': xl("'Pricing Report'!B2"),
            'Number of Ports': xl("'Pricing Report'!B3"),
            'Use CPI Index':  xl("'Pricing Report'!B4"),

            'Ship': xl("'Pricing Report'!D1"),
            'Class': xl("'Pricing Report'!D2"),

            'Room Type': xl("'Pricing Report'!F1"),
            'Room Classification': xl("'Pricing Report'!F2"),
            'Floor': xl("'Pricing Report'!F3"),
            'Room Category': xl("'Pricing Report'!F4"),

            'Price': xl("'Pricing Report'!H1"),
            'OBC': xl("'Pricing Report'!H2"),
            'Costco Rebate': xl("'Pricing Report'!H3"),
            'AARP Discount': xl("'Pricing Report'!H4"),

            'Month': xl("'Pricing Report'!J1"),
            'Days': xl("'Pricing Report'!J2"),
            'Travelers':  xl("'Pricing Report'!J3")
        }


def get_pricing_agg(df, agg):

    # if agg is a str convert to list
    if isinstance(agg, str): agg = agg.split()

    agg_list = ['min', 'max', 'mean']

    #cruise_amount = df.groupby(agg)['Cruise Amount'].agg(agg_list)
    daily_person_costs = df.groupby(agg)['Daily Person Costs'].agg(agg_list)

    pricing_dict = {
        'daily_person_costs': daily_person_costs
    }

    return pricing_dict


def is_before_current_month(base_month, current_month):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    base_month_index = months.index(base_month)
    current_month_index = months.index(current_month)
    return base_month_index < current_month_index


def calculate_cost_of_living_index(cpi_df, base_year, base_month):
    # https://data.bls.gov/timeseries/CUUR0000SA0?years_option=all_years
    today = datetime.today()
    first_day_of_current_month = today.replace(day=1)
    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
    previous_month_name = last_day_of_previous_month.strftime('%B')[:3]
    current_year = today.year
    before_current_month = is_before_current_month(base_month, previous_month_name)
    if base_year < current_year and before_current_month:
        cpi_base = cpi_df.loc[cpi_df['Year'] == base_year, base_month].values[0]
        cpi_target = cpi_df.loc[cpi_df['Year'] == current_year, previous_month_name].values[0]
        cli = (cpi_target / cpi_base) * 100
    else:
        cli = 100
    return cli


copy_file = True
current_date = datetime.now()
report_params = get_report_params()
tab_data = get_env_vars(copy_file)
cruise_data = tab_data['cruise_data']
# Column names
columns_names = get_column_names()
tab_cruise_data_column_names = columns_names['tab_cruise_data_column_names']
# Data Frames
cruise_data_df = cruise_data.rename(columns=tab_cruise_data_column_names)
cruise_data_df = cruise_data_df[cruise_data_df['Cruise Amount'] != 0]  # remove Robert HS Cruise
cruise_data_df = cruise_data_df[[
    'Booking #', 'Year', 'Month', 'Ship', 'Itinerary', 'Itinerary Category', 'Port', 'Class',
    'Room Type', 'Room Category', 'Room Classification',
    'Days', 'Floor',
    'Daily Person Costs', 'Number of Ports'
]]

cpi_index = report_params['Use CPI Index']
if cpi_index:
    cpi_data = tab_data['cpi']
    tab_cpi_column_names = columns_names['tab_cpi_column_names']
    cpi_df = cpi_data.rename(columns=tab_cpi_column_names)

    cruise_data_df['CLI'] = cruise_data_df.apply(lambda row: calculate_cost_of_living_index(
        cpi_df=cpi_df,
        base_year=row['Year'],
        base_month=row['Month']
    ), axis=1)
    cruise_data_df['Daily Person Costs'] = cruise_data_df['Daily Person Costs'] * (cruise_data_df['CLI'] / 100)
    cruise_data_df = cruise_data_df.drop(columns=['CLI'])

pricing_list = get_pricing_list()
pricing_data = {}
for p in pricing_list:
    agg = pricing_list[p]
    price_breakdown = get_pricing_agg(cruise_data_df, agg)
    if p not in pricing_data:
        pricing_data[p] = {
            "data_agg": agg,
            "price_breakdown": price_breakdown
        }


booking_report_df = get_booking_price_breakdown(booking_dict=report_params, pricing_breakdown=pricing_data)
booking_report_df = booking_report_df.sort_values(by=['Min', 'Mean', 'Max'], ascending=True)
booking_report_df['Mock Booking Label'] = booking_report_df['Mock Booking']
# Further exclude rows where 'Min', 'Mean', 'Max', and 'Mock Booking' are the same
# Round values to the nearest dollar
booking_report_df = booking_report_df.round(0)
booking_report_df = booking_report_df[
    ~((booking_report_df['Min'] == booking_report_df['Mean']) &
      (booking_report_df['Mean'] == booking_report_df['Max']) &
      (booking_report_df['Max'] == booking_report_df['Mock Booking']))
]
booking_report_df = booking_report_df.reset_index(drop=True)
booking_report_df.loc[1:, 'Mock Booking Label'] = ""
booking_report_df