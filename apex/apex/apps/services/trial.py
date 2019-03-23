# importing requests package 
import requests	 

def NewsFromBBC(): 
	
	# BBC news api 
	main_url = "https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=ffb8a867858a410cb805e3cd7e6134fd"

	# fetching data in json format 
	open_bbc_page = requests.get(main_url).json() 

	# getting all articles in a string article 
	article = open_bbc_page["articles"] 

	# empty list which will 
	# contain all trending news 
	results = [] 
	
	for ar in article: 
		results.append(ar["title"]) 
		results.append(ar["description"])
		results.append(ar["url"])
		results.append(ar["publishedAt"])
		results.append(ar["content"])				
		
	for i in range(len(results)): 
		
		# printing all trending news 
		print(i + 1, results[i])				 

# Driver Code 
if __name__ == '__main__': 
	
	# function call 
	NewsFromBBC() 
