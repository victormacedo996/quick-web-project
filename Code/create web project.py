class Project:

    def __init__(self, name):
        self.name = name

    def OS (self):
        from sys import platform
        if platform not in ('win32', 'cygwin'):
            return "/"
        else:
            return "\\"


    def createDirectories(self):
        import os
        separator = self.OS()
        os.mkdir(self.name)
        os.mkdir(f"{self.name}{separator}images")
        os.mkdir(f"{self.name}{separator}src")
        os.mkdir(f"{self.name}{separator}css")

    def createFiles (self):
        separator = self.OS()
        html = open(f"{self.name}{separator}index.html", "w")
        css = open(f"{self.name}{separator}css{separator}style.css", "a")
        js = open(f"{self.name}{separator}src{separator}bundle.js", "a")
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
