from common.dotest_ddt import TestCaseddt
from common.run_cases import RunCases
from common.manageexcel import ManageExcel
from common.info import InfoPart
import HTMLTestRunner
import unittest
import os
import sys
import time


class ManageSuits(object):

    def __init__(self):
        self.urls = InfoPart.url
        self.test_data = ManageExcel().data_treat()
        self.test_mode = InfoPart.test_mode # 0则正常跑，1则使用ddt，临时数据跑
        self.report = InfoPart.report_path
        self.suit = unittest.TestSuite()
        self.loader = unittest.TestLoader()

    def get_suit(self):
        if self.test_mode == 0:
            for key in self.test_data.keys():
                for i in range(0, len(self.test_data[key])):
                    data = self.test_data[key][i]
                    http_method = data['httpmethod']
                    url = self.urls[data['group']]
                    des = data['description']
                    params = eval(data['params'])
                    ExpectedResult = eval(data['ExpectedResult'].replace('null', 'None'))
                    case_id = data['id']
                    status = data['login_status']
                    self.suit.addTest(
                        RunCases(
                            status,
                            http_method,
                            url,
                            des,
                            params,
                            ExpectedResult,
                            key,
                            case_id,
                            methodname='test_process'))
        else:
            self.suit.addTest(self.loader.loadTestsFromTestCase(TestCaseddt))  # 通过类名导入case
        return self.suit