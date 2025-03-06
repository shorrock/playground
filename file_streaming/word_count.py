def do_parse_file(filename):
    file = open(filename, 'r')
    file_contents = file.read()
    words = file_contents.split()
    wordcount = len(words)
    #for word in words:
    #    print(word, len(word))
    print(wordcount)

if __name__ == '__main__':
    filename = str(input())
    do_parse_file(filename)