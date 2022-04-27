s = "photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11"
def solution(s):
    # newS          = s.replace(",","")
    # removed_dot_s = newS.replace("."," ")
    sSlice        = s.split("\n")
    sList = list(sSlice)
    print(sList)
    sArr          = [i.split(", ") for i in sList]
    print("----------------------------------")
    print(sArr)
    print("----------------------------------")
    # sortArr = sorted(sArr, key=lambda x:x[2])
    # print(sortArr)
    # print("----------------------------------")
    
    for i in sArr:
        if i in "Warsaw":
            
            
    # a = []
    # b = []
    # c = []
    # print(sortArr[0][1])
    # for i in sortArr:
    #     if sortArr[i][1] == "Warsaw":
    #         a.append(sortArr[i][1])
    # print(a)
    # print(sArr)    
    # sArr_dict = []
    # for i in range(len(sArr)):
    #     sArr_dict.append({
    #                     "photoname":sArr[i][0],
    #                     "extension":sArr[i][1],
    #                     "city_name":sArr[i][2],
    #                     "date":sArr[i][3],
    #                     "datetime":sArr[i][4]})

    # sArr_dict_sorted = sorted(sArr_dict, key=lambda x:(x["date"],x["datetime"]))
    # print(sArr_dict_sorted)
solution(s)