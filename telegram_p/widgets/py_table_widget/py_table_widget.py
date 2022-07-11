# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
import re
# IMPORT STYLE
# ///////////////////////////////////////////////////////////////
from . style import *

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyTableWidget(QTableWidget):
    def __init__(
        self, 
        radius = 8,
        color = "",
        bg_color = "",
        selection_color = "",
        header_horizontal_color = "",
        header_vertical_color = "",
        bottom_line_color = "",
        grid_line_color = "",
        scroll_bar_bg_color = "",
        scroll_bar_btn_color = "",
        context_color = ""
    ):
        super().__init__()

        # PARAMETERS

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
        )

    # SET STYLESHEET
    def set_stylesheet(
        self,
        radius,
        color,
        bg_color,
        header_horizontal_color,
        header_vertical_color,
        selection_color,
        bottom_line_color,
        grid_line_color,
        scroll_bar_bg_color,
        scroll_bar_btn_color,
        context_color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,          
            _color = color,
            _bg_color = bg_color,
            _header_horizontal_color = header_horizontal_color,
            _header_vertical_color = header_vertical_color,
            _selection_color = selection_color,
            _bottom_line_color = bottom_line_color,
            _grid_line_color = grid_line_color,
            _scroll_bar_bg_color = scroll_bar_bg_color,
            _scroll_bar_btn_color = scroll_bar_btn_color,
            _context_color = context_color
        )
        # print(style_format)
        self.setStyleSheet(style_format)
      
    def set_config(self,config:dict,edit:bool=False):

        self.config = config
        self.checkboxlist = []
        


        count_true = re.findall(r'True',str(config))
        
        self.setColumnCount(len(count_true))
        self.setGridStyle(Qt.SolidLine)
        self.setFrameShape(QFrame.NoFrame)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        if edit == False:
           
            self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalHeader().setCascadingSectionResizes(False)

        # self.verticalHeader().setVisible(True)

        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setDefaultSectionSize(200)
        self.verticalHeader().setStretchLastSection(False)
        self.verticalHeader().setHighlightSections(False)
        self.horizontalHeader().setMinimumSectionSize(35)
        # self.horizontalHeader().setVisible(False)
        self.setAlternatingRowColors(False)
        self.setSortingEnabled(False)
        self.setWordWrap(False)
        self.setShowGrid(True)

        self.P_setColumnWidth()
        QShortcut(QKeySequence("Space"), self).activated.connect(self.selectCheckbox)
        
    def add_row(self):
        rowcount = self.rowCount()
        self.insertRow(rowcount)
        checkbox_item = QTableWidgetItem()
        self.checkboxlist.append(checkbox_item)
        checkbox_item.setCheckState(Qt.Unchecked)
        self.setItem(rowcount, 0, checkbox_item)


        return rowcount
    def P_setColumnWidth(self):
        # print(data)
        a = 0
        for key,value  in self.config.items():
            # print(key,value)
            if value['stt']:
                
                item = QTableWidgetItem()
                self.setHorizontalHeaderItem(a, item)
                item = self.horizontalHeaderItem(a)
                item.setText(key)
                self.setColumnWidth(a, value['size'])
                self.config[key].update({'loc':a})
                a = a+1
        return self.config


                    








    def selectCheckbox(self):
        # print(1)
        indexes = list(set(index.row() for index in self.selectedIndexes()))
        for index in indexes:
            if self.checkboxlist[index].checkState() == Qt.Unchecked:
               
                self.checkboxlist[index].setCheckState(Qt.Checked)
            
            else:
               
                self.checkboxlist[index].setCheckState(Qt.Unchecked)
       
                

    def setDatabaseOnTable(self,datas:list):
   
        count_true = re.findall(r'True',str(self.config))
        self.P_setColumnWidth()
        row_count = len(datas)
        if row_count < 1:
            self.setRowCount(0) 
        else:
        
            self.checkboxlist = []
            self.setRowCount(row_count) 
            self.setColumnCount(len(count_true))
            for i in range(len(datas)):
                for key,value in self.config.items():
                    if value['stt']:
                        if key != 'COMPLETE':
                            try:
                                vl = datas[i][key]
                            except:
                                vl =False
                            item = QTableWidgetItem(str(vl))
                            self.setItem(i, value['loc'], item)
                        else:
                            
                            Progress_Bar = QProgressBar()
                        
                            self.setCellWidget(i, value['loc'], Progress_Bar)
                checkbox_item = QTableWidgetItem()
                self.checkboxlist.append(checkbox_item)
                checkbox_item.setCheckState(Qt.Unchecked)
                self.setItem(i, 0, checkbox_item)
    def getSelected(self):
        return [check_box.row() for check_box in self.checkboxlist if check_box.checkState() == Qt.Checked]
    def get_data_from_table(self):
    
        # try:
        list_value = list()
        try:
            rows_2 =  self.getSelected()
        except:
            rows_2 =  [i for i in range(self.rowCount())]
    
        for row in rows_2:

            list_data_cl = {'row':row}
            for key,value in self.config.items():
                if value['stt']:
                    try:
                        data = self.item(row,value['loc']).text().strip()
                    except:
                        data = None
           
                list_data_cl.update({key:{'data':data,'loc':value['loc']}})

            
            # list_data_cl.update({'PATH':{'data':path}})
            list_value.append(list_data_cl)
        return list_value
    def add_value_tab(self,row_count,data):
        # print(data)
        a = 0

        for key,value in self.config.items():
            if key == 'NO.':
                text = row_count
            elif key == '':
                continue
            else:
                text = data[a]
                a = a+1
            item = QTableWidgetItem(str(text))
            self.setItem(row_count, value['loc'], item)