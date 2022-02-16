import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.subplots(figsize=(15,5))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    model = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])   # scipy linregress is used to calculate a linear least-squares regression for two sets of measurements.

    x = pd.Series([i for i in range(1880, 2051)])
    y = model.slope * x + model.intercept

    plt.figure(figsize=(15,5))
    plt.plot(x, y, '-r')
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    model2 = linregress(x=df2['Year'], y=df2['CSIRO Adjusted Sea Level'])

    x = pd.Series([i for i in range(2000, 2051)])
    y = model2.slope * x + model2.intercept
    plt.plot(x, y, '-y')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()