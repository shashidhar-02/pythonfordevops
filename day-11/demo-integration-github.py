import requests
url=f'https://api.github.com/repos/kubernetes/kubernetes/pulls'
response=requests.get(url)

if response.status_code==200:
    pull_requests=response.json()
    pr_creators={}
    for pr in pull_requests:
        creator=pr["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator]+=1
        else:
            pr_creators[creator]=1
    print("pr  creators  and counts:")
    for creator,count in pr_creators.items():
        print(f"{creator}:{count}")
else:
    print(f"failed  to fetch data from github api. status code:{response.status_code}")