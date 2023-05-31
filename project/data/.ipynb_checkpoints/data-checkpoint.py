import pandas as pd
from sqlalchemy import create_engine
import openpyxl

#**************Importing Munich Vehicle Registration Data**************
#MVR = Munich Vehicle Registration Data




MVR_df = pd.read_excel('https://opendata.stadt-muenster.de/sites/default/files/Fahrzeugbestand-Regierungsbezirk-Muenster-2018-2022.xlsx',skiprows=1)
print(MVR_df)

#**************Importing Munich Bike Sharing Data**************
#BS= Munich Bike Sharing 



BS_df = pd.read_csv(r"C:\Users\Alimu\Downloads\rad_tage.csv")
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