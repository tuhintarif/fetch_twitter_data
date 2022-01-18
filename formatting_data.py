import os
import pandas as pd

class FormatingExcel(object):
    def __init__(self, responses):
        self.responses = responses

    def format_excel(self):
        writer = pd.ExcelWriter('result.xlsx', engine='openpyxl') 
        wb  = writer.book
        user_name = []
        tweet = []
        country = []

        for response in self.responses:
            user_name.append(response.user.name)
            tweet.append(response.text)
            country.append(response.place.country)

        df = pd.DataFrame({
                            'UserName': user_name,
                            'Tweet': tweet,
                            'Country': country,
                            })

        df.to_excel(writer, 'Tweet')
        wb.save('result.xlsx')

        return True

    def __str__(self) -> str:
        return self.string