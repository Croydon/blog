#!/usr/bin/env python

import os
import re

# Remove index.html from URLs 
# which wget is adding for URls whcih ended on a slash 

for subdir, dirs, files in os.walk("./"):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(subdir, filename)
            print(filepath)
            content = ""
            with open(filepath) as file:
                for line in file:
                    # Special case handling
                    # On the home page the home page link contains just index.html
                    line = line.replace("href=\"index.html\"", "href=\"/\"")
                    line = line.replace(
                        "content=\"http://localhost/", 
                        "content=\"https://blog.cr0ydon.com/"
                        )
                    if filename.endswith("feed.html"):
                        line = line.replace(
                            "http://localhost",
                            "https://blog.cr0ydon.com"
                        )
                    line = line.replace(
                        "/feed.html\"",
                        "/feed.xml\""
                    )
                    line = line.replace(
                        "content=\"/assets/",
                        "content=\"https://blog.cr0ydon.com/assets/"
                    )

                    content += re.sub("href=\"(?!http)(.*)/index\.html\"",
                                    "href=\"\\1/\"", 
                                    line
                                    )
             
            with open(filepath, "w") as file:
                file.write(content)


# Make feed being parserd as actual xml
os.rename("feed.html", "feed.xml")
