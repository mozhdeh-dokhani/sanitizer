#------------------------- Mozhdeh Dokhani ---------------------------------------
# date:    97/05/02
# version: 1.0
#---------------------------------------------------------------------------------

#------------------------------- Libraries ---------------------------------------
from functions import *
from pprint import pprint
#---------------------------------------------------------------------------------

#------------------------------------ Main ---------------------------------------
if __name__ == "__main__":
    #Huffinfton
    readCsv('../../../dataset/en/news/1-raw/huffington_environment.csv',',',True)
    readCsv('../../../dataset/en/news/1-raw/huffington_food.csv',',',True)
    readCsv('../../../dataset/en/news/1-raw/huffington_health.csv',',',True)
    readCsv('../../../dataset/en/news/1-raw/huffington_lifestyle.csv',',',True)
    readCsv('../../../dataset/en/news/1-raw/huffington_parenting.csv',',',True)
    #CNBC
    readCsv('../../../dataset/en/news/1-raw/cnbc_food.csv',',')
    readCsv('../../../dataset/en/news/1-raw/cnbc_health.csv',',')
    readCsv('../../../dataset/en/news/1-raw/cnbc_lifestyle.csv',',')
    readCsv('../../../dataset/en/news/1-raw/cnbc_science.csv',',')
    readCsv('../../../dataset/en/news/1-raw/cnbc_sport.csv',',')
    readCsv('../../../dataset/en/news/1-raw/cnbc_technology.csv',',')
    #Guardian
    readCsv('../../../dataset/en/news/1-raw/guardian_environment.csv',',')
    readCsv('../../../dataset/en/news/1-raw/guardian_food.csv',',')
    readCsv('../../../dataset/en/news/1-raw/guardian_health.csv',',')
    readCsv('../../../dataset/en/news/1-raw/guardian_lifestyle.csv',',')
    readCsv('../../../dataset/en/news/1-raw/guardian_science.csv',',')
    readCsv('../../../dataset/en/news/1-raw/guardian_sport.csv',',')
    readCsv('../../../dataset/en/news/1-raw/guardian_technology.csv',',')
    readCsv('../../../dataset/en/news/1-raw/guardian_wildlife.csv',',')

    writeCsv('../../../dataset/en/news/2-sanitized/dataset.csv', result)
    # pprint(result) #Print like print_r in php
#---------------------------------------------------------------------------------