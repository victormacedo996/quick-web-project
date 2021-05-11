class Project:

    def __init__(self, name):
        self.name = name

    def createDirectories(self):
        import os
        os.mkdir(self.name)
        os.mkdir(f"{self.name}/images")
        os.mkdir(f"{self.name}/src")
        os.mkdir(f"{self.name}/css")

    def createFiles (self):
        html = open(f"{self.name}/index.html", "w")
        css = open(f"{self.name}/css/style.css", "a")
        js = open(f"{self.name}/src/bundle.js", "a")
        html.write("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="css/style.css" rel="stylesheet"/>
        <title>Document</title>
    </head>
    <body>
        
    </body>
</html>
    """)

project_name = str(input("Enter the name of your project: "))
project = Project(project_name)
project.createDirectories()
project.createFiles()
