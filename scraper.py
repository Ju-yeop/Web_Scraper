from stack import get_jobs_stack
from wework import get_jobs_wework

def get_jobs(word):
    return get_jobs_stack(word) + get_jobs_wework(word)
