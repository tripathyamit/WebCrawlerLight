from queue import Queue
from spider import Spider
from common_functions import *
from os import path

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



# crawl item from waiting list file
def crawl_t():
    waiting_list_count=len(Spider.waiting_list)
    while len(Spider.waiting_list) > 0:
        # print("No Of Links Waiting To be Further Crawled: " + str(len(Spider.waiting_list)))
        url=Spider.waiting_list.pop()
        Spider.crawl("Spider",url)


crawl_t()
print("Done")
