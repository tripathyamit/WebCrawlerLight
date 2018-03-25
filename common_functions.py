import os

# url finder # parse to get domain and subdomain name
from html.parser import HTMLParser
from urllib import parse


# create directory to store information for website you crawl
def create_directory_for_project(directory_path):
    if not os.path.exists(directory_path):
        print("Creating Directory:" + directory_path)
        os.makedirs(directory_path)
    else:
        print("Directory: " + directory_path + " exists!")


# create a waiting_list and visited_list files
# EX:create_files('recruterBox',"https://recruiterbox.com/")
def create_files(directory_name, url):
    waiting_list = os.path.join(directory_name, 'waiting.txt')
    visited_list = os.path.join(directory_name, 'visited.txt')
    if not os.path.isfile(waiting_list):
        write_to_file(waiting_list, url)
        print("Creating File: " + waiting_list)

    if not os.path.isfile(visited_list):
        write_to_file(visited_list, '')
        print("Creating File: " + visited_list)


# create file if not present and write to the file
def write_to_file(file_name, file_content):
    file = open(file_name, 'w')
    file.write(file_content)
    file.close()

# append contents To file already exists
def appendToFile(file_name,file_content):
    with open(file_name,'a') as file:
        file.write(file_content+'\n')

# remove file contents
def remove_file_contents(file_name):
    with open(file_name,'w') as file:
        pass

def file_to_set(file_name):
    with open(file_name, "r") as myfile:
        data = set(myfile.readlines())
    return data

def set_to_file(set,file):
    remove_file_contents(file)
    for row in set:
        appendToFile(file,row)


# finds sub doamin from url
def get_sub_domain_from_url(url):
    try:
        return parse.urlparse(url).netloc
    except:
        print("In get_sub_domain_from_url no sub domain found from: "+url)
        return ''

def get_domain_from_url(url):
    try:
        sub_domain=get_sub_domain_from_url(url)
        sub_domain_tokens=sub_domain.split(".")
        domain=sub_domain_tokens[-2]+"."+sub_domain_tokens[-1]
        return domain
    except:
        print("In get_domain_from_url no domain found from subdomain: "+url)
        return ''


class UrlFinder(HTMLParser):

    def __init__(self,home_page_url,inside_url):
        super().__init__()
        self.home_page_url=home_page_url
        self.inside_url=inside_url
        self.urls=set()
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            # print("Found an Ancor Element With Properties:"+str(attrs) )
            for attribute,value in attrs:
                if attribute=="href":
                    url=parse.urljoin(self.home_page_url,value)
                    # print("Found Link: " + value)

                    self.urls.add(url)

    def get_page_urls(self):
        return self.urls


# finder = UrlFinder()
# finder.feed('<html><head><title >Test</title></head>'
#             '<body><h1>Parse me!<a class="bordered" style="color:pink" href="https://recruiterbox.com/"></a></h1></body></html>')



