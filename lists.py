def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        remove_elements 
        list_to_remove_elements.pop(0)
        list_to_remove_elements.pop(3)
        list_to_remove_elements.pop(3)
        return list_to_remove_elements
    elif len(list_to_remove_elements) == 5:
        list_to_remove_elements.pop(0)
        list_to_remove_elements.pop(3)
        return list_to_remove_elements
    elif len(list_to_remove_elements) == 4:
        list_to_remove_elements.pop(0)
        return list_to_remove_elements
    else:
        return []

def add_elements(list_to_add_elements):
    list_to_add_elements.append("Yellow")
    list_to_add_elements.insert(0, "Pink")
    return list_to_add_elements

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        print(True)
        return True
    else:
        print(False)
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    elif len(list_to_compare1) < 2 or len(list_to_compare2) < 2:
        return False 

def list_of_lists(list_of_lists_to_modify): 
    if len(list_of_lists_to_modify) != 3:
        return "No se puede realizar la operación"
    list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]
    list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
    return list_of_lists_to_modify
