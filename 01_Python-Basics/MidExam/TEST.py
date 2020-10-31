list_names = input().split("#")
final_list = []
final_final_list = []
for items in list_names:
    temp_list = items.split(".")
    if len(temp_list) > 2:
        final_list += temp_list
for item in final_list:
    if len(item.split()) < 2:
        final_final_list.append(item)

for i in range(len(final_final_list)):
    if i%2 == 0:
        print(f"{final_final_list[i]} {final_final_list[i+1]}")



# Welcome to #EMIS. If you need any help from HR you can write to #Milo.Minderbinder. For any technical problems you should contact #Major.Major. If you need any smart advises, please contact #Ali.Baba or #John.Yossarian. When you are sick, please stay at #Home.
