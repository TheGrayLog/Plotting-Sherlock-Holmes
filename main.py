#plan: show that you should buy nft's.
import matplotlib.pyplot as plt
import pandas as pd


columns = ['Sales_USD_cumsum','Number_of_Sales_cumsum','Active_Market_Wallets_cumsum','Primary_Sales_cumsum','Secondary_Sales_cumsum','AverageUSD_cum','Sales_USD','Number_of_Sales','Active_Market_Wallets','Primary_Sales']

data = pd.read_csv("NFT_Sales.csv")

#Data found @ Line 1344 under the csv
Sales_USD_cumsum = data('332589970.32')
Active_Market_Wallets_cumsum = ('5340354')
Primary_Sales_cumsum = ('225978.0')
Secondary_Sales_cumsum = ('3411365')
AverageUSD_cum = ('1902.0')[y]
Sales_USD = ('62.28')[y]
Number_of_Sales = ('15636076.329999983')
Active_Market_Wallets = ('3649.0')
Primary_Sales = ('1021.0')
plt.bar(columns)
plt.xlabel('Number Avabile')
plt.ylabel('Number of NFTs Sold')
plt.show()




