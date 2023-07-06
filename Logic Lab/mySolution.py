
class MySolution:
    def __init__(self):
        self.alpha=[]
        self.KB=[]
        self.newClauses=[]
        self.numOfClauseInKB=0
        self.result=True
        self.smd=[]

    def getInput(self,filename):
        file = open(filename, 'r')
        Lines = file.readlines()
        self.alpha =Lines[0].strip().replace(" ","").split('OR')
        self.numOfClauseInKB=int(Lines[1].strip())

        for i in range(2,len(Lines)):
            self.KB.append(Lines[i].strip().replace(" ","").split('OR'))
        file.close()

    def PLResolve(self,c1,c2):
        pos1,pos2,isFound=0,0,0
        for i1 in range(0,len(c1)):
            for i2 in range(0,len(c2)):
                if(len(c1[i1])>len(c2[i2]) and c1[i1][1]==c2[i2][0]):
                    pos1=i1
                    pos2=i2
                    isFound=isFound+1
                    break
                elif(len(c1[i1])<len(c2[i2]) and c1[i1][0]==c2[i2][1]):
                    pos1=i1
                    pos2=i2
                    isFound=isFound+1
                    break
            if(isFound==2):
                return
        # neu menh de moi co them cap literals trai dau => mde True =>loai
        # khi isFound==2 tuc co toi 2 cap trung
        if(isFound==1):
            newClause = c1[:pos1]+c1[pos1+1:]+c2[:pos2]+c2[pos2+1:]
            return self.checkFormat(newClause)

    def checkFormat(self,clause):
        clause=list(dict.fromkeys(clause))
        length = len(clause)
        for i in range(0,length-1):
            for j in range(i+1,length):
                first=clause[i]
                second=clause[j]
                if first[0]=='-':
                    first=first[1]
                if second[0]=='-':
                    second=second[1]
                if second<first:
                    temp=clause[i]
                    clause[i]=clause[j]
                    clause[j]=temp
        return clause
            
    def changeToNegative(self,clause):
        for i in range(0,len(clause)):
            if(len(clause[i])==1):
                clause[i]="-"+clause[i]
            else:
                clause[i]=clause[i][1]
        return clause


    def PLSolution(self):
        KB_temp=self.KB.copy()
        alphaNev = self.changeToNegative(self.alpha)
        for c in alphaNev:
            if(c not in KB_temp):
                KB_temp.append([c])
        lenTemp=len(KB_temp)
        while True:
            for i in range(0, lenTemp):
                for j in range(i+1, lenTemp):
                    newClause = self.PLResolve(KB_temp[i],KB_temp[j])
                    if(newClause!= None and newClause not in KB_temp):
                        KB_temp.append(newClause)
                        self.newClauses.append(newClause)
            self.smd.append(len(KB_temp)-lenTemp)
            if(0 in self.smd or self.newClauses in self.KB):
                self.result = False
                return 
            if([] in self.newClauses):
                self.result=True
                return True
            lenTemp=len(KB_temp)
    def covertToClause(self,arr):
        if len(arr)==0:
            return "{}"
        c=arr[0]
        for i in range(1,len(arr)):
            c+=" OR "+arr[i]
        return c
    def writeOutput(self,filename):
        file = open(filename, 'w')
        temp=0
        for i in self.smd:
            file.write(str(i) + '\n')
            for j in range(temp,i+temp):
                file.write(self.covertToClause(self.newClauses[j])+'\n')
            temp+=i
        if(self.result):
            file.write("YES")
        else: 
            file.write("NO")
        file.close()



