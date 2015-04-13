from mrjob.job import MRJob
from itertools import groupby
from operator import itemgetter, attrgetter

MRJob.SORT_VALUES = True

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        fields = line.strip().split('\t')   
        stock = fields[0]
        info = fields[1]
        info = info[1: len(info) - 1]

        industry = info.split(',')

        for x in industry:
            detail = x.split(':')
            industry_name = detail[0][2:len(detail[0]) - 1]
            count = detail[1]

            print stock + " " + count + " " + industry_name
            #yield stock, ()

        #print industry[len(industry) - 1]

        yield stock, 1

        #yield words[0], (int(words[1]), "industry_name")

    def reducer(self, key, values):

        yield key, sum(values)

        '''
        for d in values:
            line_data='\t'.join(str(n) for n in d)
            print key + " " + str(line_data)
        '''
        '''
    	values = sorted(values, key=lambda x: x[1])
    	count = 0

    	for d in values:
    		if count < 2:
    			line_data='\t'.join(str(n) for n in d)
        		print key + " " + str(line_data)
        		count += 1
        '''

if __name__ == '__main__':
    MRWordFrequencyCount.run()