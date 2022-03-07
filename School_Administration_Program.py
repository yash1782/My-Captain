#Project 1: Basic School administration tool 
import csv

def write_into_csv(info_list):
    with open("student_info.csv","a",newline="") as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Number","Email"])
        writer.writerow(info_list)    
            
if __name__ == "__main__":
    condition = True

    student_num=1
    
    while(condition):
        student_info = input("Enter student information for student #{} in following format(name age number email):".format(student_num))
        print(student_info)
        
        student_split_info=student_info.split(" ")
        print("Enterd Split information is : ",str(student_split_info))
        
        print("\nThe Entered information is -\nName: {}\nAge: {}\nContact_Number: {}\nEmail_ID: {}".format(student_split_info[0],student_split_info[1],student_split_info[2],student_split_info[3]))
        
        Choice_Check=input("Is the enterd information is correct? (yes/no): ")
        if Choice_Check == "yes":
            write_into_csv(student_split_info)
            
            condition_check = input("Enter (yes/no) if you want to enter more information for another student: ")
            
            if condition_check=="yes":
                condition=True
                student_num = student_num + 1
            elif condition_check=="no":
                condition=False
        elif Choice_Check=="no":
            print("\nPlease ReEnter The Values!")