import pandas as pd

# Read data from 'paste.txt'
df1 = pd.read_csv('paste.txt', sep='\s+', skiprows=2, names=['ADM0_EN', 'ADM1_EN', 'date', 'sum', 'Area_km', 'Area_ha'])

# Additional data
data2 = {
    'County_Area_km': [10889.2, 9305.5, 3008.4, 3334.6, 2525.5, 30456.8, 1475.3, 2513.2, 6047.0, 2543.0, 25979.3, 21015.7, 2484.7, 2438.2, 6992.5, 2835.8, 2823.7, 2581.0, 1313.7, 897.2, 707.5, 3266.7, 7487.1, 12599.3, 233.6, 43596.0, 17912.2, 17131.1, 8174.9, 3396.8, 25399.3, 39192.2, 56668.6, 8266.0, 70131.8, 560.5, 76027.8, 3008.0, 3016.2, 21884.8, 9536.9, 4731.9, 6044.3, 2665.0, 1811.6, 3520.4, 3144.3],
    'Percentage_forest_Area': ['67.0404621', '66.7894256', '63.8063422', '57.5670245', '54.0411800', '46.4473615', '46.0286044', '45.4034697', '42.4112783', '41.9335431', '39.4821262', '39.3488202', '38.4984103', '35.0611107', '34.3033250', '33.4268989', '32.3100896', '32.1960480', '31.4249829', '30.7634864', '29.5265018', '29.3213335', '29.0380788', '26.7124364', '26.3142123', '21.2242637', '19.8937037', '19.3142880', '16.2905968', '15.9273434', '15.6003512', '14.9101607', '12.5952644', '11.4275345', '11.1447731', '10.1266726', '10.1015418', '9.9045878', '9.4904184', '8.8781712', '8.4761296', '3.1697627', '2.8822196', '2.7166979', '2.3299845', '1.0995910', '0.9661928']
}

# Create DataFrame from additional data
df2 = pd.DataFrame(data2)

# Merge based on 'ADM1_EN'
merged_df = pd.merge(df1, df2, how='left', left_on='ADM1_EN', right_on='County_Area_km')

# Drop unnecessary columns
merged_df = merged_df.drop(['County_Area_km'], axis=1)

# Save the merged data to 'paste1.txt'
merged_df.to_csv('paste1.txt', index=False, sep='\t')
