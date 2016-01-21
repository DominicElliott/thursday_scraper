# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
myvar = 'he said "welcome!".'
myage = 35
mylist  = ['Tuesday','Wednesday','Thursday']
mynumlist = [1,15,25,35]
print myvar
print myage
print mylist
listlength = len(mylist)
stringlength = len(myvar)
numlength = len(myage)
print listlength
print stringlength
print numlength
print mylist[2] 
print mynumlist[3:4]

# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
