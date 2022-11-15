import os
import requests
from PIL import Image, ImageDraw



avatar_ubi = (60, 45)

def get_user_info(apikey, user, debug = True):
    req = requests.get(f'https://api.github.com/users/{user}', headers={'Accept': 'application/vnd.github+json', 'Authorization': apikey})

    if req.status_code == 404:
        if debug:
            return f'Error to search user. Status code: 404. Error type: {req.content.decode("utf-8")}'
        else:
            return 'Error to search user. Status code: 404.'
        


    else:
        raw_userdata = req.json()

        req_repos = requests.get(f"{raw_userdata['repos_url']}?sort=update", headers={'Accept': 'application/vnd.github+json', 'Authorization': apikey})
        repos = req_repos.json()

        recent_repos = []

        for repo in repos[:2]:
            recent_repos.append(repo['name'])



        user_data = {
            'icon': raw_userdata['avatar_url'],
            'repos_count': raw_userdata['public_repos'], 
            'followers': raw_userdata['followers'], 
            'following': raw_userdata['following'], 
            'recent': recent_repos
        }

        try:
            os.mkdir(f'./users/{user}')
        except:
            pass
        


        avatar_route = f'./users/{user}/avatar-{user}.png'
        avatar_download = requests.get(user_data['icon']).content 
        with open(avatar_route, 'wb+') as image_download:
            image_download.write(avatar_download)


        image_base = Image.open('./src/base/target.png')
        lienzo = Image.new('RGBA', image_base.size, (0, 0, 0, 0))

        image_avatar = Image.open(avatar_route)


        lienzo_avatar = Image.new('RGBA', image_avatar.size, 0)
        mask_avatar = Image.new('L', image_avatar.size, 0)
        draw = ImageDraw.Draw(mask_avatar)

        
        circle = draw.ellipse((0, 0, image_avatar.size[0], image_avatar.size[1]), fill = 255) # Imagen redonda!!
        image_avatar = Image.composite(image_avatar, lienzo_avatar, mask_avatar).resize((600, 600))
        lienzo.paste(image_avatar,  (60, 45))

        f_target = Image.alpha_composite(image_base, lienzo)



        f_target.save(f'./users/{user}/target.png')

        



        return user_data





with open('./config/config.txt', 'r+') as apikey:
    key = apikey.readlines()[0]

    result = get_user_info(key, 'ElHaban3ro')
    print(result)