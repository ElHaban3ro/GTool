import os
import requests
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup



def get_user_info(user):
    font_route = os.path.abspath('./src/base/MP16OSF.ttf')

    avatar_ubi = (60, 45)
    avatar_size = (600, 600)

    username_ubi = (1015, 160)

    repos_ubi = (810, 310)
    followers_ubi = (1010, 310)
    following_ubi = (1210, 310)
    
    repo_uno = (1010, 535)
    repo_dos = (1010, 585)


    user_data = {
        'icon': '',
        'repos_count': '', 
        'followers': '', 
        'following': '', 
        'recent': []
    }


    user_page = f'https://www.github.com/{user}'
    req_user = requests.get(user_page, headers={'User-Agent': 'Mozilla/5.0'}).text
    supsup = BeautifulSoup(req_user, 'lxml')


    social_info = supsup.find_all('div', class_='js-profile-editable-area')
    
    
    for campo in social_info:
        info = campo.find_all('span', class_='text-bold')
        
        user_data['followers'] = info[0].string
        user_data['following'] = info[1].string


    
    avatar = supsup.find_all('img', class_='avatar-user')[-1]['src']
    user_data['icon'] = avatar
    
            
    repositories = supsup.find_all('a', class_='UnderlineNav-item')[1]
    print(repositories)

    repositories = repositories.find_all('span')[0]
    print(repositories)





    repositories_page = f'https://github.com/{user}?tab=repositories'
    req_repos = requests.get(repositories_page).text
    supsup_repos = BeautifulSoup(req_repos, 'lxml')

    recent_repo = supsup_repos.find_all('h3', class_='wb-break-all')

    if len(recent_repo) > 0:
        if len(recent_repo) >= 2:
            for repo in recent_repo[:2]:
                user_data['recent'].append(repo.find_all('a')[0].string.replace('\n        ', ''))

    







    try:
        os.mkdir(f'./users/{user}')
    except:
        pass
    


    # avatar_route = f'./users/{user}/avatar-{user}.png'
    # avatar_download = requests.get(user_data['icon']).content 
    # with open(avatar_route, 'wb+') as image_download:
    #     image_download.write(avatar_download)


    # image_base = Image.open('./src/base/target.png')
    # lienzo = Image.new('RGBA', image_base.size, (0, 0, 0, 0))

    # image_avatar = Image.open(avatar_route)


    # lienzo_avatar = Image.new('RGBA', image_avatar.size, 0)
    # mask_avatar = Image.new('L', image_avatar.size, 0)
    # draw = ImageDraw.Draw(mask_avatar)

    
    # circle = draw.ellipse((0, 0, image_avatar.size[0], image_avatar.size[1]), fill = 255) # Imagen redonda!!
    # image_avatar = Image.composite(image_avatar, lienzo_avatar, mask_avatar).resize(avatar_size)
    # lienzo.paste(image_avatar,  avatar_ubi)

    # f_target = Image.alpha_composite(image_base, lienzo)



    # # Text!
    # text_layer = ImageDraw.Draw(f_target)

    # font_username = ImageFont.truetype(font_route, 70)
    # font_data = ImageFont.truetype(font_route, 40)

    # text_layer.text(username_ubi, f'@{user}', font = font_username, align='center', fill=(35, 35, 35, 255), anchor='mm')



    # text_layer.text(repos_ubi, f'@{user_data["repos_count"]}', font = font_data, align='center', fill=(35, 35, 35, 255), anchor='mm')
    # text_layer.text(followers_ubi, f'@{user_data["followers"]}', font = font_data, align='center', fill=(35, 35, 35, 255), anchor='mm')
    # text_layer.text(following_ubi, f'@{user_data["following"]}', font = font_data, align='center', fill=(35, 35, 35, 255), anchor='mm')




    # text_layer.text(repo_uno, f'- {user_data["recent"][0]}', font = font_data, align='left', fill=(35, 35, 35, 255), anchor='ms')
    # text_layer.text(repo_dos, f'- {user_data["recent"][0]}', font = font_data, align='left', fill=(35, 35, 35, 255), anchor='ms')



    # f_target.save(f'./users/{user}/target.png')

    


    return user_data




result = get_user_info('twnlink')
print(result)