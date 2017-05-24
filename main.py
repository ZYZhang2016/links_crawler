import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'diatominus'
HOMEPAGE = 'https://westerndiatoms.colorado.edu/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 5
queue = Queue()

#the first spiser boot the project
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)


#Create workers threads(will die when main.py exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        #to make sure it will die when main.py exits
        t.daemon = True
        t.start()

#Do the the next job in the queue
def work():
    while True:
        #get next link in the working queue
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()

#Each queued links is a new job(put all the link into the working thread)
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#check if there is items in the queue,if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links))+' links in the queue')
        create_jobs()


create_workers()
crawl()
