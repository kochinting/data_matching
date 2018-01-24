# data_matching
This is a data matching script to match csv file "match_file.csv" to json file "source_data.json"
### Doctor Match:
- NPI
- first name + last name + full address

### Practice Match:
- full address

## Output Result:
- Num of total documents scanned: 1265
- Num of Doctors matched with NPI: 864
- Num of Practices matched with address: 921
- Num of Doctors matched with name and address: 921
- Num of documents that could not be matched: : 171
- Num of documents that matched: : 1094

#### data_matching.py:
python script to match csv file "match_file.csv" to json file "source_data.json"
#### match_file.csv:
original input match file
#### match_result.csv:
orginal input match file with detailed match results
#### output_file.txt:
summary match result output
#### source_data.json:
source data for matching

## Author: Chin-Ting Ko (Tim)
## Date: 01/23/2017


