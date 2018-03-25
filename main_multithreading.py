import threading
from queue import Queue
from spider import Spider
from common_functions import *
from os import path

# from tqdm import tqdm
# tqdm.monitor_interval = 0

PROJECT_FOLDER = input('Enter project folder name to save all urls: ')
ROOT_URL=input('Provide web url which you want to crawl: ')
cwd = os.getcwd()
print("")
print("##############################################################################################")
print('YOUR RESULTS WILL BE STORED AT: '+ os.path.join(cwd,PROJECT_FOLDER) )
print('ROOT_URL :', ROOT_URL)
print("######################### STARTED CRAWLING "+ROOT_URL+" ######################################")
print("")

######################## PRIMARY INPUT PARAMETRES ###########################
# PROJECT_FOLDER = "recruiterbox"                                            ##
# ROOT_URL = "https://recruiterbox.com/"                                     ##
#############################################################################

DOMAIN = get_domain_from_url(ROOT_URL)
WAITING_LIST_FILE = path.join(PROJECT_FOLDER, 'waiting.txt')
WVISITED_LIST_FILE = path.join(PROJECT_FOLDER, 'visited.txt')
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_FOLDER, ROOT_URL, DOMAIN)






# creating worker threads which will die after main exits
def create_workers():
    for i in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# create work for the worker thread
def work():
    while True:
        url = queue.get()
        Spider.crawl(threading.current_thread().name, url)
        queue.task_done()

# adding url from waiting list to queue.Each link from waiting list added to queue is a new job
def create_job():
    # for url in file_to_set(WAITING_LIST_FILE):
    for url in Spider.waiting_list:
        queue.put(url)
    queue.join()
    crawl_t()


# check whether witing list file has urls and if prestnt call to create job to add to que
def crawl_t():
    # waiting_list = file_to_set(WAITING_LIST_FILE)
    # waiting_list_count = len(waiting_list)
    waiting_list_count=len(Spider.waiting_list)
    if waiting_list_count > 0:
        # print("No Of Links Waiting To be Further Crawled: " + len(str(Spider.waiting_list)))
        create_job()


create_workers()
crawl_t()
print("Done")
