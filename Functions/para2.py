def checktext():
    para = soup.body.findAll(text=re.compile('The purpose'))
    para2 = soup.body.findAll(text=re.compile('Click on the tabs'))
    paracombine = para + para2
    list(para)
    print(para)
    if "The purpose" in para or paracombine:
        print("True1")
        return True
        if "Click on" in para or para2:
            print("True2")
            return True
        else:
            print("False")
            return False
    else:
        print("False else")
        return False