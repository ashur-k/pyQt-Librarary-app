from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
#import MySQLdb

from PyQt5.uic import loadUiType

ui, _ = loadUiType('library.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()

    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.main_tab_widget.tabBar().setVisible(False)

    def Handel_Buttons(self):
        self.theme_btn.clicked.connect(self.Show_Themes)
        self.theme_hide_btn.clicked.connect(self.Hiding_Themes)

        self.day_to_day_btn.clicked.connect(self.Open_Day_to_Day_Tab)
        self.books_tab_btn.clicked.connect(self.Open_Books_Tab)
        self.users_tab_btn.clicked.connect(self.Open_Users_Tab)
        self.settings_tab_btn.clicked.connect(self.Open_Settings_Tab)

        self.book_save_btn.clicked.connect(self.Add_New_Book)


    def Show_Themes(self):
        self.theme_menu.show()

    def Hiding_Themes(self):
        self.theme_menu.hide()

    ################################
    ''' Opening Tabs Functionality'''
    #################################

    def Open_Day_to_Day_Tab(self):
        self.main_tab_widget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.main_tab_widget.setCurrentIndex(1)

    def Open_Users_Tab(self):
        self.main_tab_widget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.main_tab_widget.setCurrentIndex(3)

    ################################
    ''' Books Tabs Functionality'''
    #################################

    def Add_New_Book(self):
        print("Function is running")
        print(sys.version)
        print(sys.executable)

    def Search_Books(self):
        pass

    def Edit_Book(self):
        pass

    def Delete_Book(self):
        pass

    ################################
    ''' Users Tabs Functionality'''
    #################################

    def Add_New_User(self):
        pass

    def Login(self):
        pass

    def Edit_User(self):
        pass

    ################################
    ''' Users Tabs Settings'''
    #################################

    def Add_Category(self):
        pass

    def Add_Author(self):
        pass

    def Add_Publisher(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
