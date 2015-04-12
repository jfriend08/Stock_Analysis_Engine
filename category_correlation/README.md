#Stock_Analysis_Engine
This is the directory for category correlation

#Working data source
Google Drive [link](https://drive.google.com/open?id=0BzG5zLRRrgKwfkthYmJhdW94aUE1QVpDeTN4bnhsVDJuNmJSZ1d2aElaSExJaUVpWWs5ZDg&authuser=0)

#Steps:
##Combine raw data
- Merge stock close price for the past 360 days
- Append market cap and industury category
- Output: ClosePrice_360days.txt

>`./bin/preprocess_merge.R`

##Compute MarketCap percentage in each specific industry
- First pass to calculate the total marketCap for each industry
- Second pass to get the precentage of that stock in that industry
- Third pass to append MarketCap percentage info accordingly
- Output: ClosePrice_360days_complete.txt

>`cat ClosePrice_360days.txt|python ./src/preprocess_marketCap.py>ClosePrice_360days_complete.txt`

##Checks have been done
- Checked the industry of "Wholesale Distributors", and the percentage is correct
- Checked the stock "ZBK". Its marketCap is n/a, so the percentage is 0

#Analytic Works:
##Step 1: Get the index-weighted price-differences for each of industry
- Data Source: ./constant/PriceDiff_360days.txt. Definition of PriceDiff: Price_Day1_Close - Price_Day2_Close
- Mapper output

>`[IndustryA, Day1_PriceDiff1*weight_Company1], ..., [IndustryA, Day365_PriceDiff365*weight_Company1], 
[IndustryA, Day1_PriceDiff1*weight_Company2], ..., [IndustryA, Day365_PriceDiff365*weight_Company2], 
[IndustryB, Day1_PriceDiff1*weight_Company7], ..., [IndustryB, Day365_PriceDiff365*weight_Company7],
[IndustryB, Day1_PriceDiff1*weight_Company8], ..., [IndustryB, Day365_PriceDiff365*weight_Company8],`
- Hadoop will partition the Industry(key) to reducer
- Reducer output: 




##ToDos
- Double check readme
- Double check source code
- Double check correctness of processed data
- Start coding!