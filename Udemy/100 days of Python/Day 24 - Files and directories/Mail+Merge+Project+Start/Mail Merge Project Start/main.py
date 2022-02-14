#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/home/jeremy/repos/Udemy/100 days of Python/Day 24 - Files and directories/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as letter:
    contents = letter.readlines()
    name_ex = contents[0]

with open("/home/jeremy/repos/Udemy/100 days of Python/Day 24 - Files and directories/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names:
    invited_guests = names.readlines()

for name in invited_guests:
    new_name = name.strip()
    with open(f"/home/jeremy/repos/Udemy/100 days of Python/Day 24 - Files and directories/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as n:
        for line in contents:
            replaced_name = line.replace("[name]",f"{new_name}")
            n.write(f"{replaced_name}")


