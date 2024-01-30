import pandas as pd

# -----------------------------------------------------------------------------

# Series są jednowymiarowe (1-dimensional)
series = pd.Series(['bmw', 'toyota', 'honda'])
print(series)
# 0       bmw
# 1    toyota
# 2     honda
# dtype: object

colours = pd.Series(['red', 'green', 'blue'])
print(colours)
# 0      red
# 1    green
# 2     blue
# dtype: object

# DataFrame są dwuwymiarowe (2-dimensional) i są tworzone z serii
car_data = pd.DataFrame({'car make':series, 'colour':colours})
print(car_data)
#   car make colour
# 0      bmw    red
# 1   toyota  green
# 2    honda   blue

# -----------------------------------------------------------------------------\
    
# Import data *.CSV
car_sales = pd.read_csv('Python_/car-sales.csv')
print(car_sales)
#      Make Colour  Odometer (KM)  Doors       Price
# 0  Toyota  White         150043      4   $4,000.00
# 1   Honda    Red          87899      4   $5,000.00
# 2  Toyota   Blue          32549      3   $7,000.00
# 3     BMW  Black          11179      5  $22,000.00
# 4  Nissan  White         213095      4   $3,500.00
# 5  Toyota  Green          99213      4   $4,500.00
# 6   Honda   Blue          45698      4   $7,500.00
# 7   Honda   Blue          54738      4   $7,000.00
# 8  Toyota  White          60000      4   $6,250.00
# 9  Nissan  White          31600      4   $9,700.00

# Export data
car_sales.to_csv('Python_/export-car-sales.csv', index=False) #index False nie zapisuje indexowani czyli pierwszej kolumny
# -----------------------------------------------------------------------------s

# OPIS DATYCH

print(car_sales.dtypes)
# Make             object
# Colour           object
# Odometer (KM)     int64
# Doors             int64
# Price            object
# dtype: object

print(car_sales.columns) 
# Index(['Make', 'Colour', 'Odometer (KM)', 'Doors', 'Price'], dtype='object')

print(car_sales.index) 
# RangeIndex(start=0, stop=10, step=1)

print(car_sales.describe()) 
#        Odometer (KM)      Doors
# count      10.000000  10.000000
# mean    78601.400000   4.000000
# std     61983.471735   0.471405
# min     11179.000000   3.000000
# 25%     35836.250000   4.000000
# 50%     57369.000000   4.000000
# 75%     96384.500000   4.000000
# max    213095.000000   5.000000

print(car_sales.info()) 
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   Make           10 non-null     object
#  1   Colour         10 non-null     object
#  2   Odometer (KM)  10 non-null     int64
#  3   Doors          10 non-null     int64
#  4   Price          10 non-null     object
# dtypes: int64(2), object(3)
# memory usage: 532.0+ bytes
# None

car_prices = pd.Series([3000, 1500, 111250])
print(car_prices.mean())
# 38583.333333333336

print(car_sales.sum())
# Make             ToyotaHondaToyotaBMWNissanToyotaHondaHondaToyo...
# Colour               WhiteRedBlueBlackWhiteGreenBlueBlueWhiteWhite
# Odometer (KM)                                               786014
# Doors                                                           40
# Price            $4,000.00$5,000.00$7,000.00$22,000.00$3,500.00...
# dtype: object

print(car_sales['Doors'])
# 0    4
# 1    4
# 2    3
# 3    5
# 4    4
# 5    4
# 6    4
# 7    4
# 8    4
# 9    4
# Name: Doors, dtype: int64

print(car_sales['Doors'].mean())
# 4.0

print(car_sales['Doors'].sum())
# 40

print(len(car_sales))
# 10

print(car_sales['Doors'][2])
# 3
# -----------------------------------------------------------------------------
# PODGLĄD i WYBIERANIE DANYCH

print(car_sales)
#      Make Colour  Odometer (KM)  Doors       Price
# 0  Toyota  White         150043      4   $4,000.00
# 1   Honda    Red          87899      4   $5,000.00
# 2  Toyota   Blue          32549      3   $7,000.00
# 3     BMW  Black          11179      5  $22,000.00
# 4  Nissan  White         213095      4   $3,500.00
# 5  Toyota  Green          99213      4   $4,500.00
# 6   Honda   Blue          45698      4   $7,500.00
# 7   Honda   Blue          54738      4   $7,000.00
# 8  Toyota  White          60000      4   $6,250.00
# 9  Nissan  White          31600      4   $9,700.00

