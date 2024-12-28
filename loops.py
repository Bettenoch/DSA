

def return_lower(list):
    final = []
    for num in list:
        prod = num.lower()
        final.append(prod)
    return final

def check_username(list1, list2):
    newList1 = return_lower(list1)
    newList2 = return_lower(list2)
    
    for user in newList2:
        if user in newList1:
            print(f"Username {user} already in use, choose another one") 
        else:
            print(f"{user} available")
            
CURRENT_USERS = ["John", "Mathew", "Victor", "Caleb", "Brian"]
NEW_USERS = ["mathew", "victor", "Allan", "Trump", "Kasongo"]

res = check_username(CURRENT_USERS, NEW_USERS)

print(res)
