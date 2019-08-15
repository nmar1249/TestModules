from selenium import webdriver
from selenium.webdriver.support.ui import Select

from EHTest import EHTest

def error_logger(test_class):

    test = test_class

    while True:
        try:
            test.loop()
        except Exception as err:
            print('\nError  ' + str(err))
            print('On date:\t\t' + str(test.month) + '/' + str(test.day) + '/' + str(test.year))
            print('Args:\t\t\t' + str(err.args))
            print('Cause:\t\t\t' + str(err.__cause__))
            print('Class:\t\t\t' + str(err.__class__))
            print('Context:\t\t' + str(err.__context__))
            print('traceback:\t\t' + str(err.__traceback__))