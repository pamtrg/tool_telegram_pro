



from qt_core import *
from .mainwindow import Ui_Fasttool_Telegram_UI
from ..widgets import *
from .QMenuP import Create_QMenuP

class Create_Ui:
    parent : Ui_Fasttool_Telegram_UI
    def __init__(self, themes: dict,config_TableWidge:dict,parent=None):
        self.parent = parent
        self.themes = themes
        self.config_TableWidge = config_TableWidge


    def Create_TableWidget(self,name,Layout) -> PyTableWidget:
     
        
        table_Widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["white"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
   
        table_Widget.setContextMenuPolicy(Qt.CustomContextMenu)
  
        table_Widget.customContextMenuRequested.connect(lambda pos, child=table_Widget:Create_QMenuP.connect_QMenu(self.parent,name,pos,child))


        table_Widget.set_config(self.config_TableWidge[name])
        Layout.addWidget(table_Widget)
        return table_Widget