"""
File: webcrawler.py
Name: Johnny Chan
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': "t-stripe"})  # Find all table tags with class 't-stripe'

        for tag in tags:  # Loop through each table tag
            lst = tag.tbody.text.split("\n")  # Get the text of the tbody tag

            total_male = total_female = 0
            for i in range(2, len(lst)-4, 2):    # Loop through list
                number_male = lst[i].split(" ")[1]
                number_female = lst[i].split(" ")[3]

                number_male = int("".join(number_male.split(",")))    # change str number to int number
                number_female = int("".join(number_female.split(",")))
                total_male += number_male    # adding male number to the totals
                total_female += number_female    # adding female number to the totals
            print(f"Male number: {total_male}")
            print(f"Female number: {total_female}")


if __name__ == '__main__':
    main()
