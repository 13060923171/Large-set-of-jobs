import pandas as pd
import numpy as np
import os

#求出各科的平均值
def sum_average():
    # name = '成绩样板'
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path,sheet_name='Sheet1').loc[1:,]
    d = {}
    language_mean = df['语文'].agg('mean')
    language_mean = '%0.2lf' % language_mean
    mathematics_mean = df['数学'].agg('mean')
    mathematics_mean = '%0.2lf' % mathematics_mean
    english_mean = df['英语'].agg('mean')
    english_mean = '%0.2lf' % english_mean
    think_mean = df['思品'].agg('mean')
    think_mean = '%0.2lf' % think_mean
    science_mean = df['科学'].agg('mean')
    science_mean = '%0.2lf' % science_mean
    d['语文'] = language_mean
    d['数学'] = mathematics_mean
    d['英语'] = english_mean
    d['思品'] = think_mean
    d['科学'] = science_mean
    df1 = pd.DataFrame(
        list(d.items()),
        columns=['科目','平均值']
    )
    return df1

#求出各个学校各科的平均值
def classify_mean():
    # name = '成绩样板'
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path, sheet_name='Sheet1').loc[1:, ['学校','语文','数学','英语','思品','科学']]
    df = df.replace(0,value=np.NaN)
    df2 = df.groupby('学校').agg('mean')

    def number(x):
        x = '%0.2lf' %x
        return x
    df2['语文'] = df2['语文'].apply(number)
    df2['数学'] = df2['数学'].apply(number)
    df2['英语'] = df2['英语'].apply(number)
    df2['思品'] = df2['思品'].apply(number)
    df2['科学'] = df2['科学'].apply(number)
    df2.columns = ['语文-平均值','数学-平均值','英语-平均值','思品-平均值','科学-平均值']
    return df2


def reference_rate():
    # name = '成绩样板'
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path, sheet_name='Sheet1').loc[1:, ['语文', '数学', '英语', '思品', '科学']]
    df1 = df.isnull().sum()
    x = list(df1.index)
    y = list(df1.values)
    z = [len(df['语文']),len(df['数学']),len(df['英语']),len(df['思品']),len(df['科学'])]
    d = {}
    for j,k,l in zip(x,y,z):
        reference = "%0.4lf" %float(float((l-k)/l) * 100)
        reference = str(reference) + '%'
        d[j] = reference
    df2 = pd.DataFrame(list(d.items()),columns=['科目', '参考率'])

    return df2


def qualified_excellent():
    # name = '成绩样板'
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path, sheet_name='Sheet1').loc[1:, ['语文', '数学', '英语', '思品', '科学']]
    df = df.replace(np.NaN,0)
    #语文合格率
    df = df.astype(int)
    def language_tihuan(x):
        if x < 90:
            return 0
        elif x >= 90 and x < 120:
            return 1
        else:
            return 2
    def english_tihuan(x):
        if x < 72:
            return 0
        elif x >= 72 and x < 96:
            return 1
        else:
            return 2

    def think_tihuan(x):
        if x < 30:
            return 0
        elif x >= 30 and x < 40:
            return 1
        else:
            return 2
    df['语文'] = df['语文'].apply(language_tihuan)
    df['数学'] = df['数学'].apply(english_tihuan)
    df['英语'] = df['英语'].apply(english_tihuan)
    df['思品'] = df['思品'].apply(think_tihuan)
    df['科学'] = df['科学'].apply(think_tihuan)
    list_name = ['语文','数学','英语','思品','科学']
    sum_data = []
    for l in list_name:
        hege = float(float(len(df.loc[df[l]==1,l]) / len(df[l])))
        he1 ='%0.2lf' %float(float(hege) * 100)
        hege = str(he1) + "%"
        yx = float(float(len(df.loc[df[l]==2,l]) / len(df[l])))
        yx1 = '%0.2lf' % float(float(yx) * 100)
        yx = str(yx1) + "%"
        d = {
            '科目':l,
            '合格率':hege,
            '优秀率':yx,
        }
        sum_data.append(d)

    df2 = pd.DataFrame(
        sum_data,
        columns=['科目','合格率','优秀率']
    )
    return df2


