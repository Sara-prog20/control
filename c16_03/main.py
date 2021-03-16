note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
print(notes)

#def moyenne(x,y):
 # return (x[2]+y[2])/2



#eleve1=note1+note2
#print(moyenne(note1,note2))




[]
###c-Moyenne de l'eleve 1
def moyenne(liste):
  valeurs=0
  for i in range(len(liste)):
    valeurs=valeurs+liste[i][2]
    moyenne=valeurs/len(liste)
  return moyenne
notes_eleve1 = [note1, note2, note3, note4, note5, note6]
print("moyenne de eleve1",moyenne(notes_eleve1))

###b-moyenne de eleve1 en maths

notes_eleve1_math = [note1,note3, note6]
print("moyenne de eleve1 en math",moyenne(notes_eleve1_math))

## liste compréhension
def moyenne_comprehension(liste):
  liste=[]
  return [sum(liste[i][2])/len(liste) for liste[i] in liste]

print(moyenne_comprehension(notes_eleve1))

##c- Fonction qui calcule moyenne d'un élève dans une matière.

def moyenne_tuples(liste, eleve=liste[0], matière =liste[1]):
  return moyenne

print(moyenne_tuples(notes,eleve="eleve1"))