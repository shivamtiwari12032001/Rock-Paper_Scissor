import random
def play():
    user=input("enter your choice?? 'r' for rock 's' for scissor or 'p' for paper:\n ")
    computer=random.choice(["r","s","p"])
    if user==computer:
        return "It\"s tie"
    if is_win(user,computer):
        return  "You won"
    return "you lost"


def is_win(user,opponent):
    if(user=="r" and opponent=="s")or (user=="p" and opponent=="r") or (user=="s" and opponent=="p"):
        return True
print(play())