import unittest
from ddt import ddt,data,unpack
from common.httprequest import HttpRequest
from common.info import InfoPart
from common.manageexcel import ManageExcel
import json

ddt_sheet_name = InfoPart().ddt_sheet_name
testdata = ManageExcel().read_data(ddt_sheet_name)
@ddt
class TestCaseddt(unittest.TestCase):

    def setUp(self):
        print("Test begin!")

    def tearDown(self):
        print("Test End!")
    
    @data(*testdata)
    def test_ddt_process(self,testdata):
        id = testdata['id']
        url = testdata['url']
        httpmethod = testdata['httpmethod']
        description = testdata['description']
        params = testdata['params']
        expectedresult = eval(testdata['ExpectedResult'].replace('null','None'))
        # actualresult = testdata['ActualResult']
        test_result = testdata['TestResult']
        status = testdata['login_status']
        try:
            res = HttpRequest(status,httpmethod,url,params).http_request()
        except Exception as e:
            test_result = 'Error'
            print("{0},error msg:{1}".format(test_result,e))
            raise e
        else:
            actualresult = res.json()
        try:
            for key in expectedresult.keys():
                self.assertEqual(expectedresult[key],actualresult[key])
            test_result = 'Pass'
            print("result:{0};\nsheet_name:{1};\ncase_id:{2};\ndescription:{3}".format(test_result,ddt_sheet_name,id,description))
        except Exception as e:
            test_result = 'Fail'
            print("{0},msg:{1}".format(test_result,e))
            raise e
        finally:
            ManageExcel().write_back(ddt_sheet_name,id+1,test_result,json.dumps(actualresult,ensure_ascii=False))

if __name__=='__main__':
    unittest.main()