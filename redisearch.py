from redisearch import Client, TextField, IndexDefinition, Query

#Index 'idx:movie' already exists, i.e. no need to create a new index
client = Client(
    'idx:movie',
    host = 'localhost',
    password = ''
    )

#result=client.search("war") -> This line would search for every document with the word 'war' in it

#Below query for more advanced search -> find all documents in the 'idx:movie' index with the word 'war' in the title, and only return me the title

result=client.search(Query("war").return_fields('title').limit_fields("title")) #Query for more advanced search

#Code below this for formatting output

string=(str(result))
new=string.replace('Document', '\n')
print(new)
