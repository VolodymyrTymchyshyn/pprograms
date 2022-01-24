class Ebook():
    def __init__(self,title,author,page_numbers, current_page):
        self.title = title
        self.author=author
        self.page_numbers=page_numbers
        self.current_page=current_page
        self.status=False
    def printer(self):
        print(self.title,self.author,self.page_numbers, self.current_page)
    def openn(self):
        self.status=True
        print("NOw open")
    def close(self):
        self.status=False
        

    def set_current(self,new_page):
        self.current_page=new_page
   
        
c=Ebook("Til","jogn",345, 12)
c.printer()
c.openn()
c.set_current(134)