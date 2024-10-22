from documanager import Document, ScienceDocument, Library

docTypes = [Document, ScienceDocument]
docs = [Document(r'documents/d1.txt'), ScienceDocument(r'documents/d2.txt'), Document(r'documents/d3.txt')]
lib = Library(docs=docs, name='My Library')

while(True):

    print("Please choose an option:")    

    methods = [func.replace('_', ' ').capitalize() for func in dir(Library) if callable(getattr(Library, func)) and not func.startswith("__")]

    for i, method in enumerate(methods, 1):
        print(f"{i}. {method}")

    choice = input("Enter the number of your choice: ")
        