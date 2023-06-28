import pandas as pd
from sqlalchemy import create_engine
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


#**************Importing Munich Vehicle Registration Data**************
#MVR = Munich Vehicle Registration Data




MVR_df = pd.read_excel('"C:\Users\aleem\Downloads\rad_tage.csv"',skiprows=1)
print(MVR_df)

#**************Importing Munich Bike Sharing Data**************
#BS= Munich Bike Sharing 



BS_df = pd.read_csv("file://rad_tage.csv")
#data can be download from the link ("https://www.kaggle.com/code/docxian/bike-traffic-in-munich")
print(BS_df.head())




#**************Cleaning Munich Vehicle Registration Data**************


#Cleaning of Munich Vehicle Registration data to acquire only required columns

# Specify the number of columns to include
num_columns = 20

# Slice the DataFrame to store up to the specified number of columns
new_mvr_df = MVR_df.iloc[:, :num_columns]

# Display the new DataFrame with only specified number of column names 
print(new_mvr_df.columns)


#Changing of column names to English for ease 

# Define the new column names
new_column_names = ['Year', 'Administrative district', 'Statistical code and registration district', 'altogether', 'therefrom Two-wheeled Car', 'of that three-wheeled car', 'of that light four-wheeled vehicles', 'underneath female Holder', 'passenger cars total', 'Displacement until 1,399cc', '1400 until 1999cc', '2000 and more cc', 'unknown', 'With open Construction', 'with all wheel drive', 'namely residential mobile', 'in fact Suffer-car, emergency doctor operational vehicles', 'commercial holder', 'female holder', 'Car Density per 1000 resident']

# Assign the new column names to the DataFrame
new_mvr_df.columns = new_column_names

# Display the DataFrame with the updated column names
print(new_mvr_df.columns)


#**************Cleaning Munich Bike Sharing Data**************




# Specify the number of columns to include
num_columns = 7

# Slice the DataFrame to exclude the first row and store up to the specified number of columns
new_bs_df = BS_df.iloc[:, :num_columns]

# Display the new DataFrame with added column names and no first row
print(new_bs_df.columns)

#Assigning New Column Names in English to Munich Bike Sharing Data

# Define the new column names
new_column_names = ['Date', 'Time_Start', 'Time_End', 'Counting_Station', 'Direction_1', 'Direction_2', 'In_total', ]

# Assign the new column names to the DataFrame
new_bs_df.columns = new_column_names
# Display the DataFrame with the updated column names
print(new_bs_df.columns)


#**************Removing Missing Values from Data Frames**************

new_mvr_df.dropna()
new_bs_df.dropna()


#**************Creating DB Files**************



createDb = create_engine("sqlite:///Munich_VR_&_BS.db")

#Creating SQL database for Munich Vehicle Registration data
new_mvr_df.to_sql("MVR_DATA", createDb, if_exists="replace")

#Creating SQL database for Munich Bike Sharing Data 

new_bs_df.to_sql("BS_DATA", createDb, if_exists="replace")


# Data Summary
print("Munich Vehicle Registration Data Summary:")
print(new_mvr_df.shape)  # Shape of the data frame
print(new_mvr_df.describe())  # Summary statistics
print(new_mvr_df.dtypes)  # Data types of columns

print("Munich Bike Sharing Data Summary:")
print(new_bs_df.shape)  # Shape of the data frame
print(new_bs_df.describe())  # Summary statistics
print(new_bs_df.dtypes)  # Data types of columns

# Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='Year', data=new_mvr_df)
plt.title('Vehicle Registrations by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='In_total', data=new_bs_df)
plt.title('Bike Rentals over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Data Manipulation

# Group the data in new_mvr_df by year and calculate the sum of "altogether" for each year
total_registrations_by_year = new_mvr_df.groupby('Year')['altogether'].sum()

#Average rented bikes per day
avg_bikes_rented_day = new_bs_df.groupby('Date')['In_total'].mean()


# Data Aggregation and Analysis
registrations_by_district = new_mvr_df.groupby('Administrative district')['altogether'].sum()
rentals_by_station = new_bs_df.groupby('Counting_Station')['In_total'].sum()

# ***** Rented bikes per year ******

# Convert the "Date" column in new_bs_df to datetime 
new_bs_df['Date'] = pd.to_datetime(new_bs_df['Date'])
# Extract the year from the "Date" column
new_bs_df['Year'] = new_bs_df['Date'].dt.year
# Group the data by year and calculate the average of "In_total" for each year
average_bikes_rented_by_year = new_bs_df.groupby('Year')['In_total'].mean()

# *****Calculate the correlation*****
# Drop the additional column from the new_bs_df DataFrame
new_bs_df = new_bs_df[new_bs_df['Year'] != 2017]

# Calculate the correlation between the average number of bikes rented and the total number of registrations
correlation = average_bikes_rented_by_year.corr(total_registrations_by_year)

# Plot the correlation graph
plt.scatter(average_bikes_rented_by_year, total_registrations_by_year)
plt.xlabel('Average Bikes Rented per Year')
plt.ylabel('Total Registrations per Year')
plt.title('Correlation between Average Bikes Rented and Total Registrations')
plt.grid(True)
plt.show()


# Print the results
print("Total Registrations per Year:")
print(total_registrations_year)

print("Average Bikes Rented per Day:")
print(avg_bikes_rented_day)

# Print the average number of bikes rented per year for all the years
print(average_bikes_rented)

print("Registrations by Administrative District:")
print(registrations_by_district)

print("Rentals by Counting Station:")
print(rentals_by_station)