print(car_sales.head()) # mały wycinek
#      Make Colour  Odometer (KM)  Doors       Price
# 0  Toyota  White         150043      4   $4,000.00
# 1   Honda    Red          87899      4   $5,000.00
# 2  Toyota   Blue          32549      3   $7,000.00
# 3     BMW  Black          11179      5  $22,000.00
# 4  Nissan  White         213095      4   $3,500.00

print(car_sales.head(7)) # wycinek o określonej długości
#      Make Colour  Odometer (KM)  Doors       Price
# 0  Toyota  White         150043      4   $4,000.00
# 1   Honda    Red          87899      4   $5,000.00
# 2  Toyota   Blue          32549      3   $7,000.00
# 3     BMW  Black          11179      5  $22,000.00
# 4  Nissan  White         213095      4   $3,500.00
# 5  Toyota  Green          99213      4   $4,500.00
# 6   Honda   Blue          45698      4   $7,500.00

animals = pd.Series(['cat', 'dog', 'bird', 'panda', 'snake'])
print(animals)
# 0      cat
# 1      dog
# 2     bird
# 3    panda
# 4    snake
# dtype: object
animals = pd.Series(['cat', 'dog', 'bird', 'panda', 'snake'], index=[0,2,4,1,4])
print(animals)
# 0       cat
# 2       dog
# 4      bird
# 1     panda
# 34    snake
# dtype: object

print(animals.loc[4])
# 4     bird
# 4    snake
# dtype: object

print(animals.loc[1]) # wskazanie po oznaczeniu indeksu
# panda

print(animals.iloc[1]) # wskazanie po rzeczywistej pozycji od 0
# dog

print(animals.iloc[:2])
# 0    cat
# 2    dog

print(animals.iloc[1:4])
# 2      dog
# 4     bird
# 1    panda

print(car_sales.loc[2])
# Make                Toyota
# Colour                Blue
# Odometer (KM)        32549
# Doors                    3
# Price            $7,000.00
# Name: 2, dtype: object

print(car_sales.loc[:2])
#      Make Colour  Odometer (KM)  Doors      Price
# 0  Toyota  White         150043      4  $4,000.00
# 1   Honda    Red          87899      4  $5,000.00
# 2  Toyota   Blue          32549      3  $7,000.00

print(car_sales.loc[2:5])
#      Make Colour  Odometer (KM)  Doors       Price
# 2  Toyota   Blue          32549      3   $7,000.00
# 3     BMW  Black          11179      5  $22,000.00
# 4  Nissan  White         213095      4   $3,500.00
# 5  Toyota  Green          99213      4   $4,500.00 

print(car_sales['Make'])
# 0    Toyota
# 1     Honda
# 2    Toyota
# 3       BMW
# 4    Nissan
# 5    Toyota
# 6     Honda
# 7     Honda
# 8    Toyota
# 9    Nissan
# Name: Make, dtype: object

print(car_sales.Make) # to samo co wyżej tylko z tą różnicą że jak nazwa kolumny będzie ze spacją to niezadziała
# 0    Toyota
# 1     Honda
# 2    Toyota
# 3       BMW
# 4    Nissan
# 5    Toyota
# 6     Honda
# 7     Honda
# 8    Toyota
# 9    Nissan
# Name: Make, dtype: object

print(car_sales.Make.loc[2])
# Toyota

print(car_sales.Make[2])
# Toyota

print(car_sales[car_sales['Make'] == 'Toyota'])
#      Make Colour  Odometer (KM)  Doors      Price
# 0  Toyota  White         150043      4  $4,000.00
# 2  Toyota   Blue          32549      3  $7,000.00
# 5  Toyota  Green          99213      4  $4,500.00
# 8  Toyota  White          60000      4  $6,250.00

