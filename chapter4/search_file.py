#Listing 4-48,49

#coroutine_next not working!
#@coroutine_next
def search_file(filename):
    print('Searching file %s' % (filename))
    my_file = open(filename, 'r')
    file_content = my_file.read()
    my_file.close()
    while True:
        search_text = (yield)
        search_result = file_content.count(search_text)
        print('Number of matches: %d' % (search_result))

search = search_file("example4_3.txt")
search.next()
print(search.send("python"))
print(search.send("Jython"))
print(search.send("the"))
print(search.send("This"))
