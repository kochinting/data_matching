"""
This is a data matching script to match csv file "match_file.csv" to json file "source_data.json"
* Doctor Match
NPI
first name + last name + full address

* Practice Match
full address

* Output:
# of total documents scanned: 1265
# of Doctors matched with NPI: 864
# of Practices matched with address: 921
# of Doctors matched with name and address: 921
# of documents that could not be matched: : 171

author: Chin-Ting Ko (Tim)
date: 01/23/2017
"""

import pandas as pd
from pprint import pprint

# generate output file for output result
output_file = open("output_file.txt", "w")
# read json file to pandas data frame
source = pd.read_json('source_data.json', lines=True)
#pprint(source['doctor'][0]['npi'])

# read match raw csv file to pandas data frame
match = pd.read_csv('match_file.csv')
print '# of total documents scanned: ', len(match.index)
output_file.write('# of total documents scanned: ' + str(len(match.index)) + '\n')
#print match['npi']

# below is to match doctor NPI
npi_match = 0
# NPI count result
npi_list = []
# for reach match record, track NPI match result
for match_npi in match['npi']:
    if str(match_npi) != 'nan':
        # handle missing value
        npi_list.append(False)
        for source_doctor_data in source['doctor']:
            if str(match_npi) in str(source_doctor_data['npi']):
                npi_match += 1
                npi_list[-1] = True
                # This represent this record found NPI match

    if str(match_npi) == 'nan':
        npi_list.append(False)

print '# of Doctors matched with NPI: ', str(npi_match)
output_file.write('# of Doctors matched with NPI: ' + str(npi_match) + '\n')


# below is to match pratices address
practices_address_match = 0
practices_list = []
match_addresses = match['street'] + match['street_2'] + match['city'] + match['state'] + match['zip']

for match_address in match_addresses:
    if str(match_address) != 'nan':
        practices_list.append(False)

        for practices_data in source['practices']:
            for practice in practices_data:
                practice_address = practice['street'] + practice['street_2'] + practice['city'] + practice['state'] + \
                                   practice['zip']

                if str(match_address).lower() in str(practice_address).lower():
                    practices_address_match += 1
                    practices_list[-1] = True
                    #print match_address
    if str(match_address) == 'nan':
        practices_list.append(False)

print '# of Practices matched with address: ', str(practices_address_match)
output_file.write('# of Practices matched with address: ' + str(practices_address_match) + '\n')


# below is to match doctor name and address
name_address_match = 0
name_address_list = []
match_name_addresses = match['first_name'] + match['last_name'] + match['street'] + match['street_2'] + match['city'] \
                       + match['state'] + match['zip']
for match_name_address in match_name_addresses:
    if str(match_name_address) != 'nan':
        name_address_list.append(False)

        for doctor_data, practices_data in zip(source['doctor'], source['practices']):
            for practice in practices_data:
                name_address = doctor_data['first_name'] + doctor_data['last_name'] + practice['street'] \
                               + practice['street_2'] + practice['city'] + practice['state'] + practice['zip']
                if str(match_name_address).lower() in str(name_address).lower():
                    name_address_match += 1
                    name_address_list[-1] = True
                    #print match_name_address
    if str(match_name_address) == 'nan':
        name_address_list.append(False)

print '# of Doctors matched with name and address: ', str(name_address_match)
output_file.write('# of Doctors matched with name and address: ' + str(name_address_match) + '\n')


# This is to generate matching result for each match records.
match['NPI'] = npi_list
match['NAME_ADDRESS'] = name_address_list
match['PRACTICES'] = practices_list
match['MATCH'] = match['NPI'] | match['NAME_ADDRESS'] | match['PRACTICES']
# logic OR operation

match_true = match[match['MATCH'] == True]
match_false = match[match['MATCH'] == False]
#print match_false

print '# of documents that could not be matched: ', len(match_false.index)
output_file.write('# of documents that could not be matched: : ' + str(len(match_false.index)) + '\n')
output_file.close()

match.to_csv('match_result.csv')
# output match result file
