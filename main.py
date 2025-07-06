import requests

def get_random_wiki():

    url="https://en.wikipedia.org/api/rest_v1/page/random/summary"

    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()

        title=data.get("title","n/a")
        extract=data.get("extract","no summary available")
        page_url=data.get("content_urls",{}).get("desktop",{}).get("page","url not available")

        print(f"Title:{title}\n")
        print(f"summar:{extract}\n")
        print(f"Read more:{page_url}")
    except requests.RequestException as e:
        print("failed to fetch data",e)

get_random_wiki()