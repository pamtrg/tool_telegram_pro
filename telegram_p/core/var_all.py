


class Messages_Noti:
    NofindFileSession = 'Không tìm thấy file session !'
    ConvertSuccess = 'Convert Success !'
    ConvertFailed = 'Convert Failed !'
    NofindProxy = 'Không tìm thấy proxy !'
    ErrorLogin = 'Lỗi đăng nhập !'
    VeryLogin = 'Đăng nhập thành công !'
    JoinGrSuccess = 'Join {} Success !'
    Checklive_Success = 'Check live Success!'
    Checklive_Failed = 'Check live Failed!'


class VarAll:

    def __init__(self):
        self.__var_all = {}

    def set_var(self, key, value):
        self.__var_all[key] = value

    def get_var(self, key):
        return self.__var_all[key]

    def del_var(self, key):
        del self.__var_all[key]

    def get_all(self):
        return self.__var_all