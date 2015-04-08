# Stock_Analysis_Engine
Using Hadoop to analyze stock market


The project provides the US stock investors an intelligent stock analytical tool to help them make wise investment decisions. The basic idea underneath is to effectively apply advanced analytical technologies (including statistical analysis, machine learning, data mining and natural language processing, etc.) under the framework of ?Big Data Technology?. New information related to stock price and company financial performance is being produced from various sources on a daily basis. In order to take advantage of the overwhelming amount of realtime information and to make timely investment decisions, investors need an intelligent system to help them get useful insights, not only historical facts, but realtime analysis results as well, in just a second. Our project is built on both historical and realtime data/information, and delivers investment analysis to users. Specifically, the first potential topic is to analyze the correlation-behavior between different stocks? price. We will apply MapReduce to figure out the pattern of price movement between any two stocks based on daily/weekly updated data sources. Stocks that have similar behavior or totally opposite behavior will be ranked and presented to users, who will use the information to dig out potential investment opportunities. The second topic would be financial report analysis for each company. Several important key-ratios that reflect the performance of the company will be calculated and compared across the industry/market. The complicated computation is also based on MapReduce method, and the data is updated quarterly/yearly. The third goal is to use NLP technology to parse text information/opinions from equity research websites. Sentimental analysis will be made and the result will serve as an indicator for investors. The last topic is to conduct machine learning algorithms for stock price or financial statement to dig out hidden information that might be useful for decision making.