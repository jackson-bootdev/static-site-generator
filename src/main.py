from textnode import *
from htmlnode import *
from generate import *

def main():
    clear_directory('./public')
    copy_directory('./static', './public')

main()
