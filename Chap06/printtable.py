def printtable(tabledata):
    outlistlen = len(tabledata)
    inlistlen = len(tabledata[0])
    for i in range(outlistlen):
        maxlen = 0
        
        for j in range(len(tabledata[i])):
           
            if len(tabledata[i][j])>maxlen:
                maxlen = len(tabledata[i][j])
                
        for k in range(len(tabledata[i])):
            tabledata[i][k] = tabledata[i][k].rjust(maxlen)
    j = 0
              
    while j<inlistlen:
        i = 0
        while i < outlistlen:
            
            print(tabledata[i][j],end='  ')
            i+=1
            
        j+=1
        print('\n')
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printtable(tableData)