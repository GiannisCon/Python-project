from graphics import *
import time
def drawEmptyRectangle(win,p1,p2,patchwork):
    selectx=int(p1/100)
    selecty=int(p2/100)
    patchwork[selectx][selecty]=0
    p3=p1+100
    p4=p2+100
    empty=Rectangle(Point(p1,p2),Point(p3,p4))
    empty.draw(win)
    empty.setFill("white")
    drawBorder(win,p1,p2,patchwork)
    return patchwork
def removeBorder(win,p1,p2,patchwork):
    selectx=int(p1/100)
    selecty=int(p2/100)
    p3=p1+100
    p4=p2+100
    patchwork[selectx][selecty]=1
    disselect=Rectangle(Point(p1,p2),Point(p3,p4))
    disselect.draw(win)
    disselect.setOutline("white")
    return patchwork


def drawBorder(win,p1,p2,patchwork):
    selectx=int(p1/100)
    selecty=int(p2/100)
    p3=p1+100
    p4=p2+100
    patchwork[selectx][selecty]=2
    border=Rectangle(Point(p1,p2),Point(p3,p4))
    border.draw(win)
    border.setOutline("black")
    return patchwork
def checkColor(color):
    colors=["red","green","blue","magenta","orange","cyan"]
    condition2=True
    while condition2:
        for i in range(6):
            if color.lower()==colors[i]:
                condition2=False
        if condition2==True:
            color=str(input("invalid colour insert again"))
    return str(color)
def drawWindow(win,size,color1,color2,color3):
    for i in range (0,size,+100):
        for j in range (0,size,+100):
            if i<100 or i>=size-100:
                if (j/100)%2==0:
                    if i==j:
                        drawPatchWindowFinal(win,color1,i,j)
                    else:
                        drawPatchWindowPenultimate(win,color1,i,j)
                else:
                    drawPatchWindowPenultimate(win,color2,i,j)
            if (j<100 and i>=100 and i<size-100) or (j>=size-100 and i>=100 and i<size-100):
                if (i/100)%2==0:
                    if i==j:
                        drawPatchWindowFinal(win,color1,i,j)
                    else:
                        drawPatchWindowPenultimate(win,color1,i,j)
                else:
                    drawPatchWindowPenultimate(win,color2,i,j)
            if i>=100 and i<size-100 and j>=100 and j<size-100:
                if i==j:
                    drawPatchWindowFinal(win,color3,i,j)
                else:
                    drawPatchWindowPenultimate(win,color3,i,j)
    challengeFeature(win,size,color1,color2,color3)
def drawPatchWindowFinal(win,color,p1,p2):
    p2=p2+100
    for i in range(1,11,+1):
        square=Rectangle(Point(p1,p1),Point(p2,p2))
        square.draw(win)
        if i%2!=0:
            square.setFill(color)
            square.setOutline(color)
        else:
            square.setFill("white")
            square.setOutline("white")
        p2-=5
        p1+=5
def  drawPatchWindowPenultimate(win,color,centerx,centery):
    radius=10
    centerx=centerx+10
    centery=centery+10
    centerxstart=centerx
    condition4=True
    for i in range (1,6,+1):
        centerx=centerxstart
        for j in range(1,7,+1):
            if j%2==1 and j>1 and  condition4 and i%2==1:
                centerx-=15
                condition4=False
            elif j%2==0 and j>1  and condition4 and i%2==0:
                centerx-=15
                condition4=False
            if condition4==False:
                centerx+=5
            if i==1 and j==5:
                centerx+=10
            if i==1 and j==6:
                centerx-=10
            if i==2 and (j==4 or j==6):
                centerx+=10
            if i==2 and j==5:
                centerx-=10
            if i==3 and j==5:
                centerx+=10
            if i==3 and j==6:
                centerx-=10
            if i==4 and (j==4 or j==6):
                centerx+=10
            if i==4 and j==5:
                centerx-=10
            if i==5 and j==5:
                centerx+=10
            if i==5 and j==6:
                centerx-=10
            circle=Circle(Point(centerx,centery),radius)
            circle.setFill(color)
            circle.setOutline(color)
            circle.draw(win)
            condition4=True
            centerx+=20
        centery+=20

