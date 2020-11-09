from PyQt5.QtWidgets import QMenu, QAction

def MenuCreate(menuBar=None, menuName="", action=None):
    if menuBar != None: 
        menu = menuBar.addMenu(menuName)   
    else:  
        menu = QMenu(menuName)
    if action != None: 
        menu.addAction(action)
    return menu

def MenuActionCreate(window=None, actionName="", actionTip="", action=None):
    menuAct = QAction(actionName, window)
    menuAct.setStatusTip(actionTip)
    menuAct.setWhatsThis(actionTip)
    menuAct.triggered.connect(action)
    return menuAct