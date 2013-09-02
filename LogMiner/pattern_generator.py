from external_format import cut_external_format

def get_substrate(string):

    string = cut_external_format(string)

    main_separator = [': ', ', ', ' ']
    result_value = [string]
    result_separator = ['']
    separator_list = []

    for item in main_separator:
        value_list = []
        for str in result_value:
            if len(str) > 0:
                value_list.append(str.split(item))
        result_value = []
        separator_list = []

        for i in range(0, len(value_list)):
            list = value_list[i]
            for j in range(0, len(list)):
                list_item = list[j]
                if len(list_item) > 0:
                    result_value.append(list_item)
                    if j < len(list) - 1:
                        separator_list.append(item)
                    else:
                        separator_list.append(result_separator[i])
        result_separator = separator_list

    new_string = ''
    if len(result_value) != len(result_separator):
        print('Sorry! Different length')
    else:
        for i in range(0,len(result_value)):
            new_string = new_string + result_value[i] + result_separator[i]
        if new_string != string:
            #print ('Trouble get pattern from string: "{0}"'.format(string))
            #result_delimeter = []
            #result_value = []
            flag = True
            length = len(string)
            if length < len(new_string):
                length = len(new_string)
            for i in range(0, length):
                if string[i] != new_string[i]:
                    flag = False
                    #print(new_string[0:i])
                    #print(string[0:i])
                    print(i)
                    break
            if 	flag:
                print('Tail different')
    return {'separator': result_separator, 'value': result_value}