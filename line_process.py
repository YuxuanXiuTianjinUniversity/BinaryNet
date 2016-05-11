import sys
import os
LR=[]
TraingLoss=[]
ValLoss=[]
ValErrorRate=[]
TestLoss=[]
TestErrorRate=[]
BestEpoch=[]
BestValErrorRate=[]
EpochTime=[]
file=open('data.txt')
while 1:
    newline= file.readline()
    if not newline:
        break
    newline=newline.strip()
    if not newline:
        break
    if cmp(newline[0:5],'Epoch')==0:
 #       line = line[6:].strip()
 #       ThisEpochNumber=line[0]
 #       line[13:]

        linesplited=newline.split()

        ThisEpochNumber=linesplited[1]
        ThisEpochTime = linesplited[-1]
        ThisEpochTime=ThisEpochTime.strip()
        ThisEpochTime=ThisEpochTime.replace('s','')
        EpochTime.append(ThisEpochTime)
        #count=1
        #while count <= 8 :
        #    count=count+1
        #    newline = file.readline()

    if cmp(newline[0],'L')==0:
                SplitedLine=newline.split(':')
                ThisEpochLR=SplitedLine[-1].strip()
                LR.append(ThisEpochLR)
                #newline=newline[33:]
                #newline=newline.strip()
    if cmp(newline[0],'t')==0:
                SplitedLine = newline.split(':')
                LineFlag=SplitedLine[0].strip()
                if cmp(LineFlag,'training loss')==0:
                    ThisEpochTraningLoss=SplitedLine[1].strip()
                    TraingLoss.append(ThisEpochTraningLoss)
                elif cmp(LineFlag,'test loss')==0:
                    ThisEpochTestLoss=SplitedLine[1].strip()
                    TestLoss.append(ThisEpochTestLoss)
                elif cmp(LineFlag,'test error rate')==0:
                    ThisEpochTestErrorRate=SplitedLine[1].strip()
                    TestErrorRate.append(ThisEpochTestErrorRate)
    if cmp(newline[0],'v')==0:
                SplitedLine = newline.split(':')
                LineFlag = SplitedLine[0].strip()
                if cmp(LineFlag, 'validation loss')==0:
                    ThisEpochValidationLoss = SplitedLine[1].strip()
                    ValLoss.append(ThisEpochValidationLoss)
                elif cmp(LineFlag, 'validation error rate')==0:
                    ThisEpochValidationErrorRate = SplitedLine[1].strip()
                    ValErrorRate.append(ThisEpochValidationErrorRate)
    if cmp(newline[0],'b')==0:
                SplitedLine = newline.split(':')
                LineFlag = SplitedLine[0].strip()
                if cmp(LineFlag, 'best epoch')==0:
                    ThisEpochbestepoch = SplitedLine[1].strip()
                    BestEpoch.append(ThisEpochbestepoch)
                elif cmp(LineFlag, 'best validation error rate')==0:
                    ThisEpochbestvalidationerrorrate = SplitedLine[1].strip()
                    BestValErrorRate.append(ThisEpochbestvalidationerrorrate)

file.close()
file=open('LR.txt','w')
for l in LR:
    file.write(l+ '\n')
file.close()
file=open('TraingLoss.txt','w')
for l in TraingLoss:
    file.write(l + '\n')
file.close()
file=open('TestErrorRate.txt','w')
for l in TestErrorRate:
    file.write(l + '\n')
file.close()
file=open('TestLoss.txt','w')
for l in TestLoss:
    file.write(l + '\n')
file.close()
file=open('ValErrorRate.txt','w')
for l in ValErrorRate:
    file.write(l + '\n')
file.close()
file=open('ValLoss.txt','w')
for l in ValLoss:
    file.write(l + '\n')
file.close()
file=open('BestValErrorRate.txt','w')
for l in BestValErrorRate:
    file.write(l + '\n')
file.close()
file=open('BestEpoch.txt','w')
for l in BestEpoch:
    file.write(l + '\n')
file.close()
file=open('EpochTime.txt','w')
for l in EpochTime:
    file.write(l + '\n')
file.close()
