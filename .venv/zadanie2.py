def name_sorter(names):
    sorted_names = {"female" : [], "male" : []}
    for name in names:
        if name[-1] == "a":
            sorted_names["female"].append(name)
            sorted_names["female"].sort()
        else:
            sorted_names["male"].append(name)
            sorted_names["male"].sort()
    return sorted_names

names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
print(name_sorter(names))
