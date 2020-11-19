from bs4 import BeautifulSoup
import requests


html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'today' in published_date:
        company_name = job.find(
            'h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        print(f'company name: {company_name.strip()}')
        print(f'Required skills: {skills.strip()}\n')
        # print(company_name)
