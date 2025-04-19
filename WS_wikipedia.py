import requests

def get_wikipedia_summary(subject_name, language='en'):

    search_url = "https://www.wikidata.org/w/api.php"
    search_params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': language,
        'search': subject_name
    }
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    if not search_data.get('search'):
        return f"No results found for '{subject_name}'."

    entity_id = search_data['search'][0]['id']


    entity_url = "https://www.wikidata.org/w/api.php"
    entity_params = {
        'action': 'wbgetentities',
        'format': 'json',
        'ids': entity_id,
        'props': 'sitelinks',
        'sitefilter': f'{language}wiki'
    }
    entity_response = requests.get(entity_url, params=entity_params)
    entity_data = entity_response.json()

    try:
        title = entity_data['entities'][entity_id]['sitelinks'][f'{language}wiki']['title']
    except KeyError:
        return f"No Wikipedia link found for '{subject_name}'."

    summary_url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{title}"
    summary_response = requests.get(summary_url)
    summary_data = summary_response.json()

    if 'extract' in summary_data:
        return summary_data['extract']
    else:
        return f"No summary available for '{subject_name}'."

# Example usage
if __name__ == "__main__":
    subject = input("Choose a subject: ")
    desc = get_wikipedia_summary(subject)
    print(desc)
