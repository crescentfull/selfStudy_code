facebook_posts = [
    {'Likes' : 21, 'comments' : 2},
    {'Likes' : 21, 'comments' : 2, 'shares': 1},
    {'Likes' : 21, 'comments' : 2, 'shares': 1},
    {'comments' : 2, 'shares': 1},
    {'comments' : 2, 'shares': 1},
    {'Likes' : 21, 'comments' : 2}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
        print(total_likes)
    except KeyError as e:
        print(f"{post}에 {e} 가 없습니다")
        total_likes += 0
