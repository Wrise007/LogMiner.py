def cut_external_format(str):

    n = str.find('[')
    m = str.find('<')
    k = str.find('{')

    l_max = max([n, m, k])
    #return string

    if l_max < 0:
        return str
    elif n == l_max:

        str_begin = ''
        if n > 0:
            str_begin = str[0:n]
        n_end =  str.rfind(']')
        str_end = ''
        if n_end < len(str)-1:
            str_end = str[n_end+1:len(str)]
        if n_end > n:
            if str[n:n_end].find(',') == -1:
                return str
            return str_begin + '(?P<json>[])' + str_end
        else:
            return str

    elif m == l_max:

        str_begin = ''
        if m > 0:
            str_begin = str[0:m]
        m_end =  str.rfind('>')
        str_end = ''
        if m_end < len(str)-1:
            str_end = str[m_end+1:len(str)]
        if m_end > n:
            return str_begin + '(?P<xml><>)' + str_end
        else:
            return str
    elif k == l_max:

        str_begin = ''
        if k > 0:
            str_begin = str[0:k]
        k_end =  str.rfind('}')
        str_end = ''
        if k_end < len(str)-1:
            str_end = str[k_end+1:len(str)]
        if k_end > n:
            return str_begin + '(?P<json>{})' + str_end
        else:
            return str
