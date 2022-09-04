import random,os,string
def main():
    lEN=int(input("Length for your password: "))
    gen_pass(lEN)
def gen_pass(lEN,strength=''):
    pwd=[]
    lisT=list(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation )
    for i in range(lEN):
        pwd.append(random.choice(lisT))
    random.shuffle(pwd)
    print(''.join(pwd))
    
if __name__=="__main__":
	main()
