# Python program to find github repositories contributors emails
## Install
```
cd yeahonadav
cd githuber
python -m venv venv
venv\\Scripts\\activate || . venv/bin/activate
pip install -r requirements.txt
```

## Example usage
```
#### Find email addressess of contributors of a repository
`python run.py https://github.com/username/repository`


#### Find email addresses of members of an organization
`python run.py organization --org`

or

`python run.py https://github.com/orgs/organzation`

#### Save JSON output to a file
`python run.py https://github.com/username/repository -o /path/to/file`

#### Rate limiting
Github allows 60 unauthenticated requests per hour but limit for authenticated requests is 6000 per hour.
You don't need to generate any kind of authenticated token, just supply your username via `-u` option as follows:

`python run.py username -u yourUsername`

#### Threading
run supports multi-threading for faster data retrieval.

`python run.py IBM --org -t 20`

#### Check if email has appeared in a breach
run uses haveibeenpwned.com API to check if an email has been breached or not. This feature is turned off by default and can be used with `--breach` option as follows

`python run.py s0md3v --breach`
```
