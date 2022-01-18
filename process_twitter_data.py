from query_builder import QueryBuilder
from formatting_data import FormatingExcel

searchCountry = input("Enter country to search= ")

def proccessTwitterData():

    get_query = QueryBuilder(searchCountry)
    twitter_data = get_query.getQueryData()
    proccess_string = FormatingExcel(twitter_data)
    proccess_string.format_excel()





