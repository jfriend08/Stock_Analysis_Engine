# Correlation computing

###Plan A:
The Hadoop Streaming Python will take a file as input flow, but we need to compute the price difference within one day,which requires both the open price and close price. I add one more step on preprocess to calcualte the daily price difference. 

###Plan B
However, the raw data of daily price contains both the open price and close price in one day, why don't we take advantage of that and try to use a mapper to do the preprocess.