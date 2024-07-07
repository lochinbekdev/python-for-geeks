# Find with loop

def look_for_key(main_box):
    pile=main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grade_a_box()midmid
        for item in box:
            if item.is_a_box():
                pile.append(item)
            else:
                return "Key is found"


# Recursive  algorithm

def look_for_key_main(box):
    for item in box:
        if item.is_a_box():     #base case
            look_for_key(item)  
        else:                   #recursive case
            return "key found"