import random

FN = input("Output File Name: ")
NP = int(input("Number of Packets: "))
#RD = input("Random Packets? {Y] [N}: ")
PS = int(input("Packet Size: "))
DT = int(input("Delta Time (ms): "))
i = DT
# print(NP, PS, DT)

file = open(FN + ".scd", "w")

#if RD == "Y":
while NP > 0:
    file.write(str(DT) + " " + str(PS))
    j = PS
    while j > 0:
        A = "%02x" % random.randint(0, 0xFF)
        file.write(" " + A)
        j -= 1
    file.write("\n")
    DT = DT + i
    NP -= 1

'''
else:
    j = PS
    while j > 0:
        A = ["%02x" % random.randint(0, 0xFF)]
        B.append[A]
        j -= 1

    while NP > 0:
        file.write(str(DT) + " " + str(PS) + " " + B)
        file.write("\n")
        DT = DT + i
        NP -= 1
    # print(NP)
    # print(DT)
'''
