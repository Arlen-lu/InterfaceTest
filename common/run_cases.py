import unittest
from common.logger import logging
from common.info import InfoPart
from common.manageexcel import ManageExcel
from common.httprequest import HttpRequest
import json
from common.get_cookie import GetCookies


class RunCases(unittest.TestCase):
    '''测试开始'''

    def __init__(
            self,
            status,
            http_method,
            url,
            des,
            params,
            Expected_Result,
            sheet_name,
            case_id,
            methodname=None):
        # 保留父类的初始化参数,methodname为传入测试函数名，即test_process
        super(RunCases, self).__init__(methodname)
        self.http_method = http_method  # get/post
        self.url = url  # 接口url
        self.des = des  # description，测试说明
        self.params = params  # 参数
        self.ExpectedResult = Expected_Result  # 预期数据
        self.sheet_name = sheet_name  # 表名
        self.case_id = case_id  # caseid
        self.status = status

    # 测试前准备

    def setUp(self):
        print(
            "Test begin!\nsheet_name:{0};\ncase_id:{1};\ndescription:{2}".format(
                self.sheet_name,
                self.case_id,
                self.des))
        logging.info(
            "Test begin!sheet_name:{0};case_id:{1};description:{2}".format(
                self.sheet_name, self.case_id, self.des))
    @classmethod
    def setUpClass(cls,):
        pass
        # GetCookies().get_cookie()

    def tearDown(self):
        print("Test finished!")
        logging.info("Test finished!")

    def test_process(self):
        try:
            res = HttpRequest(
                self.status,
                self.http_method,
                self.url,
                self.params).http_request()
        except Exception as e:
            test_result = 'Error'
            logging.exception(e)
            print("{0},Error msg:{1}".format(test_result, e))
            raise e

        else:
            Actual_Result = res.json()
            # self.getlogging.get_logging("INFO","响应体：{}".format(ActualResult))
            # print(ActualResult)
        try:
            for key in self.ExpectedResult.keys():  # 遍历预期结果的key值
                # print(key)
                # 对比预期和实际结果中，对应的值是否一样
                self.assertTrue(self.ExpectedResult[key] == Actual_Result[key])
            test_result = 'Pass'
            logging.info(test_result)
        # if self.ExpectedResult["reason"] ==ActualResult['reason'] and
        # self.ExpectedResult['error_code']==ActualResult['error_code']:
        except Exception as e:
            test_result = 'Fail'
            # log写入fail的原因，是由于预期和实际结果，key相同的情况下，value值不一致导致
            logging.info(
                "{0},ExpectedResult is not equal to ActualResult, wrong msg({1}):[{2}]!=[{3}]".format(
                    test_result,
                    key,
                    self.ExpectedResult[key],
                    Actual_Result[key]))
            print(
                "Test Fail，ExpectedResult is not equal to ActualResult, wrong msg({0}):[{1}]!=[{2}]".format(
                    key,
                    self.ExpectedResult[key],
                    Actual_Result[key]))
            raise e
        finally:
            # self.getlogging.get_logging("INFO","test fail")
            # test_result = 'Fail'
            # print("Test Fail")
            # print("test_result:{}".format(test_result))
            # 重新写会excel文件，由于actualresult文件是json，则需要转化到str，ensure_ascii=False-->控制输出中文
            ManageExcel().write_back(
                self.sheet_name,
                self.case_id + 1,
                test_result,
                json.dumps(
                    Actual_Result,
                    ensure_ascii=False))

            # ManageExcel().write_back(self.sheet_name,self.row_num,test_result)


if __name__ == '__main__':
    unittest.main()
