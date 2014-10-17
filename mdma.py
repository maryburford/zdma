import csv
import urllib2
import mechanize
import sys
br = mechanize.Browser()

filename = sys.argv[1]

def readCSV(filename):
	zipcodes = []
	csvfile = open(filename, 'rb')
	log = csv.reader(csvfile, delimiter=',')	
	for line in log:
		zipcodes.append(line[0])
	return zipcodes
	
def getDMA(zipcode):
	br = mechanize.Browser()
	url = 'http://www.gilbarco.com/DMA/'
	response = br.open(url)
	br.select_form("dma")
	br.form['zipcode'] = zipcode
	response = br.submit()
	for line in response:
		if 'You are in DMA' in line:
			a,b = line.split('You are in DMA ',2)
			dma,c = b.split(' : ')
			dmaname,donutcare = c.split('</H2>')
			return zipcode, dma, dmaname
			
	
if __name__ == "__main__":
	csvfile = open(filename.replace('.csv','')+'_output.csv', 'wb')
	writezips = csv.writer(csvfile, delimiter=',')

	for zipcode in readCSV(filename):
		output = getDMA(zipcode)
		print output
		writezips.writerow([output[0],output[1],output[2]])

