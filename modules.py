import os
import markdown
import shutil

def buildHeader(title="Intellecta"):
    style = ""
    if title == "Intellecta - Math":
        style = "<link rel='stylesheet' href='/assets/css/math.css'>"

    header = rf'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>

            <link rel="stylesheet" href="https://unpkg.com/simpledotcss/simple.min.css">

            <!--<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css" crossorigin="anonymous">-->
            <script src="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.js" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/katex/dist/contrib/mathtex-script-type.min.js" defer></script>

            <link rel="stylesheet" href="/assets/css/style.css">
            {style}

        </head>
        <body>
            <header>
                <nav>
                    <a href="/" class="current">Home</a>
                    <a href="/math">Math</a>
                    <a href="/cs">CS</a>
                </nav>

                <h1>Intellecta</h1>
                <p>Making knowledge accessible.</p>
            </header>

            <main>
    '''
    return header

def buildFooter():
    footer = rf'''
    </main>

        <footer>
            <p>A project by Vinny Horgan and Francesco Catalanotti.<br>
            To make knowledge accessible to everyone.<br>
            All content licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</p>
        </footer>

        </body>
    </html>'''
    
    return footer

def copyFolder(source_folder, destination_folder):
    # Remove the destination folder and its contents if it already exists
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)

    # Copy the entire contents of the source folder to the destination folder
    shutil.copytree(source_folder, destination_folder)

    return

def mdToHtml(path, extensions=[], extension_configs={}):
    with open(path, "r") as file:
        html = markdown.markdown(file.read(), extensions=extensions, extension_configs=extension_configs)
        return html

def ifNotExistsCreate(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return
