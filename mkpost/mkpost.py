#!/usr/bin/python3
#
#+--------------------------------------------------------------------+
#| mkpost.py - by: Costa Kavidas (@ckavidas)                          |
#| summary:                                                           |
#|  - Transform Joplin notes to hugo posts.                           |
#|  - Compatible with hugo theme: LoveIt                              |
#| Requirements:                                                      |
#|  - Exported Markdown from joplin                                   |
#|  - header.md file in pwd                                           |
#| Usage:                                                             |
#|  - python3 mkpost.py <joplin-note.md>                              |
#|                                                                    |
#| Reference post: https://ckavidas.github.io/my-new-blog-05-2020     |
#+--------------------------------------------------------------------+
#
#Imports
import datetime
import re
import fileinput
import sys
import pathlib
import shutil

def interactiveMode():
    #Description: Function handles interactive collection of input.
    #Returns: Dictionary (options) which contains the variables and their values
    options = {}
    #Post title, description and tags
    title = input("What is the title of the post? \n")
    title = "\"" + title + "\""
    options.update({'title:': title})
    desc = input("Enter a short description of the post. \n")
    desc  = "\"" + desc + "\""
    options.update({'description:': desc})
    tags = input('Please enter tags for this post example: "comma","delimited","with","quotes" \n')
    tags = "[" + tags + "]"
    options.update({'tags:': tags})
    category = input('Please enter categories for this post example: "comma","delimited","with","quotes" \n')
    category = "[" + category + "]"
    options.update({'categories:': category})
    #Post date and modified date
    date = input("What is the date of this post (YYYY-MM-DD)? \n")
    #lazy check
    if re.fullmatch("^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$", date):
        options.update({'date:': date})
    else:
        print("Error in date, please run again.")
        quit()
    today = str(datetime.date.today())
    options.update({'lastmod:': today})
    #Author details
    author = input("Who is the author of the post? \n")
    author = "\"" + author + "\""
    options.update({'author:': author})
    link = input("What is the link to the author's site? do not include https or www. \n")
    link = "\"" + "https://" + link + "\""
    options.update({'authorLink:': link})
    print("\n The rest of the settings are left on their defaults, you can edit it manually if you like.")
    print("NOTE: You will have to insert the banner manually.\n")
    #Output file
    outfile = input("Please provide the output file name (example: my-new-post.md) ")
    options.update({'outFile': outfile})
    return(options)

def createPost(optDict, inFile, headerFile):
    #Description: Function writes lines from header.md and optDict into new post file.
    #Returns: Nothing
    #Start by copying header.md to our new post name
    newFile = optDict['outFile']
#    shutil.copy('header.md', newHeader)
    #Dump the markdown from the note into the new post file.
    with open(newFile, "w") as nf:
        with fileinput.input(files=(headerFile, inFile)) as inputs:
            for line in inputs:
                nf.write(line)
    #Iterate through replacementItems, replace lines with replacementItem with apropriate values.
    replacementItems = ["title:", "date:", "lastmod:", "author:", "authorLink:", "description:", "tags:", "categories:"]
    for item in replacementItems:
        replacementStr = item + " " + optDict[item]
        with fileinput.input(newFile, inplace=True) as f:
            for line in f:
                newLine = line.replace(item, replacementStr)
                print(newLine, end='')

def main():
    inFile = pathlib.Path(sys.argv[1])
    headerFile = pathlib.Path("header.md")
    if inFile.exists () and headerFile.exists ():
        pass
    else:
        print("Error: Either the joplin note or header.md does not exist.")
        quit()
    optDict = (interactiveMode())
    createPost(optDict, inFile, headerFile)
main()
