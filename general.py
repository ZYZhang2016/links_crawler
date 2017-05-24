import os

#Each website you crawl is a seprate project
#thie will create a directory for each project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating progect '+directory)
        os.makedirs(directory)

#create_project_dir('thenewboston')

#create queue(url need to be crawle) and crawler files(if not created)
def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#Create a new file
def write_file(path,data):
    with open(path,'w') as f:
        f.write(data)

#create_data_files('thenewboston','https://thenewboston.com/')

#add data onto an existing_file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')

#Delete the contents of a file
def delete_file_contents(path):
    open(path,'w').close()

#Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#Iterate a through a set,each item will be a new line in the file
def set_to_file(links,file):
    with open(file,'w') as f:
        for link in sorted(links):
            f.write(link+'\n')
