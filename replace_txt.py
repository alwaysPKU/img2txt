txt=''
with open('shaonianpai2') as f:
    lines = f.readlines()
    for line in lines:
        txt=txt+line
print(txt)
with open("./output2.txt") as f:
    len_txt = len(txt)
    print(len_txt)
    count = 0
    lines = f.readlines()
    for line in lines:
        # line.rstrip('\n')
        mark_line = ''
        length = len(line)
        for i in range(length-1):
            if line[i] != ' ':
                num = count%len_txt
                mark_line=mark_line+txt[num]
                count += 1
            else:
                mark_line=mark_line+' '
        with open('replace.txt','a') as w:
            w.write(mark_line+'\n')