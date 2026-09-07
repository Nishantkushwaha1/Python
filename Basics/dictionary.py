
# DICTIONARY:- 

# marks{}     ---> empty dictionary

marks = {
    "Animesh": 40,
    "Gurdeep": 30,
    "Hemant": 35,
    "Nishant": 30
}

print(marks)        # {'Animesh': 40, 'Gurdeep': 30, 'Hemant': 35, 'Nishant': 30}

print(marks["Animesh"])     # 40

marks["Om"] = "35" #Adding a new item

print(marks)        # {'Animesh': 40, 'Gurdeep': 30, 'Hemant': 35, 'Nishant': 30, 'Om': '35'}


# dictionary Methods

print(marks.items())    # dict_items([('Animesh', 40), ('Gurdeep', 30), ('Hemant', 35), ('Nishant', 30), ('Om', '35')])
print(marks.keys())     # dict_keys(['Animesh', 'Gurdeep', 'Hemant', 'Nishant', 'Om'])
print(marks.values())   # dict_values([40, 30, 35, 30, '35'])

marks.update({"Nishant": 35, "Shalni": 40})

print(marks)        # {'Animesh': 40, 'Gurdeep': 30, 'Hemant': 35, 'Nishant': 35, 'Om': '35', 'Shalni': 40}

# print(marks.get("Nishant3"))     #prints none
# print(marks["Nishant3"])         #give error


