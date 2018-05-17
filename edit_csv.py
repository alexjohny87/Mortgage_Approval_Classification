import csv, os

with open('ny_hmda_2015.csv', 'r') as inf, open('ny_hmda_2015_CLEANED_data.csv', 'w') as outf:
	reader = csv.reader(inf)
	writer = csv.writer(outf)
	for line in reader:
		if line[0] == '1' or line[0] == '2' or line[0] == '6':
			print("hit")
			line[0] = '1'
 			writer.writerow(line)
		else: #line[0] == '3' || line[0] == '5' || line[0] == '7' || line[0] == '4':
			line[0] = '0'			
			writer.writerow(line)    

os.remove('ny_hmda_2015.csv')
os.rename('ny_hmda_2015_CLEANED_data.csv', 'ny_hmda_2015.csv')