def student_qualified():
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path, sheet_name='Sheet1').loc[1:, ['学校','语文', '数学', '英语', '思品', '科学']]
    df = df.replace(np.NaN, 0)

    def qualified_excellent(x):
        df = x
        def language_tihuan(x):
            if x < 90:
                return 0
            elif x >= 90 and x < 120:
                return 1
            else:
                return 2

        def english_tihuan(x):
            if x < 72:
                return 0
            elif x >= 72 and x < 96:
                return 1
            else:
                return 2

        def think_tihuan(x):
            if x < 30:
                return 0
            elif x >= 30 and x < 40:
                return 1
            else:
                return 2

        df['语文'] = df['语文'].apply(language_tihuan)
        df['数学'] = df['数学'].apply(english_tihuan)
        df['英语'] = df['英语'].apply(english_tihuan)
        df['思品'] = df['思品'].apply(think_tihuan)
        df['科学'] = df['科学'].apply(think_tihuan)
        list_name = ['语文', '数学', '英语', '思品', '科学']
        sum_data = []
        for l in list_name:
            hege = float(float(len(df.loc[df[l] == 1, l]) / len(df[l])))
            he1 = '%0.2lf' % float(float(hege) * 100)
            hege = str(he1) + "%"
            sum_data.append(hege)
        return sum_data

    data1 = df.groupby('学校').apply(qualified_excellent)
    sum_data = []
    for n,l in zip(list(data1.index),list(data1.values)):
        d = {
            '学校':n,
            '语文-合格率': l[0],
            '数学-合格率': l[1],
            '英语-合格率': l[2],
            '思品-合格率': l[3],
            '科学-合格率': l[4],
        }
        sum_data.append(d)
    df = pd.DataFrame(sum_data, columns=['学校', '语文-合格率', '数学-合格率', '英语-合格率', '思品-合格率','科学-合格率'])
    return df


def student_excellent():
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path, sheet_name='Sheet1').loc[1:, ['学校','语文', '数学', '英语', '思品', '科学']]
    df = df.replace(np.NaN, 0)

    def qualified_excellent(x):
        df = x
        def language_tihuan(x):
            if x < 90:
                return 0
            elif x >= 90 and x < 120:
                return 1
            else:
                return 2

        def english_tihuan(x):
            if x < 72:
                return 0
            elif x >= 72 and x < 96:
                return 1
            else:
                return 2

        def think_tihuan(x):
            if x < 30:
                return 0
            elif x >= 30 and x < 40:
                return 1
            else:
                return 2

        df['语文'] = df['语文'].apply(language_tihuan)
        df['数学'] = df['数学'].apply(english_tihuan)
        df['英语'] = df['英语'].apply(english_tihuan)
        df['思品'] = df['思品'].apply(think_tihuan)
        df['科学'] = df['科学'].apply(think_tihuan)
        list_name = ['语文', '数学', '英语', '思品', '科学']
        sum_data = []
        for l in list_name:
            yx = float(float(len(df.loc[df[l] == 2, l]) / len(df[l])))
            yx1 = '%0.2lf' % float(float(yx) * 100)
            yx = str(yx1) + "%"
            sum_data.append(yx)

        return sum_data

    data1 = df.groupby('学校').apply(qualified_excellent)
    sum_data = []
    for n, l in zip(list(data1.index), list(data1.values)):
        d = {
            '学校': n,
            '语文-优秀率': l[0],
            '数学-优秀率': l[1],
            '英语-优秀率': l[2],
            '思品-优秀率': l[3],
            '科学-优秀率': l[4],
        }
        sum_data.append(d)
    df = pd.DataFrame(sum_data, columns=['学校', '语文-优秀率', '数学-优秀率', '英语-优秀率', '思品-优秀率', '科学-优秀率'])
    return df


