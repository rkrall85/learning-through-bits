import pandas as pd;
import os;
import shutil;
from datetime import datetime;
import math;
import numpy as np

if os.name == "nt":
    from common_functions import *


def get_env_vars(copy_file=False):
    if os.name == "nt":
        source_path = "C:\\Users\\rober\\OneDrive\\Documents\\life_events\\Cruise Life.xlsx";
        destination_path = "C:\\dev\\data_learning\\travel\\Cruise Life.xlsx";
        if copy_file: shutil.copy(source_path, destination_path);
        return {
            "cruise_data": pd.read_excel(destination_path, sheet_name="cruise_data")
        }
    else:
        return {
            "cruise_data": pd.DataFrame(xl("cruise_data"))
        }


def get_report_params():
    if os.name == "nt":
        return {
            'Itinerary Category': 'Caribbean - Southern',
            'Port': 'Galveston',
            'Type': 'Balcony',

            'Ship': 'Dream',
            'Class': 'Dream',

            'Price': 3500,
            'OBC': 50,
            'Costco Rebate': 0,
            'AARP Discount': True,

            'Floor': 9,
            'Month': 'Jun',
            'Days': 8
        }
    else:
        return {
            'Itinerary Category': xl("'Pricing Report'!B1"),
            'Port': xl("'Pricing Report'!B2"),
            'Type': xl("'Pricing Report'!B3"),

            'Ship': xl("'Pricing Report'!E1"),
            'Class': xl("'Pricing Report'!E2"),

            'Price': xl("'Pricing Report'!H1"),
            'OBC': xl("'Pricing Report'!H2"),
            'Costco Rebate': xl("'Pricing Report'!H3"),
            'AARP Discount': xl("'Pricing Report'!H4"),

            'Floor': xl("'Pricing Report'!K1"),
            'Month': xl("'Pricing Report'!K2"),
            'Days': xl("'Pricing Report'!K3"),
        }


def get_pricing_agg(df, agg):

    # if agg is a str convert to list
    if isinstance(agg, str): agg = agg.split()

    agg_list = ['min', 'max', 'mean']

    cruise_amount = df.groupby(agg)['Cruise Amount'].agg(agg_list)
    cruise_amount_minus_savings = df.groupby(agg)['Cruise Amount Minus Savings'].agg(agg_list)

    pricing_dict = {
        'cruise_amount': cruise_amount,
        'cruise_amount_minus_savings': cruise_amount_minus_savings
    }

    return pricing_dict


copy_file = True
current_date = datetime.now()
tab_data = get_env_vars(copy_file)
cruise_data = tab_data['cruise_data']
# Column names
columns_names = get_column_names()
tab_cruise_data_column_names = columns_names['tab_cruise_data_column_names']
# Data Frames
cruise_data_df = cruise_data.rename(columns=tab_cruise_data_column_names)
cruise_data_df = cruise_data_df[cruise_data_df['Cruise Amount'] != 0]  # remove Robert HS Cruise
cruise_data_df = cruise_data_df[[
    'Booking #', 'Month', 'Ship', 'Itinerary', 'Itinerary Category', 'Port', 'Class',
    'Days', 'Type', 'Floor',
    'Cruise Amount', 'Cruise Amount Minus Savings'
]]

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

report_params = get_report_params()
booking_report_df = get_booking_price_breakdown(booking_dict=report_params, pricing_breakdown=pricing_data)
booking_report_df