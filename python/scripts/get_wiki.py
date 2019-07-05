import wikipedia

def wiki_search(search_text='soccer'):
	response_string = ""
	wikipedia.set_lang("ja")
	search_response = wikipedia.search(search_text)
	if not search_response:
		response_string = "Not Found"
		return response_string
	try:
		wiki_page = wikipedia.page(search_response[0])
	except Exception as e:
		response_string = "[Error]\n{}\n{}".format(e.message, str(e))
		return response_string
	wiki_content = wiki_page.content
	response_string += wiki_content[0:wiki_content.find(".")] + "\n"
	response_string += "Link : " + wiki_page.url
	return response_string

if __name__ == "__main__":
	wiki_search()
