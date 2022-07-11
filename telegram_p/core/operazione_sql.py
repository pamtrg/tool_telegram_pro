
from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy import create_engine,inspect
from sqlalchemy import update,delete,select
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.ext.declarative import declarative_base
import os,datetime

import typing

list_block = ['ADD MemBer']


class SQL_Database_P():
    def __init__(self):
        self.engine = create_engine('sqlite:///Database/Account/Database.sqlite', connect_args={"check_same_thread": False})
        self.db_session = scoped_session(sessionmaker(bind=self.engine)) 
        self.meta = MetaData()
        self.insp = inspect(self.engine)
        self.conn = self.engine.connect()
        self.list_Table_names = self.Get_list_Table()
        # self.list_Table_names.append('Home')
    def connect_insp(self):
        self.meta = MetaData()
        self.insp = inspect(self.engine)
        self.conn = self.engine.connect()
    def Get_list_Table(self)-> list:
        # self.connect_insp()
        return self.insp.get_table_names()
    def Create_Table(self,__tablename__):
        # self.connect_insp()
        try:
            if not self.insp.has_table(__tablename__):
                
                Table(
                    __tablename__, self.meta , 
                    Column('SESSION', String,primary_key = True), 
                    Column('ID', String,index=True), 
                    Column('USERNAME', String,index=True),
                    Column('PASSWORD', String,index=True),
                    Column('PHONE', String,index=True),
                    Column('FULLNAME', String,index=True),
                    Column('AVATAR', String,index=True),
                    Column('LIVE', String,index=True),
                    Column('PROXY', String,index=True),
                    Column('PATH', String,index=True),
                    Column('TIME', String,index=True),
                    Column('ACCEPTED TIME', String,index=True),
                    Column('STATUS', String,index=True),
                    Column('MESSENGER', String,index=True)
                )

                self.meta.create_all(self.engine)
                self.list_Table_names.append(__tablename__)
                return 1
            return 0
        except:
            return 2
    # from main import MainWindow
    def remove_table(self,__tablename__):
   
        try:
            table = self.meta.tables.get(__tablename__)
            if table is not None:
                base = declarative_base()
                # base.metadata.drop_all(table)


                base.metadata.drop_all(self.engine, [table], checkfirst=True)
                self.list_Table_names.remove(__tablename__)
                return 1
        except:
            return 0    





        
    def Insert_Data(self,__tablename__,list_path,__password__,__only__= None):
        try:
            
            path_check = []
            list_data = []
            list_account_check = []
            table = Table(__tablename__, self.meta , autoload=True, autoload_with=self.engine)
            # if isinstance(__only__,dict):
            #     list_data.append({
            #         'SESSION':__only__['SESSION'],
            #         'PATH':r'Database\Account\AddNew',
            #         'TIME':datetime.datetime.now(),
            #         'PASSWORD':__only__['PASSWORD']
            #         })
            # else:
                # m = 0
            for i in range(len(list_path)):
                path = list_path[i]
                for ii in [x[2] for x in os.walk(path)][0]:
                    if path not in path_check:
                        path_check.append(path)
                        for ii in [x[2] for x in os.walk(path)][0]:
                            if 'session' == str(ii.split('.')[-1]):
                                if ii not in list_account_check:
                                    list_account_check.append(ii)
                                    TIME = datetime.datetime.now()
                                    list_data.append(
                                        {'SESSION':ii,'PATH':path,'TIME':TIME,'PASSWORD':__password__}
                                    )
                                    # m = m+1
            len_ = len(list_data)
            if len_ < 1:
                return 2
            else:
                self.engine.execute(table.insert(), list_data)
                return 1
        except Exception as e:
            print(e)
            return 0
    def Add_row(self,__tablename__,list_data):
        try:
            table = Table(__tablename__, self.meta , autoload=True, autoload_with=self.engine)

            self.engine.execute(table.insert(),list_data)
            return 1
        except:
            return 0
    def Update_Data(self,__tablename__,SESSION,data):

        TIME = datetime.datetime.now()
        data.update({'TIME':TIME})
       


        try:
            table = Table(__tablename__, self.meta , autoload=True, autoload_with=self.engine)
            # for i in data:
         
            rs = update(table).where(table.c.SESSION == SESSION ).values(data)
            self.engine.execute(rs)
            return 1
        except Exception as e:
            
            print(e)
            return 0
    def Delete_Rows(self,__tablename__,SESSION):
        try:
            table = Table(__tablename__, self.meta , autoload=True, autoload_with=self.engine)
            rs = delete(table).where(table.c.SESSION == SESSION)
            self.engine.execute(rs)
            return 1
        except Exception as e:
            print(e)
            return 0
    def Get_counts(self,__tablename__):
        # table = Table(__tablename__, self.meta , autoload=True, autoload_with=self.engine)
        # # print(func.count())
    
        count = self.engine.execute('SELECT count(*) AS count_1 FROM {0}'.format(__tablename__)).scalar()
        return count
    def Get_data(self,__tablename__):
        # self.connect_insp()
        if self.insp.has_table(__tablename__):
            table = Table(__tablename__, self.meta , autoload=True, autoload_with=self.engine)
            query = select([table]) 
            a = self.conn.execute(query).mappings().all()
            # data = dict(zip([c[0] for c in cur.description], res[0]))
            return a
        return []
 
        

