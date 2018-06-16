import pymongo as pymongo
from django.shortcuts import render
from bson.json_util import dumps
from django.http import HttpResponse

# Create your views here.

client = pymongo.MongoClient('localhost', 27017)
db_win_400 = client['win400']
# 分类的url数据库
sheet_classify = db_win_400['sheet_classify']


# 分类下的图集列表数据库
# 单个图集的信息数据库

def cantonese_privacy(request):
    return render(request,'cantonese_privacy.html')

def choose_db_by_country(country):
    country_classify = {'US': 'sheet_album_info_oumei', 'IN': 'sheet_album_info_yindu', 'KR': 'sheet_album_info_hanguo',
                        'JP': 'sheet_album_info_riben', 'RU': 'sheet_album_info_eluosi'}
    return country_classify.get(country)


# 获取配置
def get_server_config(request):
    result = [{"mode_normal": True}]
    return HttpResponse(dumps(result), content_type="application/json")


# 获取分类标题列表
def get_classify_list(request):
    result = []
    for item in sheet_classify.find():
        result.append(item)
    # print(result)
    return HttpResponse(dumps(result), content_type="application/json")


# 获取图集信息列表
def get_album_info_list(request):
    limit = int(request.GET.get('limit', '30'))
    page = int(request.GET.get('page', '0'))
    whichClassify = request.GET.get('whichClassify', 'classify_mingxing')
    country = request.GET.get('country', 'US')
    sheet_album_info = db_win_400['sheet_album_info']

    by_country = choose_db_by_country(country)

    # if (whichClassify == 'classify_meinv' and (by_country is not None)):
    #     sheet_album_info = db_win_400[by_country]

    result = []
    for item in sheet_album_info.find({'whichClassify': whichClassify}).skip(page * limit).limit(limit):
        result.append(item)
    # print(result)
    return HttpResponse(dumps(result), content_type="application/json")
