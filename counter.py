def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    d=dict()
    for line in handle:
        line=line.rstrip()
        words=line.split()
        if line.startswith('From'):
            if line.startswith('From:'):
                continue
            else:
                sender = words[1]
                if sender not in d:
                    d[sender] = 1
                else:
                    d[sender] += 1
    BigSender = None
    BigCount = 0
    for key in d:
        if d[key] >= BigCount:
            BigCount = d[key]
            BigSender = key
    print(BigSender, BigCount)
    
    




        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
