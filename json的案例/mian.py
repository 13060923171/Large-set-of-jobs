import json


def updata_city():
    citys = {}
    while True:
        #增
        print('请选择对应功能')
        print('a – 新增城市')
        print('q -- 退出')
        a = str(input('请选择城市编码:'))
        if a == 'a':
            print('增加了城市后')
            print('0 -- 北京')
            print('1 -- 上海')
            print('a – 新增城市')
            print('d – 删除城市')
            print('u – 修改城市名')
            print('s – 保存')
            print('q -- 退出')
            b = str(input('请选择城市编码:'))

            if b == '0':
                print('您选择了城市北京')
                print('a – 增加区')
                print('b – 返回上一级')
                print('s – 保存')
                print('q – 退出')
                r = str(input('请选择北京市的区:'))
                if r == 'a':
                    print('增加区')
                    print('0 – 海淀区')
                    print('1 – 朝阳区')
                    print('a – 增加区')
                    print('d – 删除区')
                    print('u – 修改区名')
                    print('b – 返回上一级')
                    print('s – 保存')
                    print('q – 退出')
                    y = str(input('请选择北京市的区:'))

                    if y == '0':
                        print('0 -- 香山')
                        print('1 -- 清华大学')
                        print('a – 增加景点')
                        print('d – 删除景点')
                        print('u – 修改景点')
                        print('b – 返回上一级')
                        print('s – 保存')
                        print('q – 退出')
                        p = str(input('请选择海淀区的著名景点:'))
                        if p == '0':
                            citys['北京'] = {
                                "海淀区": {"香山": "秋天看红叶的地方", }
                            }
                        if p == '1':
                            citys['北京'] = {
                                "朝阳区": {"清华大学": "自强不息，厚德载物"}
                            }

                        if p == 'a':
                            print('增加景点')
                            print('0 -- 香山')
                            print('1 -- 清华大学')
                            u = str(input('请选择景点编码:'))
                            if u == '0':
                                citys['北京'] = {
                                    "海淀区": {"香山": "秋天看红叶的地方", }
                                }
                            if u == '1':
                                citys['北京'] = {
                                    "朝阳区": {"清华大学": "自强不息，厚德载物"}
                                }
                        # 删
                        if p == 'd':
                            print('0 -- 香山')
                            print('1 -- 清华大学')
                            i = str(input('请选择删除景点:'))

                            if i == '0':
                                citys.pop('香山')
                            if i == '1':
                                citys.pop('清华大学')

                        # 改
                        if p == 'u':
                            print('0 -- 香山')
                            print('1 -- 清华大学')
                            o = str(input('请选择修改景点:'))
                            if o == '0':
                                e = str(input('香山要被修改的名称:'))
                                citys[e] = citys.pop("香山")
                            if o == '1':
                                e = str(input('清华大学要被修改的名称:'))
                                citys[e] = citys.pop("清华大学")

                        if p == 'b':
                            print('返回上一级')
                            continue
                        # 保存
                        if p == 's':
                            # json_str = json.dumps(citys)
                            with open('city.json', 'w', encoding='utf-8') as json_file:
                                json.dump(citys, json_file, ensure_ascii=False, indent=4)
                            print('保存成功')
                            break

                        if p == 'q':
                            print('退出')
                            break

                    if y == '1':
                        citys['北京'] = {
                            "朝阳区": {}
                        }

                    if y == 'a':
                        print('增加区')
                        print('0 -- 海淀区')
                        print('1 -- 朝阳区')
                        u = str(input('请选择城市编码:'))
                        if u == '0':
                            citys['北京'] = {
                                "海淀区": {}
                            }
                        if u == '1':
                            citys['北京'] = {
                                "朝阳区": {}
                            }
                        # 删
                        if y == 'd':
                            print('0 -- 海淀区')
                            print('1 -- 朝阳区')
                            i = str(input('请选择删除城市:'))
                            if i == '0':
                                citys.pop('海淀区')
                            if i == '1':
                                citys.pop('朝阳区')

                        # 改
                        if y == 'u':
                            print('0 -- 海淀区')
                            print('1 -- 朝阳区')
                            o = str(input('请选择修改区名:'))
                            if o == '0':
                                e = str(input('海淀区要被修改的名称:'))
                                citys[e] = citys.pop("海淀区")
                            if o == '1':
                                e = str(input('朝阳区要被修改的名称:'))
                                citys[e] = citys.pop("朝阳区")

                        if y == 'b':
                            print('返回上一级')
                            continue
                        # 保存
                        if y == 's':
                            # json_str = json.dumps(citys)
                            with open('city.json', 'w', encoding='utf-8') as json_file:
                                json.dump(citys, json_file, ensure_ascii=False, indent=4)
                            print('保存成功')
                            break

                        if y == 'q':
                            print('退出')
                            break
                if r == 'b':
                    print('返回上一级')
                    continue
                if r == 's':
                    print('保存')
                    with open('city.json', 'w', encoding='utf-8') as json_file:
                        json.dump(citys, json_file, ensure_ascii=False, indent=4)
                    break
                if r == 'q':
                    print('退出')
                    break
            if b == '1':
                citys['上海'] = {}

            if b == 'a':
                print('0 -- 北京')
                print('1 -- 上海')
                f = str(input('请选择城市编码:'))
                if f == '0':
                    citys['北京'] = {}
                if f == '1':
                    citys['上海'] = {}
            #删
            if b == 'd':
                print('0 -- 北京')
                print('1 -- 上海')
                c = str(input('请选择删除城市:'))
                if c == '0':
                    citys.pop('北京')
                if c == '1':
                    citys.pop('上海')

            #改
            if b == 'u':
                print('0 -- 北京')
                print('1 -- 上海')
                d = str(input('请选择修改城市名:'))
                if d == '0':
                    e = str(input('北京要被修改的名称:'))
                    citys[e] = citys.pop("北京")
                if d == '1':
                    e = str(input('上海要被修改的名称:'))
                    citys[e] = citys.pop("上海")

            #保存
            if b == 's':
                # json_str = json.dumps(citys)
                with open('city.json', 'w',encoding='utf-8') as json_file:
                    json.dump(citys, json_file,ensure_ascii=False,indent=4)
                print('保存成功')
                break

            if b == 'q':
                print('退出')
                break
        #退出
        elif a == 'q':
            print('退出')
            break


if __name__ == '__main__':
    updata_city()

