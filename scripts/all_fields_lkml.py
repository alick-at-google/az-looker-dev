import requests
from github import Github
import looker_sdk
from looker_sdk import models
import lkml

#initialize SDK
sdk = looker_sdk.init31("YOUR INI FILE", section="SECTION OF YOUR INI FILE")


############SET THESE VARIABLES
user = "YOUR GITHUB USER"       # your github user
token = "YOUR ACCESS TOKEN"     # personal access token (https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)
repo = "YOUR REPO"              # name of your repo
owner = "REPO OWNER"            # owner of the git repo
file_name = "LOOKML FILE"       # ie. users.view.lkml

#authenticate via git and load lookML file
def git_auth(user, token, repo, file_name, owner):
    query_url = f"https://api.github.com/repos/{owner}/{repo}"
    params = {
        "state": "open",
    }
    headers = {'Authorization': f'token {token}'}
    r = requests.get(query_url, headers=headers, params=params)
    #grab github repo content(s)
    g = Github(token)
    repo = g.get_repo(owner + "/" + repo)
    #specify lookml file
    content = repo.get_contents(path="/Views/" + file_name)
    raw_data = content.decoded_content.decode("utf-8")
    parsed_lookml = lkml.load(raw_data)
    return parsed_lookml

# parses through lookml to return list of all dimensions/measures in a view
def parse_lookml(parsed_lookml):
    dimensions = []
    measures = []
    for view in parsed['views']:
        if "dimensions" in view:
            for dimension in view["dimensions"]:
                dimensions.append(view['name'] + "." + dimension['name'])
        if "measures" in view:
            for measure in view['measures']:
                measures.append(view['name'] + "." + measure['name'])
    #returns set of diemensions, measures, all fields
    return (["set: all_dimensions {" + str(dimensions) + "}",            
             "set: all_measures {" + str(measures) + "}",  
             "set: all_fields {" + str(dimensions + measures) + "}"])     

parse_lookml(git_auth(user, token, repo, file_name, owner))
