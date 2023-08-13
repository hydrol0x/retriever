from googlesearch import search
import requests
from bs4 import BeautifulSoup
from palm import handle_chat
import asyncio

def google_search(query, num_results=10):
    search_results = []
    for result in search(query, num_results=num_results):
        search_results.append(result)
    return search_results

def get_result_contents(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0",
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        paragraphs = soup.find_all('p')
        
        paragraph_contents = [p.get_text() for p in paragraphs]
        
        return paragraph_contents
    else:
        return None

async def summarize_content(content, question):
    prompt=f"""Please summarize the following content into 1 concise paragraph. The paragraph shouldn't exceed 5 sentences. The summary should also try to answer the users question.

Question:
{question}

Content:
{content}
    """

    resp = await handle_chat(prompt)
    return resp
    
def run_web_search(query):
    results = google_search(query)

    if results:
        contents = get_result_contents(results[2])
        if contents:
            summary = asyncio.run(summarize_content(contents, query))
            return summary['response']
    else:
        return None


if __name__ == "__main__":
    # query = input("Enter your search query: ")
    # results = google_search(query)

    # if results:
    #     print("Search Results:")
    #     for idx, result in enumerate(results, start=1):
    #         print(f"{idx}. {result}")
    #     contents = get_result_contents(results[0])
    #     if contents:
    #         summary = asyncio.run(summarize_content(contents))
    #         print(summary)
    # else:
    #     print("No results found.")
    print(run_web_search("When was NSDA nationals 2023?"))
