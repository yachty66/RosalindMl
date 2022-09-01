myname= "jon"

print(myname)

#creation of dataset
alphabet = ["A", "C", "G", "T"]
X = []
y = []
Y=[]
x = []
for i in range(1000):
    for j in range(23):
        rand = random.sample([0, 1, 2, 3], 1)
        x.append(alphabet[rand[0]])

    X.append(x)
    x = []
    

for i in range(len(X)):
    for j in range(23):
        if X[i][j] == "T":
            y.append(X[i][j].replace("T", "U"))

        else:
            y.append(X[i][j])
    Y.append(y)
    y=[]
        
#string of numbers
#need to convert to vector
#google "convert string of numbers to vector of numbers"
#set all replacement numbers to string
#iter over X and y and apply convertion
#training should work now

for i in range(len(X)):
    for j in range(23):
        assert len(X[i]) == 23
        #print(len(X[i])) 
        #expected i wanna know the value of X[i] how to do that with the debugger
        X[i] = X[i][j].replace("A", "1")
        X[i] = X[i][j].replace("C", "2")
        X[i] = X[i][j].replace("G", "3")
        X[i] = X[i][j].replace("T", "4")
        
        '''y[i] = y[i].replace("A", 1)
        y[i] = y[i].replace("C", 2)
        y[i] = y[i].replace("G", 3)
        y[i] = y[i].replace("U", 5)'''
    
xTrain = np.array(X[:800]).reshape(800, 1)
xTest = np.array(X[800:]).reshape(200, 1)
yTrain = np.array(y[:800]).reshape(800, 1)
yTest = np.array(y[800:]).reshape(200, 1)

#reg = LinearRegression().fit(xTrain, yTrain)
#need to represent into numerical vectors
#A=1 C=2 ... take X and y and replace A=1, C=2, G=3, T=4, U=5
#need to reshape into [[], []..] format
