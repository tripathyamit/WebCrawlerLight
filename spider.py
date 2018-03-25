from urllib.request import  urlopen
from common_functions import *
import os

class Spider:
    # creating class variables so that can be accessed and updated across all instances of the class
    project_folder=""
    root_url=""
    domain=""
    waiting_list_file=""
    visited_list_file=""
    waiting_list=set()
    visited_list=set()

    def __init__(self,project_folder,root_url,domain):
        Spider.project_folder=project_folder;
        Spider.root_url=root_url
        Spider.domain=domain
        Spider.waiting_list_file=os.path.join(project_folder,'waiting.txt')
        Spider.visited_list_file = os.path.join(project_folder, 'visited.txt')
        self.boot()
        self.crawl("First Spider is Actice.",Spider.root_url)

    @staticmethod
    def boot():
        create_directory_for_project(Spider.project_folder)
        create_files(Spider.project_folder,Spider.root_url)
        Spider.waiting_list=file_to_set(Spider.waiting_list_file)
        Spider.visited_list = file_to_set(Spider.visited_list_file)

    @staticmethod
    def crawl(thread_name,page_url):
        if page_url not in Spider.visited_list:
            print(thread_name+" is crwaling: "+page_url)
            print("Waiting:"+str(len(Spider.waiting_list))+" #### "+"Visited:"+ str(len(Spider.visited_list)) )
            print("")
            Spider.add_links_to_wating_list(Spider.get_page_links(page_url))
            # removing link from waiting list and adding to visited list
            Spider.waiting_list.discard(page_url)
            Spider.visited_list.add(page_url)
            Spider.update_files()



    @staticmethod
    def get_page_links(page_url):
        try:
            response=urlopen(page_url)
            # print('response header',response.getheader('Content-Type'))
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes=response.read()
                html_string=html_bytes.decode("utf-8")
                # print("html_string",html_string)

            finder = UrlFinder(Spider.root_url,page_url)
            finder.feed(html_string)
        except:
            # print("Umable to get_page_links from: "+page_url)
            # traceback.print_exc(file=sys.stdout)
            return set()
        return finder.get_page_urls()

    @staticmethod
    def add_links_to_wating_list(urls):
        for temp in urls:
            if temp in Spider.waiting_list:
                continue
            if temp in Spider.visited_list:
                continue
            if temp =="":
                continue

            if Spider.domain not in temp:
                continue
            Spider.waiting_list.add(temp)

    @staticmethod
    def update_files():
        try:
            set_to_file(Spider.waiting_list,Spider.waiting_list_file)
            set_to_file(Spider.visited_list,Spider.visited_list_file)
        except:
            print("In update_files")









        

