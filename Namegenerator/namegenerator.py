from random import choice

fn = []
ln = []
random = ["1", "0"]
with open("firstname.txt", "r") as f:
    f = f.readlines()
    for name in f:
        fn.append(name.replace("\n", ""))

with open("lastname.txt", "r") as f:
    f = f.readlines()
    for name in f:
        ln.append(name.replace("\n", ""))

for i in range(0,100000):

    if(choice(random) == "1"):
        navn = choice(fn) + "-" + choice(fn) +" "+ choice(ln)
    else:
        navn = choice(fn)+" "+ choice(ln)

    with open("fullname.txt", "a") as f:
        f.write(navn + "\n")
    
