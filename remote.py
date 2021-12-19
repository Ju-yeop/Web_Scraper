import requests
from bs4 import BeautifulSoup


def remote_job(job):
    if job.find("td", {"class": "company_and_position"}).find("span", {"class": "closed"}) == None:
        title = job.find("td", {"class": "company_and_position"}).find("a").find("h2").text
        company = job.find("td", {"class": "company_and_position"}).find("span").find("h3").text
        apply = "https://remoteok.io" + job["data-url"]
        return {"title": title, "company": company, "apply": apply}

def extract_remote(url):
    result = requests.get(url)
    html = BeautifulSoup(result.text, "html.parser")
    jobs = html.find("div", {"class": "page"}).find("div", {"class": "container"}).find("table").find("tbody")\
        .find_all("tr", {"class", "job"})
    jobs_ls = []
    for job in jobs:
        jobs_ls.append(remote_job(job))
    return jobs_ls


def get_jobs_remote(word):
    url = f"https://remoteok.io/remote-dev+{word}-jobs"
    jobs = extract_remote(url)
    return jobs