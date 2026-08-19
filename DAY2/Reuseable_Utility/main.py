import text_util as txt # imported own created utility as txt
class Text:
    def __init__(self):
        self.text = ""
    def set_text(self,text):
        self.text=text
    def analyze_text(self):
        # Called Utility Functions 
        print("Word Count: ", txt.count_words(self.text)) 
        print("Character Count: ", txt.count_characters(self.text))
        print("Word Frequency: ", txt.count_frequency(self.text))
        
t1 = Text()
t1.set_text(input("Enter Sentence To Analyze It: "))
t1.analyze_text()