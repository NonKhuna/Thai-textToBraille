class stack :
    verb=''
    top=[]
    alphaIn=[]
    alphaFi=[]
    haveFrontVerb=0
    isalphaFi=0

    def reset(self) :
        self.verb = ''
        self.top = []
        self.alphaIn = []
        self.alphaFi = []
        self.haveFrontVerb=0
        self.isalphaFi=0
    def show(self) :
        print(self.verb)
        print(self.top)
        print(self.alphaIn)
        print(self.alphaFi)

    def count(self) :
        return len(self.verb)+len(self.top)+len(self.alphaIn)+len(self.alphaFi)+len(self.karan)
