mail= input("enter a mail : ")    # g@g.com  min  len = 6

k, d, j = 0 ,0 ,0 

if (len(mail) >= 6 ) and (mail[0].isalpha() ) :

    if ("@" in mail) and (mail.count("@") == 1 ):

        if (mail[-4]==".") ^ (mail[-3]==".") :

            for i in mail :
                if i.isspace():
                    k = 1
                elif i.isalpha():
                    if i == i.upper():
                        d =1 
                elif i== "@" or i =="." or i.isdigit() :
                    continue
                else :
                    j = 1 

            if k==1 or d ==1 or j ==1 :
                print("invalid character used ..!!")
            else :
                print("correct mail . ")                

        else:
            print("syntex error .")
    else:
        print("you are not allowded to enter '@' more than one time")
else :
    print("plz fill corectly . length is not enough and make sure that your first latter should not be capital")