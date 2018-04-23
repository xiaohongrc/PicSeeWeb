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
sheet_album_info = db_win_400['sheet_album_info']


# 获取分类标题列表
def get_classify_list(request):
    result = []
    for item in sheet_classify.find():
         result.append(item)
    # print(result)
    return HttpResponse(dumps(result), content_type="application/json")


# 获取图集信息列表
def get_album_info_list(request):
    width = request.GET.get('width', None)
    albumUrl = request.GET.get('albumUrl', None)
    albumUrl = request.GET.get('whichClassify', None)
    #result = [{"title": "titlename", "age": 3}]
    result = []
    for item in sheet_album_info.find({'whichClassify':'明星'}):
         result.append(item)
    # print(result)
    return HttpResponse(dumps(result), content_type="application/json")

# result = []
# for item in sheet_album_info.find({'width': '720'}):
#     result.append(item)
# print(result)
