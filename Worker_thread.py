from qt_core import *
from os_core import *





class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal(int)
    error = Signal(str)
    result = Signal(object)
    progress = Signal(int)




class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        # self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
  
        # Retrieve args/kwargs here; and fire processing using them
   
        __name__ = self.fn.__name__
        print(__name__)
        try:
            result = self.fn(*self.args, **self.kwargs)
            if __name__ == 'Insert_Data':
                if result:
                    self.signals.error.emit('Import Data Success')
                else:
                    self.signals.error.emit('Import Data Fail')
            elif __name__ == 'removeAccount':
                if result:
                    self.signals.error.emit('Remove Account Success')
                else:
                    self.signals.error.emit('Remove Account Fail')
            elif __name__ == 'dichuyenacount':
                if result == 1: 
                    self.signals.error.emit('Di chuyển Account Success')
                  
                else:
                    self.signals.error.emit('Di chuyển Account Fail')
            elif __name__ == 'loc_trung':
                if result == 1: 
                    self.signals.error.emit('Lọc trùng Success')
                else:
                    self.signals.error.emit('Lọc trùng Fail')
            elif __name__ == 'gop_file_contact':
                if result == 1: 
                    self.signals.error.emit('Gộp file contact Success')
                else:
                    self.signals.error.emit('Gộp file contact Fail')
            elif __name__ == 'Checklive':
                if result == 1: 
                    self.signals.error.emit('Check live proxy Success')
                else:
                    self.signals.error.emit('Check live proxy Fail')
            elif __name__ == 'addpassword':
                if result == 1: 
                    self.signals.error.emit('Thêm mật khẩu Success')
                else:
                    self.signals.error.emit('Thêm mật khẩu Fail')

        except Exception as e:
            print(e)
            self.signals.error.emit(str(e))