def total_qualified():
    # name = '成绩样板'
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path, sheet_name='Sheet1').loc[1:, ['语文', '数学', '英语', '思品', '科学']]
    df = df.replace(np.NaN, 0)
    # 语文合格率
    df = df.astype(int)

    def language_tihuan(x):
        if x < 90:
            return 0
        elif x >= 90 and x < 120:
            return 1
        else:
            return 2

    def english_tihuan(x):
        if x < 72:
            return 0
        elif x >= 72 and x < 96:
            return 1
        else:
            return 2

    def think_tihuan(x):
        if x < 30:
            return 0
        elif x >= 30 and x < 40:
            return 1
        else:
            return 2

    df['语文'] = df['语文'].apply(language_tihuan)
    df['数学'] = df['数学'].apply(english_tihuan)
    df['英语'] = df['英语'].apply(english_tihuan)
    df['思品'] = df['思品'].apply(think_tihuan)
    df['科学'] = df['科学'].apply(think_tihuan)
    count1 = 0
    count2 = 0
    for d1,d2,d3,d4,d5 in zip(df['语文'],df['数学'],df['英语'],df['思品'],df['科学']):
        if d1 !=0 and d2 !=0 and d3 != 0:
            count1 += 1
        if d1 != 0 and d2 != 0 and d3 != 0 and d4 != 0 and d5 != 0:
            count2 +=1

    qualified_3 = '%0.2lf' %float(float(count1 / len(df)) * 100)
    qualified_3 = str(qualified_3) + '%'
    qualified_5 = '%0.2lf' % float(float(count2 / len(df)) * 100)
    qualified_5 = str(qualified_5) + '%'

    d = {
        '三科合格率':qualified_3,
        '五科合格率':qualified_5
    }

    df2 = pd.DataFrame(
        list(d.items()),
        columns=['科目','合格率']
    )

    return df2

