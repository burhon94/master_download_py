import requests


def add_queue(url):
    total_sections = 10
    response = requests.head(url)

    if response.status_code > 299:
        print('status Error')
    else:
        a = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        size = response.headers["Content-Length"]
        each_size = int(int(size) / total_sections)

        for i in range(0, len(a)):
            if i == 0:
                a[i][0] = 0
            else:
                a[i][0] = a[i - 1][1] + 1

            if i < 10 - 1:
                a[i][1] = a[i][0] + each_size
            else:
                a[i][1] = int(size) - 1
        print(a)


add_queue("http://tiktok.mix.tj/video/7/46/6034ec9eca6a4.mp4")