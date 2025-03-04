
p = int(input("Enter the Prime number: "))
root = int(input("Enter the Primitive root: "))
Alice = int(input("Enter Alice's private key: "))
Bob = int(input("Enter Bob's private key: "))

PAlice = pow(root, Alice, p)
print("Alice's public value" ,PAlice)
PBob = pow(root, Bob, p)
print("Bob's public value", PBob)

SkeyA = pow(PBob, Alice, p)
print("Alice's computed shared key",SkeyA)
SkeyB = pow(PAlice, Bob, p)
print("Bob computed Shared key ",SkeyB)

if SkeyA == SkeyB:
    print("The shared secret keys match. The key exchange was successful!")
else:
    print("The shared secret keys do not match. Something went wrong.")
