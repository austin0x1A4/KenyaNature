from django.shortcuts import render
import io
import base64
import pandas as pd 
import geopandas as gpd 
import matplotlib.pyplot as plt
import os


# Create your views here.
def index(request):
    return render(request, "homepage/index.html")

def nature(request):
    DATA_DIR = os.path.join(os.path.dirname(__file__), 'data') 
    fpath = os.path.join(DATA_DIR, 'paste.txt')

    df = pd.read_csv(fpath, sep='\s+', skiprows=2, names=['ADM0_EN', 'County', 'date', 'sum', 'Area_km', 'Area_ha'])
    print("DataFrame Columns:", df.columns)

    shpath = os.path.join(DATA_DIR, 'Kenya_Counties.shp')
    counties = gpd.read_file(shpath)
    print("GeoDataFrame Columns:", counties.columns)
    merged = None
    try:
        merged = counties.merge(df, left_on='COUNTY_NAM', right_on='County')
    except KeyError as e:
        print("KeyError:", e)
        # If 'ADM1_EN' is not present in either DataFrame, adjust the column names accordingly.
    if merged is not None:
        fig, ax = plt.subplots(1, figsize=(12, 8))
        merged.plot(column='percentage forest Area', cmap='BuGn', linewidth=0.8, ax=ax, edgecolor='0.2')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plot_url = base64.b64encode(buf.read()).decode()

    else:
        print("No data available for plotting.")
        plot_url = None

    context = {
        'plot_url': plot_url
    }
    return render(request, "homepage/nature.html", context)

def energy(request):
    return render(request, "homepage/energy.html")

def about(request):
    return render(request, 'homepage/about.html')

def privacy(request):
    return render(request, 'homepage/privacy.html')

def contact(request):
    return render(request, 'homepage/contact.html')