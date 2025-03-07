document = open('CS2\\student_data_cs2.txt', 'r')       #open the student data document
csv_file = open('CS2\\student_data_new_file.csv', 'w')  #open the csv file
#for each line in the document, write each part of the document into the new csv file 
for line in document:
    #write the ID into the csv
    csv_file.write(line[0:6].strip() + ', ')
    #write the first name into the csv
    csv_file.write(line[6:21].strip()+', ')
    #write the last name into the csv
    csv_file.write(line[21:36].strip()+', ')
    #write the grade into the csv
    csv_file.write(line[36:42].strip()+', ')
    #write the gpa into the csv
    csv_file.write(line[42:48].strip()+', ')
    #write the birthdate into the csv
    csv_file.write(line[48:60].strip()+', ')
    #write the gender into the csv
    csv_file.write(line[60:67].strip()+', ')
    #write the class rank into the csv
    csv_file.write(line[67:76].strip()+', ')
    #write the attendpct into the csv
    csv_file.write(line[76:86].strip()+', ')
    #write the honors into the csv
    csv_file.write(line[86:93].strip()+', ')
    #write the sports into the csv
    csv_file.write(line[93:102].strip()+', ')
    #write the club count into the csv
    csv_file.write(line[102:112].strip())
    #new line
    csv_file.write('\n')