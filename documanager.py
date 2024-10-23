import os

class Document():

    command = "notepad.exe"

    def __init__(self, path_to_file:str):

        self.path_to_file = path_to_file
        self.title = None
        self.date  = None
        self.link  = None
        self.body  = None

        with open(path_to_file, 'r') as f:
            # read in data
            self.data = f.read()

    def set_properties(self):
        data = self.data.split('-----')
        # assign properties

        date, link = data[1].strip().split('\n') # strip the execess whitespaces and the split the text into date and link

        self.title = data[0].strip('\n') # removes excess whitespaces
        self.date = date 
        self.link = link
        self.body = data[-1].strip('\n') # removes excess whitespaces

    def __repr__(self): # __repr__ is the default method for representing an object (if __str__ is not defined)
        pass # fill me in (return the title and date of the document)

    def contains_substr_in_body(self, substr:str):
        pass # fill me in (return True if the body contains the string, False otherwise)

    def edit_document(self):
        command_with_arg = ... # TODO: Challenge 1
        os.system(command_with_arg)

class ScienceDocument(Document):
    def __init__(self, path_to_file:str):
        super().__init__(path_to_file) # call the parent class constructor
        self.author = None
        self.references = None

    def set_properties(self):
        pass # TODO Challenge (set the title, date, author, link, body, and references properties)

    def __repr__(self):
        pass # fill me in (return the title, author, and date of the document)


class Library(): 
    def __init__(self, docs:list[Document], name:str):
        self.name = name
        self.documents = docs # TODO: Challenge 4 NOTE: we are assuming that the titles are unique

    def __repr__(self) -> str:
        return f'{self.name} has {len(self)} documents.'

    def __len__(self) -> int:
        return len(self.documents)

    def add_documents(self, docs) -> None:
        if isinstance(docs, Document):
            ... # TODO: Challenge 3
        elif isinstance(docs, list[Document]):
            ... # TODO: Challenge 3
        else:
            raise ValueError('The input must be a Document or a list of Documents') # TODO:Challenge 3 (BONUS)

    def get_all_documents(self) -> list[Document]:
        return self.documents # TODO: Challenge 4

    def get_document_by_title(self, title:str) -> Document:
        pass # TODO: Challenge 4

    # TODO: Challenge 4 (BONUS) 
    

class GradeBook():
    def __init__(self, path_to_file:str):
        pass 


