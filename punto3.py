subjects = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje","filsofia","etica","ingles","naturales"]
scores = []
for subject in subjects:#pregunta las notas y las almacena
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):#imprime las notas con su respectiva materia
    print("En " + subjects[i] + " has sacado " + scores[i])