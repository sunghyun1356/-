


def solution(genres, plays):
    
    nd_genres = list(set(genres))
    # 1,2
    listing = {}
    genres_list = {}
    answer = []
    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in listing:
            listing[genre] = []
            genres_list[genre] = 0
        listing[genre].append((int(play), index))
        genres_list[genre] += int(play)  # 오타 수정

    # genres_list를 내림차순으로 정렬하여 장르 순서 정하기
    nd_genres = sorted(nd_genres, key=lambda x: genres_list[x], reverse=True)

    for i in nd_genres:
        listing[i] = sorted(listing[i], key=lambda x: (x[0], -x[1]), reverse=True)

    for key in nd_genres:
        if len(listing[key]) > 0:
            answer.append(listing[key][0][1])
        if len(listing[key]) > 1:
            answer.append(listing[key][1][1])
    
    return answer


generes = list(input().split())
plays = list(input().split())
print(solution(generes, plays))