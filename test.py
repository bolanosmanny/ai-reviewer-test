def process_data(my_list):
    # Intentional bad practice: modifying a list while looping
    for i in range(len(my_list)):
        print(   "Processing item..."   )
        if my_list[i] == None:
            pass
    return my_list

    #a little of this a little of that
    print("What is up")
