from documanager import Document, ScienceDocument, Library

docTypes = [Document, ScienceDocument]
docs = [Document(r'documents/d1.txt'), ScienceDocument(r'documents/d2.txt'), Document(r'documents/d3.txt')]
lib = Library(docs=docs, name='My Library')


methods = {func.replace('_', ' ').capitalize(): func for func in dir(Library) if callable(getattr(Library, func)) and not func.startswith("__")}

options = ""

for i, method in enumerate(methods.keys(), start=1):
    options += f"{i}. {method}\n"

choice = input(options + "Enter a command: ")

while(True):
    try:

        print("Please choose an option:")    
        func = methods[choice]
        
    except KeyError as ke:
        break
        