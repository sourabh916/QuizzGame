
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1

answer = input("If a computer has more than one processor then it is known as? ")
if answer.lower() == "Multiprocessor":
    print('Correct!')
    score += 1

    answer = input("  Which of the following are components of Central Processing Unit (CPU)?")
if answer.lower() == "Arithmetic logic unit(, Control unit":
    print('Correct!')
    score += 1

    answer = input("  Full form of URL is")
if answer.lower() == "Uniform Resource Locato":
    print('Correct!')
    score += 1

    answer = input("One kilobyte (KB) is equal to ")
if answer.lower() == "1,024 bytes":
    print('Correct!')
    score += 1

    answer = input("The rules of a language is known as ____ ")
if answer.lower() == " Syntax":
    print('Correct!')
    score += 1

    answer = input(" The lowest form of Computer language is called")
if answer.lower() == "Machine Language":
    print('Correct!')
    score += 1

    answer = input("UNIVAC is")
if answer.lower() == "Universal Automatic Computer":
    print('Correct!')
    score += 1

    answer = input("  The basic unit of a worksheet into which you enter data in Excel is called a ........")
if answer.lower() == "Cell":
    print('Correct!')
    score += 1

    answer = input("Information can be stored or retrieved from memory location through its ")
if answer.lower() == "Address":
    print('Correct!')
    score += 1

    answer = input("NOS stands for _______ ")
if answer.lower() == "Network Operating system":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")