def ranking():
    # name = '成绩样板'
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path, sheet_name='Sheet1').loc[1:, ['学校','语文', '数学', '英语', '思品', '科学']]

    # 求总分
    def sum_average(x):
        df = x
        language_mean = df['语文'].agg('mean')
        language_mean = '%0.2f' % language_mean
        mathematics_mean = df['数学'].agg('mean')
        mathematics_mean = '%0.2f' % mathematics_mean
        english_mean = df['英语'].agg('mean')
        english_mean = '%0.2f' % english_mean
        think_mean = df['思品'].agg('mean')
        think_mean = '%0.2f' % think_mean
        science_mean = df['科学'].agg('mean')
        science_mean = '%0.2f' % science_mean
        sum_grade = float(language_mean) + float(mathematics_mean) + float(english_mean) + float(think_mean) + float(science_mean)
        return sum_grade

    #参考率
    def reference_rate(x):
        df = x
        df1 = df.isnull().sum()
        x = list(df1.index)
        y = list(df1.values)
        z = [len(df['语文']), len(df['数学']), len(df['英语']), len(df['思品']), len(df['科学'])]
        sum_data = []
        for j, k, l in zip(x, y, z):
            reference = "%0.4lf" % float(float((l - k) / l) * 100)
            sum_data.append(float(reference))
        content = '%0.4lf' %float(sum(sum_data) / len(sum_data))
        return content

    def qualified_3(x):
        df = x
        df = df.replace(np.NaN, 0)
        # 语文合格率
        # df = df.astype(int)

        def language_tihuan(x):
            if x < 90:
                return 0
            elif x >= 90 and x < 120:
                return 1
            else:
                return 2

        def english_tihuan(x):
            if x < 72:
                return 0
            elif x >= 72 and x < 96:
                return 1
            else:
                return 2

        def think_tihuan(x):
            if x < 30:
                return 0
            elif x >= 30 and x < 40:
                return 1
            else:
                return 2

        df['语文'] = df['语文'].apply(language_tihuan)
        df['数学'] = df['数学'].apply(english_tihuan)
        df['英语'] = df['英语'].apply(english_tihuan)
        df['思品'] = df['思品'].apply(think_tihuan)
        df['科学'] = df['科学'].apply(think_tihuan)
        count1 = 0
        for d1, d2, d3, d4, d5 in zip(df['语文'], df['数学'], df['英语'], df['思品'], df['科学']):
            if d1 != 0 and d2 != 0 and d3 != 0:
                count1 += 1

        qualified_3 = '%0.2lf' % float(float(count1 / len(df)) * 100)
        return qualified_3

    def qualified_5(x):
        df = x
        df = df.replace(np.NaN, 0)
        # df = df.astype(int)
        def language_tihuan(x):
            if x < 90:
                return 0
            elif x >= 90 and x < 120:
                return 1
            else:
                return 2

        def english_tihuan(x):
            if x < 72:
                return 0
            elif x >= 72 and x < 96:
                return 1
            else:
                return 2

        def think_tihuan(x):
            if x < 30:
                return 0
            elif x >= 30 and x < 40:
                return 1
            else:
                return 2

        df['语文'] = df['语文'].apply(language_tihuan)
        df['数学'] = df['数学'].apply(english_tihuan)
        df['英语'] = df['英语'].apply(english_tihuan)
        df['思品'] = df['思品'].apply(think_tihuan)
        df['科学'] = df['科学'].apply(think_tihuan)
        count2 = 0
        for d1, d2, d3, d4, d5 in zip(df['语文'], df['数学'], df['英语'], df['思品'], df['科学']):
            if d1 != 0 and d2 != 0 and d3 != 0 and d4 != 0 and d5 != 0:
                count2 += 1

        qualified_5 = '%0.2lf' % float(float(count2 / len(df)) * 100)
        return qualified_5

    data1 = df.groupby('学校').apply(reference_rate)
    data2 = df.groupby('学校').apply(sum_average)
    data3 = df.groupby('学校').apply(qualified_3)
    data4 = df.groupby('学校').apply(qualified_5)
    sum_data = []
    for n1,d1,d2,d3,d4 in zip(list(data1.index),list(data1.values),list(data2.values),list(data3.values),list(data4.values)):
        ranking = '%0.3lf' %float(float(d1) * 0.1 + float(d2) * 0.4 + float(d3) * 0.3 + float(d4) * 0.2)
        d = {
            '学校':n1,
            '综合评分':float(ranking),
            '参考率': d1,
            '平均分':d2,
            '三合率':d3,
            '五合率':d4
        }
        sum_data.append(d)
    sum_data.sort(key=lambda x:x['综合评分'],reverse=True)
    df5 = pd.DataFrame(sum_data,columns=['学校','综合评分','参考率','平均分','三合率','五合率'])
    df5['排名'] = df5.index + 1
    return df5


def student_ranking():
    # name = '成绩样板'
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path, sheet_name='Sheet1').loc[1:, ['学校', '语文', '数学', '英语', '思品', '科学']]
    df = df.replace(np.NaN, 0)
    data1 = df.groupby('学校').agg('mean')
    data1['语文'] = data1['语文'].rank(method='first',ascending=False)
    data1['数学'] = data1['数学'].rank(method='first', ascending=False)
    data1['英语'] = data1['英语'].rank(method='first', ascending=False)
    data1['思品'] = data1['思品'].rank(method='first', ascending=False)
    data1['科学'] = data1['科学'].rank(method='first', ascending=False)
    data1['语文'] = data1['语文'].astype(int)
    data1['数学'] = data1['数学'].astype(int)
    data1['英语'] = data1['英语'].astype(int)
    data1['思品'] = data1['思品'].astype(int)
    data1['科学'] = data1['科学'].astype(int)
    data1.columns = ['语文-排名', '数学-排名', '英语-排名', '思品-排名', '科学-排名']
    return data1


