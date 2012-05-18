#!/usr/bin/python
import os
import sys
import sip
from PyQt4 import QtCore,QtGui
from PyQt4.QtWebKit import *
from mainUi import Ui_MainWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Tits (QtCore.QObject):
    @QtCore.pyqtSlot(QtCore.QVariant)
    def test (self):
        print "test"

class Main(QtGui.QMainWindow):
    def __init__(self, pages, workingdir):
        QtGui.QMainWindow.__init__(self)
        self.inputpages = pages
        self.workingdir = workingdir
        self.pages = []
        self.data = []
        self.currentpage = 0
        self.getPages()
        self.finalwidth = 1448
        self.finalxoffset = 164
        self.rulers = []
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.frame = self.ui.webView.page().mainFrame()
        self.ui.webView.connect(self.ui.webView, QtCore.SIGNAL('loadFinished(bool)'), self.loadFinished)
        self.ui.webView.connect(self.ui.webView.page().mainFrame(), QtCore.SIGNAL('javaScriptWindowObjectCleared()'), self.addmodeltojs)
        self.connect(self.ui.next, QtCore.SIGNAL('clicked()'), self.nextPage)
        self.connect(self.ui.previous, QtCore.SIGNAL('clicked()'), self.previousPage)
        self.connect(self.ui.chopPage, QtCore.SIGNAL('clicked()'), self.page2jpg)
        self.connect(self.ui.addRuler, QtCore.SIGNAL('clicked()'), self.addruler)
        self.ui.webView.setUrl(QtCore.QUrl("/home/nic/git/tablemaker/magic.html"))
        self.currentpage = 0
        self.ui.webView.page().settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        self.webInspector = QWebInspector(self)
        self.webInspector.setPage(self.ui.webView.page())
        self.webInspector.setVisible(True)
        self.ui.verticalLayout_2.addWidget(self.webInspector)

    def addruler (self):
        added = False
        
        for fish in self.rulers:
            if fish[2].isHidden():
                fish[2].show()
                fish[3].show()
                fish[4].show()
                added = True
                break
            
        if not added:
            rulerno = len(self.rulers)+1
            
            newRulerbox = QtGui.QHBoxLayout()
            
            rulerLabel = QtGui.QLabel(self.ui.rulerBox)
            rulerLabel.setText("Ruler #"+str(rulerno))
            
            rulerSpin = QtGui.QSpinBox( self.ui.rulerBox)
            rulerSpin.setMaximum(10000)
            rulerSpin.setObjectName(_fromUtf8("split"+str(rulerno)+"y"))
            
            rulerInc = QtGui.QCheckBox( self.ui.rulerBox)
            rulerInc.setText("Include")
            rulerInc.setChecked(True)
            rulerInc.setObjectName(_fromUtf8("include"+str(rulerno)))
            
            newRulerbox.addWidget(rulerLabel)
            newRulerbox.addWidget(rulerSpin)
            newRulerbox.addWidget(rulerInc)
            
            self.rulers.append([rulerno, newRulerbox, rulerSpin, rulerInc, rulerLabel])
            self.connect(newRulerbox, QtCore.SIGNAL('valueChanged(int)'), self.setHandles)
            self.ui.verticalLayout_3.addLayout(newRulerbox)
            
            
        
    def clearRulers (self):
        for rulerbox in self.rulers:
            rulerbox[2].hide()
            rulerbox[3].hide()
            rulerbox[4].hide()

    def toggleInspector(self):
        self.webInspector.setVisible(not self.webInspector.isVisible())
        self.ui.next.connect(self.ui.next, QtCore.SIGNAL('clicked(bool)'), self.nextPage)
        
    def addmodeltojs (self):
        self.frame.addToJavaScriptWindowObject("pyObj", self)
    
    
    @QtCore.pyqtSlot()
    def handleMoved(self, ret=False):
        tits = self.frame.evaluateJavaScript("getRulers();")
        tits= tits.toList()
        rulers = []
        for moo in tits:
            rulers.append(int(moo.toInt()[0]))
        if ret:
            return rulers
        else:
            self.getHandles(rulers)
        
    def getHandles (self, rulers):
        moo = 0
        for tits in rulers:
            if len(self.rulers) > moo:
                if not self.rulers[moo][2].isHidden():
                    self.rulers[moo][2].show()
                    self.rulers[moo][3].show()
                    self.rulers[moo][4].show()
                self.rulers[moo][2].setValue(tits)
            else:
                pewpew = self.addruler()
                self.rulers[len(self.rulers)-1][2].setValue(tits)
            moo = moo+1
    def getpagerulers (self):
        rulersarr = []
        for ruler in self.rulers:
            if not ruler[2].isHidden():
                rulersarr.append(int(ruler[2].value()))
        return rulersarr
    
    def setHandles (self):
        rulersarr = self.getpagerulers()  
        self.frame.evaluateJavaScript("setRulers("+str(rulersarr)+");")
    
    def getPages (self):
        for chunk in self.inputpages:
            for page in range(chunk[0],(chunk[1]+1)):
                self.pages.append(os.path.join(self.workingdir, "workingpages", "page"+str(page)+".jpg"))
                self.data.append([page, [100, 200, 300]])
    
    def goToPage(self, page):
        tits =self.frame.evaluateJavaScript("setPage('"+self.pages[page]+"');")
        tits= tits.toString()
    
    def saveHandles (self):
        self.data[self.currentpage] = [self.data[self.currentpage][0],[]]
        for rulers in self.rulers:
            if not rulers[2].isHidden():
                self.data[self.currentpage][1].append(int(rulers[2].value()))
        
    def nextPage (self):
        self.saveHandles()
        self.clearRulers()
        self.currentpage = self.currentpage+1
        if self.currentpage > len(self.pages):
            self.currentpage = len(self.pages)
        self.goToPage(self.currentpage)
        self.getHandles(self.data[self.currentpage][1])
        self.setHandles()
    
    def previousPage (self):
        dosomething = 1
        self.saveHandles()
        self.currentpage = self.currentpage-1
        if self.currentpage < 0:
            self.currentpage = 0
        self.goToPage(self.currentpage)
        self.getHandles(self.data[self.currentpage][1])
        self.setHandles()
        
        
    
    def loadFinished(self, ok):
        self.goToPage(self.currentpage)
        self.handleMoved()
    
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
    
    def page2jpg(self,targetpage=None):    
        if targetpage == None:
            targetpage = self.data[self.currentpage][0]
        rulers = self.handleMoved(ret=True)
        os.system("convert '"+self.pages[self.currentpage]+"' -crop "+str(self.finalwidth)+"x"+str(rulers[1]-rulers[0])+"+"+str(self.finalxoffset)+"+"+str(rulers[0])+" '"+os.path.join(tables,"page"+str(self.data[self.currentpage][0])+"_1.jpg")+"'")
        os.system("convert '"+self.pages[self.currentpage]+"' -crop "+str(self.finalwidth)+"x"+str(rulers[2]-rulers[1])+"+"+str(self.finalxoffset)+"+"+str(rulers[1])+" '"+os.path.join(tables,"page"+str(self.data[self.currentpage][0])+"_2.jpg")+"'")
        #os.system("convert '"+self.pages[self.currentpage]+"' -crop "+str(self.finalwidth)+"x"+str(735+adjust)+"+159+"+str(906+previous)+" '"+os.path.join(tables,"page"+str(page)+"_2.jpg")+"'")
        #os.system("convert '"+self.pages[self.currentpage]+"' -crop "+str(self.finalwidth)+"x"+str(852+adjust)+"+159+"+str(1641+previous)+" '"+os.path.join(tables,"page"+str(page)+"_3.jpg")+"'")
                
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