# dict_ex = ["Даниил", "Николаев", "35", ["Москва", "Северодвинск", "Челябинск"]]
dict_ex = {"name": "Даниил", "last_name": "Николаев", "age": 35, "age": 37, "cities": ["Москва", "Северодвинск", "Челябинск"], "smoke": False}
# print(dict_ex['asfe'])

# dict_ex = dict(name = 'Даниил', last_name = "Николаев")
# print(dict_ex)

# dict_ex = [["name","Даниил"], ["last_name","Николаев"]]
# del dict_ex["name"]
# print(dict(dict_ex))

# dict_ex = dict.fromkeys(["Даниил", "Николаев", "35",], 'test')
# dict_ex.clear()
# print(dict_ex)

# dict_ex2 = dict(dict_ex)
# dict_ex2["name"] = 'Даня'
# print(dict_ex2)
# name = dict_ex.get("name")
# print(name)
# dict_ex.setdefault('sfsfs', 'Дмитрий')
# print(dict_ex)

str = dict_ex.pop('sgfsfg', 'Ключа нет')
print(str)