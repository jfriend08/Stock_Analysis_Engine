#Stock_Analysis_Engine
This is the directory for category correlation

#Working data source
https://drive.google.com/open?id=0BzG5zLRRrgKwMmNHX0EybWdZanM&authuser=0

#Steps:
##Combine raw data
- merge stock close price for the past 360 days
- append market cap and industury category
- output:ClosePrice_360days.txt

>`./bin/preprocess_merge.R`

##Compute MarketCap percentage in each specific industry
- First pass to calculate the total marketCap for each industry
- Second pass to get the precentage of that stock in that industry
- Third pass to append MarketCap percentage info accordingly

>`cat ClosePrice_360days.txt|python ../../Stock_Analysis_Engine/category_correlation/src/preprocess_marketCap.py>ClosePrice_360days_complete.txt`