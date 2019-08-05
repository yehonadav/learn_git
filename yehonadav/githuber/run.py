import re
import sys
import json
import argparse
import threading
from requests import get
from requests.auth import HTTPBasicAuth

parser = argparse.ArgumentParser()
parser.add_argument('target', help='target')
parser.add_argument('-o', help='output file', dest='output')
parser.add_argument('-u', help='your username', dest='uname')
parser.add_argument('-t', help='number of threads', dest='threads', type=int)
parser.add_argument('--org', help='organization', dest='org', action='store_true')
parser.add_argument('--breach', help='check emails for breach', dest='breach', action='store_true')
args = parser.parse_args()

inp = args.target
breach = args.target
output = args.output
organization = args.org
uname = args.uname or ''
thread_count = args.threads or 2

colors = True  # Output should be colored
machine = sys.platform  # Detecting the os of current system
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False  # Colors shouldn't be displayed in mac & windows
if not colors:
    end = green = bad = info = ''
    start = ' ['
    stop = ']'
else:
    end = '\033[1;m'
    green = '\033[1;32m'
    bad = '\033[1;31m[-]\033[1;m'
    info = '\033[1;33m[!]\033[1;m'
    start = ' \033[1;31m[\033[0m'
    stop = '\033[1;31m]\033[0m'

print('''%s
    GitHuber
%s''' % (green, end))

if inp.endswith('/'):
    inp = inp[:-1]

targetOrganization = targetRepo = targetUser = False

jsonOutput = {}

if inp.count('/') < 4:
    if '/' in inp:
        username = inp.split('/')[-1]
    else:
        username = inp
    if organization:
        targetOrganization = True
    else:
        targetUser = True

elif inp.count('/') == 4:
    targetRepo = inp.split('/')
    username = targetRepo[-2]
    repo = targetRepo[-1]
    targetRepo = True
else:
    print('%s Invalid input' % bad)
    quit()


def find_contributors_from_repo(username, repo):
    response = get('https://api.github.com/repos/%s/%s/contributors?per_page=100' % (username, repo), auth=HTTPBasicAuth(uname, '')).text
    contributors = re.findall(r'https://github\.com/(.*?)"', response)
    return contributors


def find_repos_from_username(username):
    response = get('https://api.github.com/users/%s/repos?per_page=100&sort=pushed' % username, auth=HTTPBasicAuth(uname, '')).text
    repos = re.findall(r'"full_name":"%s/(.*?)",.*?"fork":(.*?),' % username, response)
    nonForkedRepos = []
    for repo in repos:
        if repo[1] == 'false':
            nonForkedRepos.append(repo[0])
    return nonForkedRepos


def find_email_from_contributor(username, repo, contributor):
    response = get('https://github.com/%s/%s/commits?author=%s' % (username, repo, contributor), auth=HTTPBasicAuth(uname, '')).text
    latestCommit = re.search(r'href="/%s/%s/commit/(.*?)"' % (username, repo), response)
    if latestCommit:
        latestCommit = latestCommit.group(1)
    else:
        latestCommit = 'dummy'
    commitDetails = get('https://github.com/%s/%s/commit/%s.patch' % (username, repo, latestCommit), auth=HTTPBasicAuth(uname, '')).text
    email = re.search(r'<(.*)>', commitDetails)
    if email:
        email = email.group(1)
        if breach:
            jsonOutput[contributor] = {}
            jsonOutput[contributor]['email'] = email
            if get('https://haveibeenpwned.com/api/v2/breachedaccount/' + email).status_code == 200:
                email = email + start + 'pwned' + stop
                jsonOutput[contributor]['pwned'] = True
            else:
                jsonOutput[contributor]['pwned'] = False
        else:
            jsonOutput[contributor] = email
    return email


def find_email_from_username(username):
    repos = find_repos_from_username(username)
    for repo in repos:
        email = find_email_from_contributor(username, repo, username)
        if email:
            print (username + ' : ' + email)
            break


def find_emails_from_repo(username, repo):
    contributors = find_contributors_from_repo(username, repo)
    print('%s Total contributors: %s%i%s' % (info, green, len(contributors), end))
    for contributor in contributors:
        email = (find_email_from_contributor(username, repo, contributor))
        if email:
            print(contributor + ' : ' + email)


def find_users_from_organization(username):
    response = get('https://api.github.com/orgs/%s/members?per_page=100' % username, auth=HTTPBasicAuth(uname, '')).text
    members = re.findall(r'"login":"(.*?)"', response)
    return members


def threader(function, arg):
    threads = []
    for i in arg:
        task = threading.Thread(target=function, args=(i,))
        threads.append(task)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    del threads[:]


def flash(function, arg):
    for begin in range(0, len(arg), thread_count):
        end = begin + thread_count
        splitted = arg[begin:end]
        threader(function, splitted)


if targetOrganization:
    usernames = find_users_from_organization(username)
    flash(find_email_from_username, usernames)
elif targetUser:
    find_email_from_username(username)
elif targetRepo:
    find_emails_from_repo(username, repo)
if output:
    json_string = json.dumps(jsonOutput, indent=4)
    savefile = open(output, 'w+')
    savefile.write(json_string)
    savefile.close()
