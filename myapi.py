import nlpcloud


class API:
    def __init__(self):
        self.client = nlpcloud.Client("finetuned-llama-3-70b", "a51c769d34fbe0e96f98d93961d91bcbb01a068f", gpu=True)
        self.client1=client = nlpcloud.Client("t5-base-en-generate-headline", "a51c769d34fbe0e96f98d93961d91bcbb01a068f", gpu=False)
        self.client2 = nlpcloud.Client("finetuned-llama-3-70b", "a51c769d34fbe0e96f98d93961d91bcbb01a068f", gpu=True)
    def sentimental_analysis(self, text):
        response=self.client.sentiment(text,target="NLP Cloud") 
        return response
    
    def generate_headline(self,text):
        response=self.client1.summarization(text)
        return response
    def name_entity_search(self,text,search):
        response=self.client2.entities(text,searched_entity=search)
        return response
