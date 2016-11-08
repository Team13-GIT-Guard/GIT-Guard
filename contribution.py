import urllib2
import webbrowser
import os



def take_repo():
    address = raw_input("\t\tType in repo address: ")
    return address

def main():
    repo_address = take_repo()

    url = "https://api.github.com/repos/"
    seperated_address = repo_address.split('/')
    url += (seperated_address[3]+'/'+seperated_address[4])
    url += "/stats/contributors"
    
    response = urllib2.urlopen(url)
    content = response.read()
    content = content.decode("utf-8")
    format_content = content.strip('[]').split(',')

    file = open("contribution.csv","w")
    file.write("contributor,insert,delete,commit\n")

    total_insert = 0
    total_delete = 0
    
    for line in format_content:
        if "\"total\"" in line:
            commit = int(line.split(':')[1])
        elif "\"a\"" in line:
            total_insert += int(line.split(':')[1])
        elif "\"d\"" in line:
            total_delete += int(line.split(':')[1])
        if "login" in line:
            contributor = line.split(':')[2]
            file.write(contributor + ',' + str(total_insert) + ',' + str(total_delete) + ',' + str(commit) + '\n')
            total_insert = 0
            total_delete = 0

    file.close()

    path = os.path.abspath('contribution_by_commit.html')
    url = 'file://' + path
    webbrowser.open(url)
    path = os.path.abspath('contribution_by_insert.html')
    url = 'file://' + path
    webbrowser.open(url)
    path = os.path.abspath('contribution_by_delete.html')
    url = 'file://' + path
    webbrowser.open(url)
