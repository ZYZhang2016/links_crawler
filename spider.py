import urllib.request
from link_finder import LinkFinder
from general import *

class Spider:

    #class variables(shared among all instance)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider',Spider.base_url)

  #the first spider should do
    @staticmethod
    def boot():
        #create the project dir and file
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name,Spider.base_url)

        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name,page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            print('Queue '+ str(len(Spider.queue)) +\
                  ' | Crawled '+ str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))

            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_str = ''
        try:
            request = urllib.request.Request(page_url)
            request.add_header("User-Agent","Mozilla/5.0 (X11; Linux x86_64) \
                               AppleWebKit/537.36 (KHTML, like Gecko) \
                               Ubuntu Chromium/58.0.3029.96 Chrome/58.0.3029.96\
                               Safari/537.36")
            response = urllib.request.urlopen(request)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_str = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url,page_url)
            finder.feed(html_str)
        except:
            print('Error:can not crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            #to make sure crawler pages in this site
            if Spider.domain_name not in url:
                continue
            if url in Spider.queue or Spider.crawled:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)