print(car_sales[car_sales["Odometer (KM)"] > 100000 ])
#      Make Colour  Odometer (KM)  Doors      Price
# 0  Toyota  White         150043      4  $4,000.00
# 4  Nissan  White         213095      4  $3,500.00

# -----------------------------------------------------------------------------

print(pd.crosstab(car_sales['Make'], car_sales['Doors']))
# Doors   3  4  5
# Make
# BMW     0  0  1
# Honda   0  3  0
# Nissan  0  2  0
# Toyota  1  3  0

print(car_sales.groupby(["Make"]).mean(True)) # grupuje kolumny te które może uśrednić (int, float), łączy wg. klucza, i uśrenia połączone
#         Odometer (KM)  Doors
# Make
# BMW      11179.000000   5.00
# Honda    62778.333333   4.00
# Nissan  122347.500000   4.00
# Toyota   85451.250000   3.75

print(car_sales.groupby(['Colour']).mean(True))
# Colour
# Black    11179.000000  5.000000
# Blue     44328.333333  3.666667
# Green    99213.000000  4.000000
# Red      87899.000000  4.000000
# White   113684.500000  4.000000

import matplotlib.pyplot as plt
#car_sales['Odometer (KM)'].plot()
# car_sales['Odometer (KM)'].hist()
# plt.show()

car_sales['Price'] = car_sales['Price'].str.replace('$', '').str.replace(',', '').str.replace('.', '').astype(int)
print(car_sales)

#      Make Colour  Odometer (KM)  Doors    Price
# 0  Toyota  White         150043      4   400000
# 1   Honda    Red          87899      4   500000
# 2  Toyota   Blue          32549      3   700000
# 3     BMW  Black          11179      5  2200000
# 4  Nissan  White         213095      4   350000
# 5  Toyota  Green          99213      4   450000
# 6   Honda   Blue          45698      4   750000
# 7   Honda   Blue          54738      4   700000
# 8  Toyota  White          60000      4   625000
# 9  Nissan  White          31600      4   970000

# car_sales['Price'].plot()
# plt.show()

# -----------------------------------------------------------------------------
# MANIPULACJA DANYMI
car_sales['Make'] = car_sales['Make'].str.lower()
print(car_sales['Make'])
# 0    toyota
# 1     honda
# 2    toyota
# 3       bmw
# 4    nissan
# 5    toyota
# 6     honda
# 7     honda
# 8    toyota
# 9    nissan
# Name: Make, dtype: object

car_sales_missing = pd.read_csv('Python_/car-sales-missing-data.csv')
print(car_sales_missing)
#      Make Colour  Odometer (KM)  Doors       Price
# 0  Toyota  White       150043.0    4.0   $4,000.00
# 1   Honda    Red        87899.0    NaN   $5,000.00
# 2  Toyota   Blue        32549.0    NaN   $7,000.00
# 3     BMW    NaN        11179.0    5.0  $22,000.00
# 4  Nissan  White       213095.0    4.0   $3,500.00
# 5  Toyota  Green            NaN    4.0   $4,500.00
# 6   Honda   Blue        45698.0    4.0   $7,500.00
# 7   Honda   Blue        54738.0    4.0   $7,000.00
# 8  Toyota  White        60000.0    4.0         NaN
# 9  Nissan    NaN        31600.0    4.0   $9,700.00

car_sales_missing['Odometer (KM)'] = car_sales_missing['Odometer (KM)'].fillna(car_sales_missing['Odometer (KM)'].mean()) # wypełnianie braku średnią z columny
car_sales_missing['Odometer (KM)'] = car_sales_missing['Odometer (KM)'].round() 
car_sales_missing['Doors'] = car_sales_missing['Doors'].fillna(car_sales_missing['Doors'].mean())
car_sales_missing['Doors'] = car_sales_missing['Doors'].round(decimals=0)
print(car_sales_missing)
#      Make Colour  Odometer (KM)  Doors       Price
# 0  Toyota  White       150043.0    4.0   $4,000.00
# 1   Honda    Red        87899.0    4.1   $5,000.00
# 2  Toyota   Blue        32549.0    4.1   $7,000.00
# 3     BMW    NaN        11179.0    5.0  $22,000.00
# 4  Nissan  White       213095.0    4.0   $3,500.00
# 5  Toyota  Green        76311.0    4.0   $4,500.00
# 6   Honda   Blue        45698.0    4.0   $7,500.00
# 7   Honda   Blue        54738.0    4.0   $7,000.00
# 8  Toyota  White        60000.0    4.0         NaN
# 9  Nissan    NaN        31600.0    4.0   $9,700.00

