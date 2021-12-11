from indeed import indeed_page, extract_indeed

last_page = indeed_page()
jobs_list = extract_indeed(last_page)
print(jobs_list)
