# coding=utf-8
# http://rate.tmall.com/list_detail_rate.htm?itemId=41464129793&sellerId=1652490016&currentPage=1
import requests, re
from Tkinter import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def worker():
    goods_url = L_entry.get()
    pages = P_entry.get()

    detail_list = []
    detail_dict = {}
    for i in range(int(pages)):
        page = i + 1
        goods_url = re.sub(r"currentPage=\d", "currentPage=%s" % page, goods_url)
        rsp = requests.get(goods_url, headers=header)

        data = rsp.text
        data = eval(re.search(r"\{.*", data).group().strip(')').replace("false", "0").replace("true", "1"))

        for detail in data['rateDetail']['rateList']:
        #for detail in data['rateList']:
            try:
                size = detail["auctionSku"]
            except Exception as e:
                print e
                continue
            size = size.split(";")

            s1 = size[0].split(":")[1] if size else ''
            s2 = size[1].split(":")[1] if len(size)>1 else ''

            s = str(s1) + str(s2)
            if s in detail_list:
                detail_dict[s] = detail_dict[s] + 1
            else:
                detail_list.append(s)
                detail_dict[s] = 1

        root.wm_title("page%d" % page)
    root.wm_title("下载完成")
    make_image(detail_list,detail_dict)

def make_image(detail_list,detail_dict,goods_name):
    print detail_list
    print detail_dict
    colors = ['#ff0000', '#eb4310', '#f6941d', '#fbb417', '#ffff00', '#cdd541', '#99cc33', '#3f9337', '#219167',
             '#239676', '#24998d', '#1f9baa', '#0080ff', '#3366cc', '#333399', '#003366', '#800080', '#a1488e',
             '#c71585', '#bd2158']
    people = [detail.decode('utf8') for detail in detail_list]
    colors = colors[0:len(people)]
    #y轴元素数量
    y_pos = np.arange(len(people))
    #每个元素对应的值,array
    performance = [detail_dict[x] for x in detail_list]
 
    bars = plt.barh(y_pos, performance, align='center')#这里是产生横向柱状图 barh h--horizontal
    #设置颜色
    for bar,colors in zip(bars,colors):
        bar.set_color(colors)
    #y轴每个元素标签

    plt.yticks(y_pos, people)
    plt.yticks(fontsize=7)

    #x轴标题
    plt.xlabel('count')
    #x轴范围
    plt.xlim(0,max(performance))
    plt.title('size and colors count about taobao')
    plt.show()
if __name__ == '__main__':
    # goods_url = "https://rate.tmall.com/list_detail_rate.htm?itemId=527956695986&spuId=517713513&sellerId=2615125783&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=146UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockt%2FRH1IdUB%2BRXpOdiA%3D%7CU2xMHDJ7G2AHYg8hAS8XLwEhD0ghSmQyZA%3D%3D%7CVGhXd1llXGhTal9iV2lSbVlhVmtJfUN4QHpAf0ZyT3JPekB0TGI0%7CVWldfS0SMg01ACAcIAAuE2JbZlInGiYcIAUrfSs%3D%7CVmhIGCcZOQQkGCccJAQ6ADwHJxskESwMOQQ5GSUaLxIyCDcCVAI%3D%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D&isg=Ar29SH8guO4XdhyBmwNtPy2rzB938vDSpl9fGH8C9JRDtt3oR6oBfItkFN0K&needFold=0&_ksTS=1496480841428_649&callback=jsonp650"
    header = {
        "authority": "rate.tmall.com",
        "method": "GET",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, sdch, br",
        "accept-language": "zh-CN,zh;q=0.8",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    }
    root = Tk()
    root.wm_title("淘宝牛统计")
    L_label = Label(root, text="链接").grid(row=0, sticky=W)
    L_entry = Entry(root,width = 240)
    L_entry.grid(row=0, column=1, stick=E)
    P_label = Label(root, text="页数").grid(row=1, sticky=W)
    P_entry = Entry(root, width = 240)
    P_entry.grid(row=1, column=1, stick=E)
    start_btn = Button(root, text="开始",anchor = 'center', command=worker).grid(row=3)
    width = 300
    height = 100
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)
    root.mainloop()

