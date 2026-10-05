

import requests 

url = "https://api.github.com/search/repositories"

response = requests.get(
    url,
    headers={"Accept": "application/vnd.github+json"},
    params={
        "q": "org:google",
        "sort": "stars",
        "order": "desc",
        "per_page": 3
    }
)

data = response.json()

for repo in data["items"]:
    print(repo["name"])
    print(repo["description"])
    print(repo["stargazers_count"])
    print(repo["language"])

remaining = response.headers.get("X-RateLimit-Remaining")
print(f"X-RateLimit-Remaining: {remaining}")

