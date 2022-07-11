import sys,json
from pyperclip import copy as copy_text
from asyncio import get_event_loop,new_event_loop,set_event_loop
import os
from bs4 import BeautifulSoup
from uuid import getnode as get_mac 
from webbrowser import open as open_web
from datetime import datetime,timedelta, date
import xlsxwriter
import requests,time,traceback