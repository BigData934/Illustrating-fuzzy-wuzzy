
from fuzzywuzzy import fuzz

list_of_possible_companies = ["Microsoft Corp","Alphabet Inc.","Amazon.com, Inc.","Meta Platforms, Inc","The Bank of America Corp"]

company_to_test = "Bank of America Corporation"

for possible_company in list_of_possible_companies:
	ratio = fuzz.ratio(company_to_test,possible_company)
	print(company_to_test, " ||| ", possible_company, " ||| ", ratio)
