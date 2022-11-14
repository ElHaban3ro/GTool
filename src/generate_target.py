import requests




def get_user_info(apikey, user, debug = True):
    req = requests.get(f'https://api.github.com/users/{user}', headers={'Accept': 'application/vnd.github+json'})

    if req.status_code == 404:
        if debug:
            return f'Error to search user. Status code: 404. Error type: {req.content.decode("utf-8")}'
        else:
            return 'Error to search user. Status code: 404.'
        


    else:
        raw_userdata = req.json()
        req_repos = requests.get(f"{raw_userdata['repos_url']}?sort=update", headers={'Accept': 'application/vnd.github+json'})
        repos = req_repos.json()

        recent_repos = []

        for repo in repos[:2]:
            recent_repos.append(repo['name'])



        user_data = {'icon': raw_userdata['avatar_url'], 'repos_count': raw_userdata['public_repos'], 'followers': raw_userdata['followers'], 'following': raw_userdata['following'], 'recent': recent_repos}
        



        return user_data





