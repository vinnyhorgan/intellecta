import os
from modules import *


## Copy the assets folder to the public folder
source_folders = ["intellecta/assets"]
destination_folders = ["public/assets"]

for source_folder, destination_folder in zip(source_folders, destination_folders):
    copyFolder(source_folder, destination_folder)


### Home index ###
with open("public/index.html", "w") as file:
    file.write(buildHeader() + mdToHtml("intellecta/index.md") + buildFooter())
    

### Math index ###
ifNotExistsCreate("public/math")

with open("public/math/index.html", "w") as file:
    file.write(buildHeader("Intellecta - Math") + mdToHtml("intellecta/math/index.md", ["mdx_math"]) + buildFooter())


### Math content ###
ifNotExistsCreate("public/math/content")

for file in os.listdir("intellecta/math/content"):
    if file.endswith(".md"):
        path = os.path.join("intellecta/math/content", file)
        html_path = os.path.join("public/math/content", os.path.splitext(file)[0] + ".html")

        with open(html_path, "w") as file:
            file.write(
                buildHeader("Intellecta - Math") + 
                mdToHtml(path, extensions=["mdx_math"], 
                         extension_configs={"mdx_math": {"enable_dollar_delimiter": True}}) +
                buildFooter())


### CS index ###
ifNotExistsCreate("public/cs")

with open("public/cs/index.html", "w") as file:
    file.write(buildHeader(title="Intellecta - CS") + mdToHtml("intellecta/cs/index.md") + buildFooter())


### CS content ###
ifNotExistsCreate("public/cs/content")

for file in os.listdir("intellecta/cs/content"):
    if file.endswith(".md"):
        path = os.path.join("intellecta/cs/content", file)
        html_path = os.path.join("public/cs/content", os.path.splitext(file)[0] + ".html")

        with open(html_path, "w") as file:
            file.write(buildHeader(title="Intellecta - CS") + mdToHtml(path) + buildFooter())
