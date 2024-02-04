import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2020', periods=1000))
print(ts)
# 2020-01-01    0.496714
# 2020-01-02   -0.138264
# 2020-01-03    0.647689
# 2020-01-04    1.523030
# 2020-01-05   -0.234153
#                 ...
# 2022-09-22   -0.281100
# 2022-09-23    1.797687
# 2022-09-24    0.640843
# 2022-09-25   -0.571179
# 2022-09-26    0.572583
# Freq: D, Length: 1000, dtype: float64

ts = ts.cumsum()
print(ts)
# 2020-01-01     0.496714
# 2020-01-02     0.358450
# 2020-01-03     1.006138
# 2020-01-04     2.529168
# 2020-01-05     2.295015
#                 ...
# 2022-09-22    16.892123
# 2022-09-23    18.689809
# 2022-09-24    19.330652
# 2022-09-25    18.759473
# 2022-09-26    19.332056
# Freq: D, Length: 1000, dtype: float64

# ts.plot()

car_sales = pd.read_csv('Python_\car-sales.csv')
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

car_sales['Price'] = car_sales['Price'].str.replace('$', '').str.replace(',', '').str.replace('.00', '')
# car_sales['Price'] = car_sales['Price'].str[:-2]
print(car_sales)
#      Make Colour  Odometer (KM)  Doors  Price
# 0  Toyota  White         150043      4   4000
# 1   Honda    Red          87899      4   5000
# 2  Toyota   Blue          32549      3   7000
# 3     BMW  Black          11179      5  22000
# 4  Nissan  White         213095      4   3500
# 5  Toyota  Green          99213      4   4500
# 6   Honda   Blue          45698      4   7500
# 7   Honda   Blue          54738      4   7000
# 8  Toyota  White          60000      4   6250
# 9  Nissan  White          31600      4   9700

car_sales['Price'] = car_sales['Price'].astype(int) # zamiana z str na int
car_sales['Sale Date'] = pd.date_range('1/1/2020', periods=len(car_sales))
print(car_sales)
#      Make Colour  Odometer (KM)  Doors  Price  Sale Date
# 0  Toyota  White         150043      4   4000 2020-01-01
# 1   Honda    Red          87899      4   5000 2020-01-02
# 2  Toyota   Blue          32549      3   7000 2020-01-03
# 3     BMW  Black          11179      5  22000 2020-01-04
# 4  Nissan  White         213095      4   3500 2020-01-05
# 5  Toyota  Green          99213      4   4500 2020-01-06
# 6   Honda   Blue          45698      4   7500 2020-01-07
# 7   Honda   Blue          54738      4   7000 2020-01-08
# 8  Toyota  White          60000      4   6250 2020-01-09
# 9  Nissan  White          31600      4   9700 2020-01-10

car_sales['Total Sales'] = car_sales['Price'].cumsum()
print(car_sales)
#      Make Colour  Odometer (KM)  Doors  Price  Sale Date  Total Sales
# 0  Toyota  White         150043      4   4000 2020-01-01         4000
# 1   Honda    Red          87899      4   5000 2020-01-02         9000
# 2  Toyota   Blue          32549      3   7000 2020-01-03        16000
# 3     BMW  Black          11179      5  22000 2020-01-04        38000
# 4  Nissan  White         213095      4   3500 2020-01-05        41500
# 5  Toyota  Green          99213      4   4500 2020-01-06        46000
# 6   Honda   Blue          45698      4   7500 2020-01-07        53500
# 7   Honda   Blue          54738      4   7000 2020-01-08        60500
# 8  Toyota  White          60000      4   6250 2020-01-09        66750
# 9  Nissan  White          31600      4   9700 2020-01-10        76450

# car_sales.plot(x='Sale Date', y='Total Sales')
# car_sales.plot(x='Odometer (KM)', y='Price', kind='bar')
# car_sales.plot(x='Odometer (KM)', y='Price', kind='scatter')

x = np.random.rand(10, 4)
print(x)
# [[0.16748258 0.10456784 0.63643025 0.70647573]
#  [0.03158614 0.93621225 0.05197128 0.54129634]
#  [0.70906052 0.87096912 0.71408693 0.80172808]
#  [0.33945019 0.81482511 0.08011485 0.89481666]
#  [0.54759238 0.81729777 0.45231828 0.6435777 ]
#  [0.52640266 0.73158952 0.08162998 0.06035208]
#  [0.24710323 0.15954468 0.87178357 0.21921399]
#  [0.97586526 0.33689579 0.18211792 0.78969851]
#  [0.65870778 0.49819572 0.55536355 0.71920178]
#  [0.22845474 0.99633392 0.97479316 0.65032569]]

df = pd.DataFrame(x, columns=['a', 'b', 'c', 'd'])
print(df)
#           a         b         c         d
# 0  0.167483  0.104568  0.636430  0.706476
# 1  0.031586  0.936212  0.051971  0.541296
# 2  0.709061  0.870969  0.714087  0.801728
# 3  0.339450  0.814825  0.080115  0.894817
# 4  0.547592  0.817298  0.452318  0.643578
# 5  0.526403  0.731590  0.081630  0.060352
# 6  0.247103  0.159545  0.871784  0.219214
# 7  0.975865  0.336896  0.182118  0.789699
# 8  0.658708  0.498196  0.555364  0.719202
# 9  0.228455  0.996334  0.974793  0.650326

# df.plot.bar()
# lub
# df.plot(kind='bar')

print(car_sales)
#      Make Colour  Odometer (KM)  Doors  Price  Sale Date  Total Sales
# 0  Toyota  White         150043      4   4000 2020-01-01         4000
# 1   Honda    Red          87899      4   5000 2020-01-02         9000
# 2  Toyota   Blue          32549      3   7000 2020-01-03        16000
# 3     BMW  Black          11179      5  22000 2020-01-04        38000
# 4  Nissan  White         213095      4   3500 2020-01-05        41500
# 5  Toyota  Green          99213      4   4500 2020-01-06        46000
# 6   Honda   Blue          45698      4   7500 2020-01-07        53500
# 7   Honda   Blue          54738      4   7000 2020-01-08        60500
# 8  Toyota  White          60000      4   6250 2020-01-09        66750
# 9  Nissan  White          31600      4   9700 2020-01-10        76450

# car_sales.plot(x='Make', y='Odometer (KM)', kind='bar')
# car_sales.plot(x='Make', y=['Odometer (KM)', 'Price'], kind='bar')

# car_sales["Odometer (KM)"].plot.hist()
# lub
# car_sales["Odometer (KM)"].plot(kind="hist")

# car_sales["Odometer (KM)"].plot.hist(bins=20) # ilość słupków
# car_sales["Odometer (KM)"].plot.hist(bins=50)


plt.show()