def challengeFeature(win,size,color1,color2,color3):
    if size==500:
        patchwork=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    else:
        patchwork=[[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
    p1=0
    p2=0
    p3=0
    p4=0
    condition2=True
    while condition2:
        p3=p1
        p4=p2
        condition=True
        while condition:
            click=win.getMouse()
            condition=False
        for i in range (0,size,+100):
            if click.getX()>=i and click.getX()<i+100:
                column=i
            for j in range(0,size,+100):
                if click.getY()>=j and click.getY()<j+100:
                    row=j
        p1=column
        p2=row
        patchwork=drawBorder(win,p1,p2,patchwork)
        if win.getKey()=="d":
            patchwork2=drawEmptyRectangle(win,p1,p2,patchwork)
        while p1!=p3 and p2!=p4:
            if patchwork2[int(p1/100)][int(p2/100)]=="0" and win.getKey()=="1":
                drawPatchWindowPenultimate(win,color1,p1,p2)
            elif patchwork2[int(p1/100)][int(p2/100)]=='0' and win.getKey()=='2':
                drawPatchWindowPenultimate(win,color2,p1,p2)
            elif patchwork2[int(p1/100)][int(p2/100)]=='0' and win.getKey()=='3':
                drawPatchWindowPenultimate(win,color3,p1,p2)
            elif patchwork2[int(p1/100)][int(p2/100)]=='0' and win.getKey()=='4':
                drawPatchWindowFinal(win,color1,p1,p2)
            elif patchwork2[int(p1/100)][int(p2/100)]=='0' and win.getKey()=='5':
                drawPatchWindowFinal(win,color2,p1,p2)
            elif patchwork2[int(p1/100)][int(p2/100)]=='0' and win.getKey()=='6':
                drawPatchWindowFinal(win,color3,p1,p2)
            elif patchwork2[int(p1/100)][int(p2/100)]=='1' and win.getKey()=='d':
                patchwork2=drawEmptyRectangle(win,p1,p2,patchwork2)
            elif patchwork2[int(p1/100)][int(p2/100)]!=0 and win.getKey()=="Right":
                for i in range (p1,size,+100):
                    if patchwork2[int(i/100)][int(p2/100)]=='0' and p1==p2 and (p2<100 or p2>= size-100):
                        movep=i
                        drawPatchWindowFinal(win,color1,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and p1==p2:
                        movep=i
                        drawPatchWindowFinal(win,color3,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and (p1=='0' or p1==size-100) and (p2/100)%2=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color1,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and (p1=='0' or p1==size-100) and (p2/100)%2=='1':
                        movep=i
                        drawPatchWindowPenultimate(win,color2,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and (p2<100 or p2>=size-100) and (p1/100)%2=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color1,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and (p2<100 or p2>=size-100) and (p1/100)%2=='1':
                        movep=i
                        drawPatchWindowPenultimate(win,color2,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color3,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
            elif patchwork2[int(p1/100)][int(p2/100)]!='0' and win.getKey()=='Left':
                for i in range (p1-100,-1,-100):
                    if patchwork2[int(i/100)][int(p2/100)]=='0' and p1==p2 and (p2<100 or p2>= size-100):
                        movep=i
                        drawPatchWindowFinal(win,color1,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and p1==p2:
                        movep=i
                        drawPatchWindowFinal(win,color3,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and (p1=='0' or p1==size-100) and (p2/100)%2=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color1,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and (p1=='0' or p1==size-100) and (p2/100)%2=='1':
                        movep=i
                        drawPatchWindowPenultimate(win,color2,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and (p2<100 or p2>=size-100) and (p1/100)%2=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color1,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0' and (p2<100 or p2>=size-100) and (p1/100)%2=='1':
                        movep=i
                        drawPatchWindowPenultimate(win,color2,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(i/100)][int(p2/100)]=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color3,movep,p2)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
            elif patchwork2[int(p1/100)][int(p2/100)]!='0' and win.getKey()=='Up':
                for i in range (p2-100,-1,-100):
                    if patchwork2[int(p1/100)][int(i/100)]=='0' and p1==p2 and (p2<100 or p2>= size-100):
                        movep=i
                        drawPatchWindowFinal(win,color1,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and p1==p2:
                        movep=i
                        drawPatchWindowFinal(win,color3,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and (p1=='0' or p1==size-100) and (p2/100)%2=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color1,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and (p1=='0' or p1==size-100) and (p2/100)%2=='1':
                        movep=i
                        drawPatchWindowPenultimate(win,color2,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and (p2<100 or p2>=-100) and (p1/100)%2=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color1,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and (p2<100 or p2>=size-100) and (p1/100)%2=='1':
                        movep=i
                        drawPatchWindowPenultimate(win,color2,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color3,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
            elif patchwork2[int(p1/100)][int(p2/100)]!='0' and win.getKey()=='Down':
                for i in range (p2+100,size,+100):
                    if patchwork2[int(p1/100)][int(i/100)]=='0' and p1==p2 and (p2<100 or p2>= size-100):
                        movep=i
                        drawPatchWindowFinal(win,color1,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and p1==p2:
                        movep=i
                        drawPatchWindowFinal(win,color3,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and (p1=='0' or p1==size-100) and (p2/100)%2=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color1,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and (p1=='0' or p1==size-100) and (p2/100)%2=='1':
                        movep=i
                        drawPatchWindowPenultimate(win,color2,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and (p2<100 or p2>=size-100) and (p1/100)%2=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color1,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0' and (p2<100 or p2>=size-100) and (p1/100)%2=='1':
                        movep=i
                        drawPatchWindowPenultimate(win,color2,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
                    elif patchwork2[int(p1/100)][int(i/100)]=='0':
                        movep=i
                        drawPatchWindowPenultimate(win,color3,p1,movep)
                        drawEmptyRectangle(win,p1,p2,patchwork2)
        removeBorder(win,p1,p2,patchwork)
def main():
    condition1=True
    condition3=True
    while condition1:
        size=int(input("insert the patchwork size(Valid sizes are 5 or 7)"))
        if size==5 or size==7:
            condition1=False
    print("There should be at least 2 different colours. Valid colours are red,green,blue,magenta,orange and cyan")
    color=str(input("insert colour 1"))
    color1=checkColor(color)
    color=str(input("insert colour 2"))
    color2=checkColor(color)
    color=str(input("insert colour 3"))
    color3=checkColor(color)
    while condition3:
        if color1.lower()==color2.lower() and color3.lower()==color1.lower():
            color=str(input("insert another colour for colour 3"))
            color3=checkColor(color)
        condition3=False
    winx=int(size*100)
    winy=int(size*100)
    win=GraphWin("patchwork",winx,winy)
    drawWindow(win,winx,color1,color2,color3)






