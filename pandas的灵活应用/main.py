import requests
import re

import pandas as pd
import time
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

headers = {
    "Host": "search.51job.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
}
session = requests.session()
session.headers = headers



def get_html():
    sum_job_name = []
    sum_job_href1 = []
    sum_company_name = []
    sum_company_href1 = []
    sum_providesalary_text1 = []
    sum_workarea_text1 = []
    sum_issuedate = []
    sum_updatedate = []
    sum_companytype_text1 = []
    sum_job_name = []
    sum_job_name = []
    sum_job_name = []
    def tihuan(list):
        list_sum = []
        for i in list:
            i = str(i)
            i = i.replace("\\","")
            list_sum.append(i)
        return list_sum

    def tihuan3(list):
        list_sum = []
        for i in list:
            i = str(i)
            i = i.replace("/","")
            list_sum.append(i)
        return list_sum

    def tihuan2(list):
        list_yaoqiu = []
        list_xueli = []
        list_renshu = []

        for i in list:
            try:
                i = str(i)
                i = i.split(',')
                list_yaoqiu.append(i[1].replace('"',''))
                list_xueli.append(i[2].replace('"',''))
                list_renshu.append(i[-1].replace('"','').replace("'",""))
            except:
                list_yaoqiu.append('')
                list_xueli.append('')
                list_renshu.append('')
        return list_yaoqiu,list_xueli,list_renshu

    time_tag = time.strftime("%Y%m%d%H%M%S", time.localtime())
    riqi = str(time_tag)[:8]
    miao = str(time_tag)[8:]
    for i in tqdm(range(1,162,1)):
        url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python%2520%25E4%25B8%258A%25E6%25B5%25B7,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=".format(i)
        html = session.get(url)
        content =html.text

        # ??????????????????
        job_names = re.compile('"job_name":"(.*?)",', re.S | re.I)
        job_name = job_names.findall(content)

        # ??????????????????
        job_hrefs = re.compile('"job_href":"(.*?)",', re.S | re.I)
        job_href = job_hrefs.findall(content)
        job_href1 = tihuan(job_href)

        # ??????????????????
        company_names = re.compile('"company_name":"(.*?)",', re.S | re.I)
        company_name = company_names.findall(content)

        # ??????????????????
        company_hrefs = re.compile('"company_href":"(.*?)",', re.S | re.I)
        company_href = company_hrefs.findall(content)
        company_href1 = tihuan(company_href)
        # ??????????????????
        providesalary_texts = re.compile('"providesalary_text":"(.*?)",', re.S | re.I)
        providesalary_text = providesalary_texts.findall(content)
        providesalary_text1 = tihuan3(providesalary_text)
        # ??????????????????
        workarea_texts = re.compile('"workarea_text":"(.*?)",', re.S | re.I)
        workarea_text = workarea_texts.findall(content)
        workarea_text1 = tihuan(workarea_text)
        if len(workarea_text1) != len(providesalary_text1):
            workarea_text1 = workarea_text1[:-1]
        # ????????????
        issuedates = re.compile('"issuedate":"(.*?)",', re.S | re.I)
        issuedate = issuedates.findall(content)
        if len(issuedate) != len(workarea_text1):
            issuedate = issuedate[:-1]
        # ????????????
        updatedates = re.compile('"updatedate":"(.*?)",', re.S | re.I)
        updatedate = updatedates.findall(content)

        # ??????????????????
        companytype_texts = re.compile('"companytype_text":"(.*?)",', re.S | re.I)
        companytype_text = companytype_texts.findall(content)
        companytype_text1 = tihuan(companytype_text)
        #??????
        companysize_texts = re.compile('"companyind_text":"(.*?)",', re.S | re.I)
        companysize_text = companysize_texts.findall(content)
        companysize_text1 = tihuan(companysize_text)
        #??????
        attribute_texts = re.compile('"attribute_text":(.*?)"],', re.S | re.I)
        attribute_text = attribute_texts.findall(content)
        list_yaoqiu,list_xueli,list_renshu = tihuan2(attribute_text)
        list_yaoqiu = list_yaoqiu[0:50]
        list_xueli = list_xueli[0:50]
        list_renshu = list_renshu[0:50]
        if len(list_yaoqiu) != len(providesalary_text1):
            list_yaoqiu = list_yaoqiu[:-1]
        if len(list_xueli) != len(providesalary_text1):
            list_xueli = list_xueli[:-1]
        if len(list_renshu) != len(providesalary_text1):
            list_renshu = list_renshu[:-1]
        df = pd.DataFrame()
        df["????????????"] = job_name
        df["????????????"] =job_href1
        df["????????????"] = company_name
        df["????????????"] = company_href1
        df["??????"] = providesalary_text1
        df["????????????"] = workarea_text1
        df["????????????"] =issuedate
        df["????????????"] =updatedate
        df["????????????"] =companytype_text1
        df["??????"] =companysize_text1
        df["??????????????????"] =list_yaoqiu
        df["????????????"] =list_xueli
        df["????????????"] =list_renshu
        try:

            df.to_csv("51job_python_{}_{}.csv".format(riqi,miao), mode="a+", index=None, encoding="gbk")
            print("????????????")
        except:
            print("????????????????????????")
        time.sleep(1)




if __name__ == '__main__':
    get_html()
