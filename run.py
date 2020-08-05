from common.info import InfoPart
import HTMLTestRunner
import os
import time
from common.manage_suits import ManageSuits

report = InfoPart.report_path
timefmt = time.strftime("%y-%m-%d-%H-%M-%S",time.localtime())
test_report = os.path.join(report, 'test_report_{}.html'.format(timefmt))  # 确定html报告的存储路径
suit = ManageSuits().get_suit()
with open(test_report, 'wb+') as f:
    runner = HTMLTestRunner.HTMLTestRunner(
        f, 2, title='interfacetest', description='接口测试', tester='Arlen')
    runner.run(suit)
