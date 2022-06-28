class Context:
    def __init__(self):
        pass
    
    def __enter__(self):
        print("Oteviram context managera")
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Zaviram context manazera...")
        if exc_type:
            print(exc_type, exc_value, exc_traceback)
        return True
        
with Context():
    print("tohle je uprostred ... napr. kdyz zapisuji do souboru...")
    raise KeyError("tenhle klic ve slovniku neni")