text_dict = {"Flower" : 1, "is" : 2, "Ever" : 1, "Hits" : 2, "Back": 1}
print("The original dictionr: ", str(text_dict))
R = 2 
res = 0
for key in text_dict:
    if text_dict[key] == R:
        res = res + 1
print("Frequency of R is: "  + str(res))