import json
from .webscraper import Website
from .llm import chat_with_llama, link_system_prompt

system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website 
and creates a short humorous, entertaining, jokey brochure about the company for prospective customers, investors and recruits.
Respond in markdown. For every mention of a company, partner, social media, or resource, include the actual clickable markdown link using the real URL if available.
Include details of company culture, customers and careers/jobs if you have the information.
"""

def get_links_user_prompt(website):
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. "
    user_prompt += "Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt

def get_links(url):
    website = Website(url)
    prompt = get_links_user_prompt(website)
    response = chat_with_llama(link_system_prompt, prompt)
    try:
        data = json.loads(response)
        if isinstance(data, dict) and "links" in data:
            return data
        else:
            return {"links": []}
    except Exception as e:
        print("Error parsing LLM response:", e)
        return {"links": []}

def get_all_details(url):
    result = "Landing page:\n"
    result += Website(url).get_contents()
    links = get_links(url)
    for link in links["links"]:
        if isinstance(link, dict) and "type" in link and "url" in link:
            result += f"\n\n{link['type']}\n"
            result += Website(link["url"]).get_contents()
    return result

def get_brochure_user_prompt(company_name, url):
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    user_prompt += "When mentioning any partner, social media, or resource, always use the actual markdown link with the real URL provided below.\n"
    user_prompt += get_all_details(url)
    user_prompt = user_prompt[:5000]  # Truncate if too long
    return user_prompt

def create_brochure(company_name, url):
    user_prompt = get_brochure_user_prompt(company_name, url)
    result = chat_with_llama(system_prompt, user_prompt)
    return result