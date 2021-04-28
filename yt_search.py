from urllib.request import Request, urlopen
def main(text):
    text = text.split("$search: ")[1]
    youtube = "https://www.youtube.com/results?search_query="
    text = text.replace(" ", "+")
    request = youtube+text
    req = Request(request, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    data = str(webpage)
    data = data.split('{"videoRenderer":{"videoId":"')[1]
    data = data.split('","thumbnail":{"thumbnails"')[0]
    link = "https://www.youtube.com/watch?v="+data
    return link
if __name__ == "__main__":
    main(text)
