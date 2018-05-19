def some_function():
    pass

def click(category): # 사실은 data.category
    sub_categories = categories[key].sub_list # sub_list에는 한 카테고리의 모든 자식들이 들어 있다.
    for sub_category in sub_categories:
        if sub_category == True: # active이면
            print('야야 선택 해제 못해.')
            return


class Object:
    subCategories = None
    pass

referenceTable = Object() # 전역 변수
categories = Object() # 역시 전역 변수

for key, data in categories: # data는 카테고리 하나.
    print(data)
    click(data, key) # 상위 카테고리를 선택 해제 할 때
    categories[key].sub_list = [] # 카테고리 하나마다 sub_list를 갖는다.
    categories[key].active_sub_list = [] # 액티브한 sub_list들만 모여 있다.
    #과연 categories[key]로 접근이 가능한가? (이게 되야 for문이 맞긴 함)
    for sub_key, sub_data in referenceTable.subCategories:
        if key == sub_key:
            print(sub_data)
            categories[key].sub_list.append(sub_data)
            if some_function() == 'selected':
                categories[key].active_sub_list.append(sub_data) # 액티브한 sub_list만 모여있다.
    if categories[key].sub_list == None:
        print('야 비었다 비었어! 추가하려면 나한테 말만 해!')


def click(category): # 사실은 data.category
    sub_categories = categories[key].sub_list # sub_list에는 한 카테고리의 모든 자식들이 들어 있다.
    for sub_category in sub_categories:
        if sub_category == True: # active이면
            print('야야 선택 해제 못해.')
            return

def click2(category): # 해결!
    #제 2의 방법
    sub_list_ = categories[key].sub_list # 자식 카테고리가 모두 들어있다.
    for sub in sub_list_:
        if some_function(sub) == 'selected':
            print('야야 해제 못해')

# def click_sub_list(sub_category):
#     if sub_category in categories[key].active_sub_list:
#         categories[key].active_sub_list.splice(sub_caategory_index)
#     else:
#         data.sub_list[sub_category.id].active = True:

