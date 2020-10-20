hi
print("Title of program: Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("good let it be anger instead")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("lets not keep it that way")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("life is just like this,so what")
      counter += 1
    if each_word=="fear":
      feelings_list.append("fear")
      encouragement_list.append("don't be afraid, just keep on going")
      counter += 1
    if each_word=="disgust":
      feelings_list.append("disgust")
      encouragement_list.append("don't be disgusted, keep calm")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
