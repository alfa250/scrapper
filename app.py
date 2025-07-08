from bs4 import  BeautifulSoup
import requests

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)
#print(page.text)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'ResultsContainer')
# for job in job_cards:
#     title = job.find('h2', class_ = 'title')
#     company = job.find('h3', class_ = 'company')
#     location = job.find('p', class_= 'location')
#     print(title.text.strip())
#     print(company.text.strip())
#     print(location.text.strip())
#     print()



# for job in python_jobs:
#     title = job.find('h2', class_ =  'title')
#     location = job.find('p', class_ = 'location')
#     company = job.find('h3', class_ = 'company')
#     print(title.text.strip())
#     print(location.text.strip())
#     print(company.text.strip())

# for job_card in python_job_cards:
#     location = job_card.find('p', class_ = 'location')
#     print(title.text.strip())
#     print(company.text.strip())
#     print()
#     print(location.texts.strip())

# for job_card in python_job_cards:
#     links = job_card.find_all('a')
#     for link in links:
#         url = link['href']
#         print(f'apply here {url} \n')
    
def scrapper(results):
    job_cards = results.find_all('div', class_ = 'card-content')
    python_jobs = results.find_all('h2', string = \
             lambda x: 'python' in x.lower())
    python_job_cards = [h2_element.parent.parent.parent for h2_element in python_jobs]
    for job_card in python_job_cards:
        title = job_card.find('h2', class_ = 'title')
        company = job_card.find('h3', class_ = 'company')
        link = job_card.find_all('a')[1]['href']
        print(title.text.strip())
        print(company.text.strip())
        print(f'apply here {link} \n')
scrapper(results)

    
    

    




    



 


    














