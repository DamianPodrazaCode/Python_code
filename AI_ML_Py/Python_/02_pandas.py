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

# import matplotlib.pyplot as plt
car_sales['Odometer (KM)'].plot()
plt.show()



# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
