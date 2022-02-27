import random

print("Password Generator")
redo = False
lower_chars = "abcdefghijklmnopqrstuvwxyz"
spec_chars = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = int(input("Desired password length: "))
spec_count = random.randint(1, length)
upper_count = random.randint(1, length-spec_count)


if spec_count == length:
  spec_count = spec_count - 1
  
while length < 12 or length > 24:
  print("\nCharacter limit: 12-24. Please choose another length.")
  length = input("Desired password length: ")
  length = int(length)
  redo = True

def func():
  lower_chars_pass = ''
  upper_chars_pass = ''
  spec_pass = ''
  
  for pwd1 in range(0, spec_count):
    spec_pass += random.choice(spec_chars)

  for pwd2 in range(0, upper_count):
    upper_chars_pass += random.choice(upper_chars)
  
  for pwd3 in range(length-(spec_count + upper_count)):
    lower_chars_pass += random.choice(lower_chars)

    
  shuff_pass = ((str(lower_chars_pass)) + (str(upper_chars_pass)) + (str(spec_pass))) 
  
  l = list(shuff_pass)
  random.shuffle(l)
  result = ''.join(l) 
  print(result)

func()

print("spec_count")
print(spec_count)
print('')
print("upper_count")
print(upper_count)
print('')