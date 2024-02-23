import os
import markdown

if not os.path.exists("public"):
    os.mkdir("public")

with open("intellecta/index.md", "r") as file:
    content = file.read()
    html = markdown.markdown(content)

with open("public/index.html", "w") as file:
    file.write(r'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Intellecta</title>

            <link rel="stylesheet" href="https://unpkg.com/simpledotcss/simple.min.css">

            <style>
                :root {
                    --accent: green;
                }
            </style>
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
    ''')

    file.write(html)

    file.write(r'''
            </main>

            <footer>
                <p>A project by Vinny Horgan and Francesco Catalanotti.<br>
                To make knowledge accessible to everyone.<br>
                All content licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</p>
            </footer>

        </body>
        </html>
    ''')

if not os.path.exists("public/math"):
    os.mkdir("public/math")

with open("intellecta/math/index.md", "r") as file:
    content = file.read()
    html = markdown.markdown(content, extensions=["mdx_math"])

with open("public/math/index.html", "w") as file:
    file.write(r'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Intellecta - Math</title>

            <link rel="stylesheet" href="https://unpkg.com/simpledotcss/simple.min.css">

            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.js" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/katex/dist/contrib/mathtex-script-type.min.js" defer></script>

            <style>
                :root {
                    --accent: green;
                }
            </style>
        </head>
        <body>
            <header>
                <nav>
                    <a href="/">Home</a>
                    <a href="/math" class="current">Math</a>
                    <a href="/cs">CS</a>
                </nav>

                <h1>Intellecta</h1>
                <p>Making knowledge accessible.</p>
            </header>

            <main>
    ''')

    file.write(html)

    file.write(r'''
            </main>

            <footer>
                <p>A project by Vinny Horgan and Francesco Catalanotti.<br>
                To make knowledge accessible to everyone.<br>
                All content licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</p>
            </footer>

        </body>
        </html>
    ''')

if not os.path.exists("public/math/content"):
    os.mkdir("public/math/content")

for file in os.listdir("intellecta/math/content"):
    if file.endswith(".md"):
        path = os.path.join("intellecta/math/content", file)
        html_path = os.path.join("public/math/content", os.path.splitext(file)[0] + ".html")

        with open(path, "r") as file:
            content = file.read()
            html = markdown.markdown(content, extensions=["mdx_math"])

        with open(html_path, "w") as file:
            file.write(r'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Intellecta - Math</title>

                    <link rel="stylesheet" href="https://unpkg.com/simpledotcss/simple.min.css">

                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.js" crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/katex/dist/contrib/mathtex-script-type.min.js" defer></script>

                    <style>
                        :root {
                            --accent: green;
                        }
                        main p {
                            text-align: justify;
                        }
                    </style>
                </head>
                <body>
                    <header>
                        <nav>
                            <a href="/">Home</a>
                            <a href="/math" class="current">Math</a>
                            <a href="/cs">CS</a>
                        </nav>

                        <h1>Intellecta</h1>
                        <p>Making knowledge accessible.</p>
                    </header>

                    <main>
            ''')

            file.write(html)

            file.write(r'''
                    </main>

                    <footer>
                        <p>A project by Vinny Horgan and Francesco Catalanotti.<br>
                        To make knowledge accessible to everyone.<br>
                        All content licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</p>
                    </footer>

                </body>
                </html>
            ''')

if not os.path.exists("public/cs"):
    os.mkdir("public/cs")

with open("intellecta/cs/index.md", "r") as file:
    content = file.read()
    html = markdown.markdown(content)

with open("public/cs/index.html", "w") as file:
    file.write(r'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Intellecta - CS</title>

            <link rel="stylesheet" href="https://unpkg.com/simpledotcss/simple.min.css">

            <style>
                :root {
                    --accent: green;
                }
            </style>
        </head>
        <body>
            <header>
                <nav>
                    <a href="/">Home</a>
                    <a href="/math">Math</a>
                    <a href="/cs" class="current">CS</a>
                </nav>

                <h1>Intellecta</h1>
                <p>Making knowledge accessible.</p>
            </header>

            <main>
    ''')

    file.write(html)

    file.write(r'''
            </main>

            <footer>
                <p>A project by Vinny Horgan and Francesco Catalanotti.<br>
                To make knowledge accessible to everyone.<br>
                All content licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</p>
            </footer>

        </body>
        </html>
    ''')

if not os.path.exists("public/cs/content"):
    os.mkdir("public/cs/content")

for file in os.listdir("intellecta/cs/content"):
    if file.endswith(".md"):
        path = os.path.join("intellecta/cs/content", file)
        html_path = os.path.join("public/cs/content", os.path.splitext(file)[0] + ".html")

        with open(path, "r") as file:
            content = file.read()
            html = markdown.markdown(content)

        with open(html_path, "w") as file:
            file.write(r'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Intellecta - CS</title>

                    <link rel="stylesheet" href="https://unpkg.com/simpledotcss/simple.min.css">

                    <style>
                        :root {
                            --accent: green;
                        }
                    </style>
                </head>
                <body>
                    <header>
                        <nav>
                            <a href="/">Home</a>
                            <a href="/math">Math</a>
                            <a href="/cs" class="current">CS</a>
                        </nav>

                        <h1>Intellecta</h1>
                        <p>Making knowledge accessible.</p>
                    </header>

                    <main>
            ''')

            file.write(html)

            file.write(r'''
                    </main>

                    <footer>
                        <p>A project by Vinny Horgan and Francesco Catalanotti.<br>
                        To make knowledge accessible to everyone.<br>
                        All content licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</p>
                    </footer>

                </body>
                </html>
            ''')