def class_ranking():
    # name = '成绩样板'
    path = './原始数据表/{}.xlsx'.format(name)
    df = pd.read_excel(path, sheet_name='Sheet1').loc[1:, ['学校','班级', '语文', '数学', '英语', '思品', '科学']]
    df = df.replace(np.NaN, 0)
    data1 = df.groupby(['学校','班级']).agg('mean')
    data1['语文'] = data1['语文'].rank(method='first', ascending=False)
    data1['数学'] = data1['数学'].rank(method='first', ascending=False)
    data1['英语'] = data1['英语'].rank(method='first', ascending=False)
    data1['思品'] = data1['思品'].rank(method='first', ascending=False)
    data1['科学'] = data1['科学'].rank(method='first', ascending=False)
    data1['语文'] = data1['语文'].astype(int)
    data1['数学'] = data1['数学'].astype(int)
    data1['英语'] = data1['英语'].astype(int)
    data1['思品'] = data1['思品'].astype(int)
    data1['科学'] = data1['科学'].astype(int)
    return data1


def comparison_table():
    name1 = input('请输入去年表名称:')
    path = './分析结果表/{}.xlsx'.format(name1)
    df = pd.read_excel(path, sheet_name='综合排名').loc[:,['平均分','三合率','五合率','排名']]
    name2 = input('请输入今年表名称:')
    path1 = './分析结果表/{}.xlsx'.format(name2)
    df1 = pd.read_excel(path1, sheet_name='综合排名').loc[:, ['平均分', '三合率', '五合率', '排名']]
    name3 = input('请输入明年表名称:')
    path2 = './分析结果表/{}.xlsx'.format(name3)
    df2 = pd.read_excel(path2, sheet_name='综合排名').loc[:, ['平均分', '三合率', '五合率', '排名']]

    df3 = df2 - df1
    df4 = df2 - df
    writer = pd.ExcelWriter(os.path.join(os.getcwd(), './分析结果表/对比结果表.xlsx'))
    df3.to_excel(writer, sheet_name='明年-今年')
    df4.to_excel(writer, sheet_name='明年-去年')
    writer.save()


if __name__ == '__main__':
    print('*'*50)
    print('请输入功能选择:')
    print('1是获取综合表,2是获取对比结果表,3是退出程序')
    while True:
        a = input('请输入功能选项:')
        if int(a) == 1:
            name = input('请输入要计算的表名称:')
            print('请等待片刻')
            df10 = sum_average()
            df11 = classify_mean()
            df12 = reference_rate()
            df13 = qualified_excellent()
            df14 = total_qualified()
            df15 = ranking()
            df16 = student_ranking()
            df17 = class_ranking()
            df18 = student_qualified()
            df19 = student_excellent()
            result = pd.merge(df10,df12,on=['科目'])
            result1 = pd.merge(result,df13,on=['科目'])
            result2 = pd.concat([result1,df14],axis=0,join='outer')

            result3 = pd.merge(df11,df18,on=['学校'])
            result4 = pd.merge(result3, df19, on=['学校'])
            result5 = pd.merge(result4, df15, on=['学校'])
            result6 = result5.drop(['综合评分','平均分','排名','参考率'],axis=1)
            result6['三合率'] = result6['三合率'] + '%'
            result6['五合率'] = result6['五合率'] + '%'
            result7 = pd.merge(result6, df16, on=['学校'])
            writer = pd.ExcelWriter(os.path.join(os.getcwd(), './分析结果表/{}-综合表.xlsx'.format(name)))
            result2.to_excel(writer, sheet_name='全部信息')
            result7.to_excel(writer, sheet_name='学校各科信息')
            df15.to_excel(writer, sheet_name='综合排名')
            # df16.to_excel(writer, sheet_name='分类排名-学校各科排名')
            df17.to_excel(writer, sheet_name='分类排名-班级学科排名')
            writer.save()
            print('运行完毕')
        elif int(a) == 2:
            comparison_table()
            print('运行完毕')
        else:
            break