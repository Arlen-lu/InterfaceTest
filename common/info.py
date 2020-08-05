from common.getpath import GetPath
from common.readconfig import ReadConfig
import os


def path_joint(*path):
    base_path = ReadConfig().base_path
    return os.path.join(base_path, *path)


# 数据汇总，将config中的数据，都汇总在info模块中
class InfoPart(object):
    results = ReadConfig().get_config()
    '''TestMode'''
    # 控制执行的case suit
    r_mode = results['TestMode']
    test_mode = eval(r_mode['test_mode'])
    ddt_sheet_name = r_mode['ddt_sheet_name']

    '''HttpConfig'''
    # 接口的url
    r_url = results['HttpConfig']
    url = eval(r_url['url'])

    '''DBConfig'''
    # db配置信息
    r_db = results['DBConfig']
    db_info = eval(r_db['db_info'])

    '''TestDataConfig'''
    # test_data相关文件的配置信息
    r_data = results['TestDataConfig']
    # 存储测试数据的文件名
    excel_name = r_data['excel_name']
    # 测试数据的路径
    test_data_path = path_joint(r_data['test_data_path'], excel_name)
    # 测试数据中的表名
    sheet_name = eval(r_data['sheet_name'])

    '''RunCaseConfig'''
    r_run = results['RunCaseConfig']
    # 运行指定case的配置,mode=all_run("all_run":全部跑;"part":跑部分，通过run_list确定)
    mode = r_run['mode']
    run_list = eval(r_run['run_list'])

    '''TestResultConfig'''
    r_report = results['TestResultConfig']
    # 测试结果的存储路径
    test_result_path = path_joint(r_report['test_result_path'])
    log_path = path_joint(r_report['log_path'])
    report_path = path_joint(r_report['report_path'])

    '''获取cookie'''
    r_cookie = results['GetCookies']
    home_page = r_cookie['home_page']
    user_name = r_cookie['user_name']
    passwd = r_cookie['passwd']
    cookie = r_cookie['cookie']



if __name__ == "__main__":
    all_info = InfoPart()
    # print(all_info.results)
    # print(all_info.base_path)
    print(InfoPart.test_mode)
    # print(InfoPart.ddt_sheet_name)
    # print(InfoPart.url)
    # print(InfoPart.db_info)
    print(InfoPart.test_data_path)
    # print(InfoPart.excel_name)
    # print(InfoPart.sheet_name)
    # print(type(InfoPart.sheet_name))
    # print(InfoPart.mode)
    # print(InfoPart.run_list)
    # print(InfoPart.test_result_path)
    # print(InfoPart.log_path)
    # print(InfoPart.report_path)
