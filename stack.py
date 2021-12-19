import requests
from bs4 import BeautifulSoup

def get_page(url):
  request = requests.get(url)
  soup = BeautifulSoup(request.text, "html.parser")
  maxPage = soup.find("div", {"class":"container"}).find("div", {"id":"content"
    }).find("div", {"class":"js-search-container"}).find("div", {"class":"js-search-results"
        }).find("div", {"class":"s-pagination"}).find_all("a")[-2].text.strip()
  return int(maxPage)

def stack_job(job):
    title = job.find("a", {"class": "stretched-link"})["title"].strip()
    company = job.find("h3", {"class": "fc-black-700"}).span.get_text(strip=True)
    apply = "https://stackoverflow.com" + job.find("a", {"class": "stretched-link"})["href"]
    return {"title": title, "company": company, "apply": apply}

def extract_stack(page, url):
    jobs_ls = []
    for pages in range(page):
      result = requests.get(f"{url}&pg={pages+1}")
      html = BeautifulSoup(result.text, "html.parser")
      jobs = html.find_all("div", {"class": "js-result"})
      for job in jobs:
          jobs_ls.append(stack_job(job))
    return jobs_ls

def get_jobs_stack(word):
    url = f"https://stackoverflow.com/jobs?r=true&q={word}"
    pages = get_page(url)
    jobs = extract_stack(pages, url)
    return jobs