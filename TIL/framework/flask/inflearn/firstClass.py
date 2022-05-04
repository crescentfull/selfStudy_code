# def list_creator(tag):
#     def text_wrapper(msg):
#         print('<{0}>{1}</{0}>'.format(tag,msg))
#     return text_wrapper

# ul_list_creator = list_creator('ul')
# print(ul_list_creator)

# ul_list_creator("목차")

def list_creator(tag):
    def text_wrapper(list_data):
        for item in list_data:
            print('{0} {1}'.format(tag, item))
    return text_wrapper

data_list_minus = list_creator('-')
data_list_minus(['안녕','하세요'])

data_list_mul = list_creator('*')
data_list_mul(['안녕', '하세요'])

data_list_x = list_creator('X')
data_list_x(['안녕', '하세요'])
