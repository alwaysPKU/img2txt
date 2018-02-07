with open('shaonianpai') as f:
    lines = f.readlines()
    for line in lines:
        new_line = line.replace(' ', '/')
        with open('shaonianpai2','a') as w:
            w.write(new_line)