#Dictionary
# academy1={
#     "13_rooom":"python",
#     "12_room":"c#",
#     "11_room":"cyber security",
#     "10_room":["chief ceo","secratary"],
# }
# print(academy1['10_room'][1])
# print(academy1.get("13_rooom"))
# print(academy1.keys())
# academy1.update({"11_room":"startup"})
# academy1.update({"9_room":'c++'})
# print(academy1)

# academy2=dict(
#     name="bobur akilhanov",
#     age=41,
#     country="tashkent"
# )
# academy3 = academy2.copy()
# print(academy3)
# for x in academy2.keys():
#     print(x)
# for x in academy2.values():
#     print(x)
# for x in academy2.items():
#     print(x)
# print(academy2["age"])
# academy2['name']="said"
# print(academy2)

# item={
#     'tree1':{
#         "type":"yablochniy",
#         "age":100,
#         "color_leaves":"brown"
#     },
#     'tree2':{
#         "type":"ogurtsoviy",
#         "age":150,
#         "color_leaves":"white"
#     },
#     'tree3': {
#         "type": "arbuzniy",
#         "age": 300,
#         "color_leaves": "orange"
#     },
# }
# print(item["tree2"]["age"])
# print(item["tree2"]["color_leaves"])

# car={
#     "marka":"ford",
#     "model":"mustang",
#     "year":1964
# }
# print(car.get("model"))
# print(car.get("year"))
# car.update({"color":"red"})
# print(car)
# car.pop("model")
# print(car)
# car.clear()
# print(car)
