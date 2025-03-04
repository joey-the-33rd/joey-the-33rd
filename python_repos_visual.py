# Processing an API Response.
# Working wiht the response dictionary.

import requests
import plotly.express as px
import pandas as pd

# Make an API call and check the response status code.
url = 'https://api.github.com/search/repositories'
url+= '?q=language:python&sort=stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Peocess the repository infomation.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo_names into active links.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"'<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    
    stars.append(repo_dict['stargazers_count'])

    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# make visualization.
title='Most_Starred Python Projects on Github'
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, 
        hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
        yaxis_title_font_size=20)  

# Customiziing Marker colors.
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

# Show the plot.
fig.show()