car_sales_missing = car_sales_missing.dropna() # porzuca wiersze które mają nan-y
#car_sales_missing.dropna(inplace=True) # inplace=True powoduje przypisanie jak wyżej
print(car_sales_missing)
#      Make Colour  Odometer (KM)  Doors      Price
# 0  Toyota  White       150043.0    4.0  $4,000.00
# 1   Honda    Red        87899.0    4.0  $5,000.00
# 2  Toyota   Blue        32549.0    4.0  $7,000.00
# 4  Nissan  White       213095.0    4.0  $3,500.00
# 5  Toyota  Green        76311.0    4.0  $4,500.00
# 6   Honda   Blue        45698.0    4.0  $7,500.00
# 7   Honda   Blue        54738.0    4.0  $7,000.00

# -----------------------------------------------------------------------------

# Columny z serii

# dodanie nowej kolumny

seats_column = pd.Series([5,5,5,5,5]) # nowa seria, może mieć mniej pól niż tabela wierszy, reszta uzupełni się nan
car_sales['Seats'] = seats_column
print(car_sales)
#      Make Colour  Odometer (KM)  Doors    Price  Seats
# 0  toyota  White         150043      4   400000    5.0
# 1   honda    Red          87899      4   500000    5.0
# 2  toyota   Blue          32549      3   700000    5.0
# 3     bmw  Black          11179      5  2200000    5.0
# 4  nissan  White         213095      4   350000    5.0
# 5  toyota  Green          99213      4   450000    NaN
# 6   honda   Blue          45698      4   750000    NaN
# 7   honda   Blue          54738      4   700000    NaN
# 8  toyota  White          60000      4   625000    NaN
# 9  nissan  White          31600      4   970000    NaN

car_sales['Seats'].fillna(5, inplace=True) # wypełnienie pustych, bez nadpisywania (inplace=True)
print(car_sales)
#      Make Colour  Odometer (KM)  Doors    Price  Seats
# 0  toyota  White         150043      4   400000    5.0
# 1   honda    Red          87899      4   500000    5.0
# 2  toyota   Blue          32549      3   700000    5.0
# 3     bmw  Black          11179      5  2200000    5.0
# 4  nissan  White         213095      4   350000    5.0
# 5  toyota  Green          99213      4   450000    5.0
# 6   honda   Blue          45698      4   750000    5.0
# 7   honda   Blue          54738      4   700000    5.0
# 8  toyota  White          60000      4   625000    5.0
# 9  nissan  White          31600      4   970000    5.0

# kolumny z list python-a

fuel_economy = [7.5, 9.2, 5.0, 9.6, 8.7, 3.4, 5.6, 7.8, 9.1, 4.3] # lista musi mieć tyle pól ile tablica ma wierszy
car_sales['Fuel per 100KM'] = fuel_economy
# car_sales['Fuel per 100KM'] = pd.Series(fuel_economy) # jeżeli nie ma pełnej listy można konwertować do panda series
print(car_sales)
#      Make Colour  Odometer (KM)  Doors    Price  Seats  Fuel per 100KM
# 0  toyota  White         150043      4   400000    5.0             7.5
# 1   honda    Red          87899      4   500000    5.0             9.2
# 2  toyota   Blue          32549      3   700000    5.0             5.0
# 3     bmw  Black          11179      5  2200000    5.0             9.6
# 4  nissan  White         213095      4   350000    5.0             8.7
# 5  toyota  Green          99213      4   450000    5.0             3.4
# 6   honda   Blue          45698      4   750000    5.0             5.6
# 7   honda   Blue          54738      4   700000    5.0             7.8
# 8  toyota  White          60000      4   625000    5.0             9.1
# 9  nissan  White          31600      4   970000    5.0             2.3

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
