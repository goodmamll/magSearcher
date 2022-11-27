from tkinter import *
import re
import requests
import subprocess



if __name__=="__main__":
    def changeType(typeVar):

        dic = {
            '电影': '1',
            '电视剧': '2',
            '综艺': '99',
            '动漫': '16',
        }
        global type
        type=dic[typeVar]
        print("类型改变"+(type))
    def thunder():

        subprocess.Popen("C:/Program Files (x86)/Thunder Network/Thunder/Program/Thunder.exe")
    def bksearch():


        ret_show = Text(root, font=('微软雅黑', 11))
        ret_show.place(x=1, y=80, relheight=1, width=900)

        get1 = enter.get()
        get2 = get1.strip()

        if get2 == 'out':
            exit(0)
        print("please wait...")
        try:


            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.9231 SLBChan/25'
            }
            url = 'http://s.ygdy8.com/plus/so.php?'
            kw = get2
            temp_de = kw.encode("gbk")
            global type
            param = {
                'typeid': type,
                'keyword': temp_de
            }
            print(type)
            respond = requests.get(url, param, headers=headers)
            respond.encoding = 'gbk'
            page_text = respond.text


            obj = re.compile(r"<td width='55%'><b><a href='(?P<add>.*?)'>", re.S)
            child_href_list = []
            result1 = obj.finditer(str(page_text))
            ret_show.insert(END, " 搜索结果:" + '\n' * 2)
            ret_show.insert(END, " -------------------------" + '\n' * 2)

            for i in result1:

                child_href = 'https://www.ygdy8.com' + i.group("add")

                child_href_list.append(child_href)
                if(type==1):


                    obj1 = re.compile(
                        r'◎译.*?名(?P<name1>.*?)<br />◎片　　名(?P<name2>.*?)<br />.*?<a target="_blank" href="(?P<mag>.*?)"><strong>',
                        re.S)
                    obj2 = re.compile(
                        r'◎译.*?名(?P<name1>.*?)<br />◎片　　名(?P<name2>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<mag>.*?)">',
                        re.S)



                    for href in child_href_list:
                        chid_resp = requests.get(href, headers)
                        chid_resp.encoding = 'gbk'
                        respond = chid_resp.text
                        result2 = obj1.finditer(str(respond))
                        result3 = obj2.finditer(str(respond))

                        for i in result2:
                            ret_show.insert(END, " 电影名称："+i.group("name1").strip()+i.group("name2")+'\n'*2)
                            ret_show.insert(END, " 磁力链接为："+i.group("mag")+'\n')
                            ret_show.insert(END, " -------------------------" + '\n' * 2)

                        for i in result3:

                            ret_show.insert(END, " 电影名称："+i.group("name1").strip()+i.group("name2")+'\n'*2)
                            ret_show.insert(END, " 磁力链接为："+i.group("mag")+'\n')
                            ret_show.insert(END, " -------------------------" + '\n' * 2)
                if(type!=1):

                    obj3 = re.compile(r'<div class="title_all"><h1><font color=#07519a>(?P<name>.*?)</font>',re.S)
                    obj4=re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<mag>.*?)">',re.S)


                    for href in child_href_list:
                        print(href)
                        chid_resp = requests.get(href, headers)
                        chid_resp.encoding = 'gbk'
                        respond = chid_resp.text
                        result1 = obj3.finditer(str(respond))
                        result2 = obj4.finditer(str(respond))
                        for i in result1:
                            ret_show.insert(END, " 电视剧名称："+i.group("name").strip()+'\n'*2)

                        for i in result2:
                            ret_show.insert(END, " 磁力链接为："+i.group("mag")+'\n')
                            ret_show.insert(END, " -------------------------" + '\n' * 2)


        except Exception as e:
            print("Faild!")
            print(repr(e))


    root = Tk()
    root.title('电影搜索器')
    root.geometry('900x500')


    type=1

    enter = Entry(root, font=('微软雅黑', 20))
    enter.place(x=10, y=5, relheight=0.13, width=500)

    ret_show = Text(root, font=('微软雅黑', 11))
    ret_show.place(x=0, y=80, relheight=1, width=900)


    searchButton = Button(root, text='查询',command=bksearch)
    searchButton.place(x=660, y=5, relheight=0.13, width=100)


    thunderButton = Button(root, text='打开迅雷', command=thunder)
    thunderButton.place(x=780, y=5, relheight=0.13, width=100)


    typeVar = StringVar()
    typeFamily = ('电影','电视剧','综艺','动漫')
    mtype=typeVar.set(typeFamily[0])
    optiontype =OptionMenu(root,typeVar,*typeFamily,command=changeType)
    optiontype.place(x=500, y=5, relheight=0.13, width=100)

    root.mainloop()