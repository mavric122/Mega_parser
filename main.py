from parser.megamarket.parser_megamarket import parser_megamarket
from GUI.gui import main_menu
from logging import getLogger, basicConfig, DEBUG

""""Блок логирования"""
logger = getLogger()
FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
basicConfig(level=DEBUG, format=FORMAT)
"""Конец блока логирования"""


#parser_megamarket("4060")

main_menu()