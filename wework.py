import requests
from bs4 import BeautifulSoup

def wework_job(job):
    title = job.find("span", {"class": "title"}).get_text(strip=True)
    company = job.find("span", {"class": "company"}).get_text(strip=True)
    apply = "https://weworkremotely.com" + job.find("a")["href"]
    return {"title": title, "company": company, "apply": apply}


def extract_wework(url):
    result = requests.get(url)
    html = BeautifulSoup(result.text, "html.parser")
    jobs = html.find_all("li", {"class": "feature"})
    jobs_ls = []
    for job in jobs:
        jobs_ls.append(wework_job(job))
    return jobs_ls

def get_jobs_wework(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = extract_wework(url)
    return jobs