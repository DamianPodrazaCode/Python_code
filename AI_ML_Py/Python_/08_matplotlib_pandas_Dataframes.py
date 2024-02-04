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



# x = np.random.randn(1000)
# nut_butter_prices = {'Almond butter': 10,
#                      'Penaut butter': 8,
#                      'Cashew butter': 12}

# # ------------------------------------------------------------------------------------
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# ax1.plot(x, x/2)
# ax2.scatter(np.random.random(10), np.random.random(10))
# ax3.bar(nut_butter_prices.keys(), nut_butter_prices.values())
# ax4.hist(x)

# # ------------------------------------------------------------------------------------
# fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# ax[0, 0].plot(x, x/2)
# ax[0, 1].scatter(np.random.random(10), np.random.random(10))
# ax[1, 0].bar(nut_butter_prices.keys(), nut_butter_prices.values())
# ax[1, 1].hist(x)

plt.show()