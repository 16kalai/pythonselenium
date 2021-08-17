#  stores in "key" and "value" pair
# not allow duplicates, changeable
# Dic = { }

dic = {"brand":"name","model":"specific","year":2020}
print(dic)
print(type(dic))

#length
print(len(dic))

#keys
print(dic.keys())
#values
print(dic.values())

#get
d = dic.get("brand")  #only for keys
print(d)
c = dic.get("name")   #not for values
print(c)
#change
dic['brand'] = "kk"
print(dic)

#update
dic.update({"year":1994})
print(dic)

#add items
dic["colour"] = "red"
print(dic)

#pop specific one
dic.pop("model")
print(dic)

#pop item last one remove
dic.popitem()
print(dic)


