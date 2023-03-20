import requests
import json
from bs4 import BeautifulSoup


def lambda_handler(event, context):
    url = event['url']
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    data_list = []
    for job_title, exp_text in zip(soup.select('.job-title-text a'), soup.select('.exp-text-d')):
        data = {'Job Title': job_title.text.strip(), 'Experience': exp_text.text.strip()}
        data_list.append(data)

    return {
        'statusCode': 200,
        'body': data_list
    }


if __name__ == "__main__":
    event = {
      "url": "https://jobs.bdjobs.com/jobsearch.asp?fcatId=8&icatId="
    }
    x = lambda_handler(event, [])
    print(x)
