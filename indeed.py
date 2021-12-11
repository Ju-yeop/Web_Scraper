import requests
from bs4 import BeautifulSoup

URL = "https://www.indeed.com/jobs?q=python&limit=50"
LIMIT = 50

def indeed_page():
    result = requests.get(URL)
    html = BeautifulSoup(result.text, "html.parser")
    results = html.find("div", {"class": "pagination"})
    pages = results.find_all("a")
    page_ls = []
    for page in pages[:-1]:
        page_ls.append(page.string)
    max_page = int(page_ls[-1])
    return max_page


def extract_job(job_one):
    title = job_one.find("span", title=True).string
    company = job_one.find("span", {"class": "companyName"}).string
    location = job_one.select_one("pre > div").text
    link = job_one["data-jk"]
    return {"title": title, "company": company, "location": location, "link": URL + f"&vjk={link}"}


def extract_indeed(pages):
    for page in range(pages):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        html = BeautifulSoup(result.text, "html.parser")
        jobs = html.find_all("a", {"class": "resultWithShelf"})
        jobs_ls = []
        for job in jobs:
            jobs_ls.append(extract_job(job))
        return jobs_ls
