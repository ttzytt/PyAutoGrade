




Romeo = int(input("Romeo's initial attraction: "))
Juliet = int(input("Juliet's initial attraction: "))
Romantic_value = (Romeo, Juliet) 
Romantic_value_altered = (Romeo, Juliet)
time = int(input('How many days should this run? ')) 
list_of_values = [(Romeo, Juliet)] 
list_of_values_altered = [(Romeo, Juliet)] 



def Romeo_Juliet_model(Romantic_value):
    Romeo = Romantic_value[0]
    Juliet = Romantic_value[1]
    Romeo_new = Romeo + 0.4 * Juliet
    Juliet_new = Juliet - 0.2 * Romeo
    Romantic_value = (Romeo_new, Juliet_new)
    return Romantic_value




def Romeo_Juliet_model_altered(Romantic_value_altered):
    Romeo = Romantic_value_altered[0]
    Juliet = Romantic_value_altered[1]
    Romeo_new = Romeo * 0.9 + 0.4 * Juliet
    Juliet_new = Juliet - 0.2 * Romeo
    Romantic_value = (Romeo_new, Juliet_new)
    return Romantic_value


for i in range (time):
    list_of_values.append(Romeo_Juliet_model(Romantic_value))
    list_of_values_altered.append(Romeo_Juliet_model_altered(Romantic_value))
    Romantic_value = Romeo_Juliet_model(Romantic_value)
    Romantic_value_altered = Romeo_Juliet_model_altered(Romantic_value_altered)


print (list_of_values)
print (list_of_values_altered)
