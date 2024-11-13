from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import argparse

arg parser = argparse.ArgumentParser(description='Herramienta para hacer ataques de fuerza bruta')
arg.add_argument("-u", dest="usuario", help="Pasar un Usuario", required=True)
arg.add_argument, dest])