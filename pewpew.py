#!/usr/bin/python
import os
import sys
from PyQt4 import QtCore,QtGui
from mainUi import Ui_MainWindow

class Main(QtGui.QMainWindow):
    def __init__(self, pages, workingdir):
        QtGui.QMainWindow.__init__(self)
        self.inputpages = pages
        self.workingdir = workingdir
        self.pages = []
        self.data = []
        self.currentpage = 0
        self.getPages()
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.webView.setUrl(QtCore.QUrl("/home/nic/workspace/tablessplitter/magic.html"))
        self.ui.webView.connect(self.ui.webView, QtCore.SIGNAL('loadFinished(bool)'), self.loadFinished)
        
        self.ui.next.connect(self.ui.next, QtCore.SIGNAL('clicked(bool)'), self.nextPage)
        self.frame = self.ui.webView.page().mainFrame()
        
        
    def getPages (self):
        for chunk in self.inputpages:
            for page in range(chunk[0],(chunk[1]+1)):
                self.pages.append(os.path.join(self.workingdir, "workingpages", "page"+str(page)+".jpg"))
                self.data.append([page, "25%", "50%", "75%",])
    
    def goToPage(self, page):
        print self.pages[page]
        tits =self.frame.evaluateJavaScript("setPage('"+self.pages[page]+"');")
        tits= tits.toString()
        print str(tits)   
            
    
    def nextPage (self):
        dosomthien = 1
        
    
    def loadFinished(self, ok):
        self.goToPage(0)
    
    def pdf2pages(self):
        for chunk in pages:
            for page in range(chunk[0],(chunk[1]+1)):
                os.system("convert -density 400 '"+os.path.join(targetfolder,pdf)+"'["+str(page)+"] -resize 2000x\\> -crop 1763x2696+119+118 '"+os.path.join(workingpages,"page"+str(page)+".jpg")+"'")
                #break
            #break
    
    def pages2splits(self,targetpage=None):    
        for chunk in pages:
            for page in range(chunk[0],(chunk[1]+1)):
                if targetpage == None or page == targetpage:
                    adjust = 0
                    previous = 0
                    os.system("convert '"+os.path.join(workingpages,"page"+str(page)+".jpg")+"' -crop "+str(self.finalwidth)+"x"+str(786+adjust)+"+"+str(self.finalxoffset)+"+"+str(120+previous)+" '"+os.path.join(tables,"page"+str(page)+"_1.jpg")+"'")
                    os.system("convert '"+os.path.join(workingpages,"page"+str(page)+".jpg")+"' -crop "+str(self.finalwidth)+"x"+str(735+adjust)+"+159+"+str(906+previous)+" '"+os.path.join(tables,"page"+str(page)+"_2.jpg")+"'")
                    os.system("convert '"+os.path.join(workingpages,"page"+str(page)+".jpg")+"' -crop "+str(self.finalwidth)+"x"+str(852+adjust)+"+159+"+str(1641+previous)+" '"+os.path.join(tables,"page"+str(page)+"_3.jpg")+"'")
                #break
            #break

pages = [(84,115),(141,190)]
pdf = "Guardian PostGrad Guide2.pdf"
targetfolder = "/home/nic/Desktop/Ebooks/Random_House/1294"
workingpages ="/home/nic/Desktop/Ebooks/Random_House/1294/workingpages"
tables="/home/nic/Desktop/Ebooks/Random_House/1294/tables"
testpage = 87


    
#pdf2pages()
def main():
    app = QtGui.QApplication(sys.argv)
    window=Main(pages, targetfolder)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()