from mrjob.job import MRJob
from itertools import groupby
from operator import itemgetter, attrgetter

MRJob.SORT_VALUES = True

class MRWordFrequencyCount(MRJob):
	
    def mapper(self, _, line):
        fields = line.strip().split('\t')
        stock = fields[0]
		
        info = eval(fields[1])
		
        for x in info:
            #industry_name = x[1]
            industry_name = x
			
            #print stock, (int(info[x]), industry_name)
			
            #print stock, int(info[x]), industry_name
            yield stock, (int(info[x]), industry_name)
	
	#yield words[0], (int(words[1]), "industry_name")
	
    def reducer(self, key, values):
		
        values = sorted(values, key=lambda x: x[0], reverse = True)
        count = 0
		
        output = []
        output.append(key)
		
        #info = {}
        info = []
		
        for d in values:
            if count < 10:
                count += 1
                item = str(d[0]) + " " + str(d[1])
                info.append(item)
		
        output.append(info)
		
        yield output

if __name__ == '__main__':
    MRWordFrequencyCount.run()