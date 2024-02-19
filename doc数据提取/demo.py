import win32com.client as win32
from os import path
import re
import os
import pandas as pd
from tqdm import tqdm
def main1(name):
    def read_doc_file(file_path):
        if not path.exists(file_path): return None

        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(file_path)


        result = []
        for paragraph in doc.Paragraphs:
            result.append(paragraph.Range.Text)

        doc.Close(False)
        return "\n".join(result)

    file_path = u'C:\\Users\\v_yuhaozeng\\Desktop\\demo\\data\\{}'.format(name)
    content = read_doc_file(file_path)
    title = re.compile(r'^([^\n]+)', re.M)
    title1 = re.search(title,content)
    # 匹配施行日期，制定机关
    pattern1 = re.compile(r'制定机关：(.*?)\n', re.S)
    pattern2 = re.compile(r'施行日期：(.*?)\n', re.S)
    pattern3 = re.compile(r'发文字号：(.*?)\n', re.S)
    # 提取施行日期，制定机关
    authority = re.search(pattern1, content)
    effective_date = re.search(pattern2, content)
    font_data = re.search(pattern3, content)

    try:
        Policy_name = str(title1.group(1).strip())
    except:
        Policy_name = " "
    try:
        Establishing_authority = str(authority.group(1).strip())
    except:
        Establishing_authority = " "
    try:
        Implementation_date = str(effective_date.group(1).strip())
    except:
        Implementation_date = " "
    try:
        Issue_number = str(font_data.group(1).strip())
    except:
        Issue_number = " "

    def find_sentence(text, keyword):
        pattern = r'[^。]*?{}[^。]*。'.format(keyword)
        result = re.findall(pattern,text)
        if len(result) != 0:
            result1 = "\\".join(result)
            result1 = result1.replace("\r"," ").replace("\n"," ").replace("\u3000"," ").strip(" ")
            return result1
        else:
            return " "

    text1 = find_sentence(content,'规模')
    text2 = find_sentence(content,'家庭农场')

    df = pd.DataFrame()
    df['政策名称'] = [Policy_name]
    df['施行时间'] = [Establishing_authority]
    df['制定机关'] = [Implementation_date]
    df['发文字号'] = [Issue_number]
    df['包含规模的句子'] = [text1]
    df['包含家庭农场的句子'] = [text2]
    df.to_csv('data.csv',encoding='utf-8-sig',mode="a+",header=False,index=False)

if __name__ == '__main__':
    def get_all_file_names(directory_path):
        return os.listdir(directory_path)

    directory_path = "data"  # 你的文件夹路径
    file_names = get_all_file_names(directory_path)
    df = pd.DataFrame()
    df['政策名称'] = ['政策名称']
    df['施行时间'] = ['施行时间']
    df['制定机关'] = ['制定机关']
    df['发文字号'] = ['发文字号']
    df['包含规模的句子'] = ['包含规模的句子']
    df['包含家庭农场的句子'] = ['包含家庭农场的句子']
    df.to_csv('data.csv', encoding='utf-8-sig', mode="w", header=False, index=False)
    for i in tqdm(file_names):
        main1(i)