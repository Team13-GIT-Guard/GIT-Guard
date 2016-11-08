import contribution
import onecontributor
import compare
import commithistory
import lines
import subscribe
import unsubscribe
import time
import datetime

def visualization():
    while(True):
        print("\n\t----------Please specify the visualization----------")
        command = raw_input("\t\tType 'a' for viewing contribution of all members;\n\t\tType 'b' for viewing commit history of a user;\n\t\tType 'c' for viewing commit history comparison;\n\t\tType 'd' for viewing commit history of a file;\n\t\tType 'e' for viewing number of lines of code;\n\t\tType others to go back to the main menu;\n\t\t\tSpecify your command: ")
        if command == "a":
            print("\n\t----------Task A----------")
            contribution.main()
        elif command == "b":
            print("\n\t----------Task B----------")
            onecontributor.main()
        elif command == "c":
            print("\n\t----------Task C----------")
            compare.main()
        elif command == "d":
            print("\n\t----------Task D----------")
            commithistory.main()
        elif command == "e":
            print("\n\t----------Task E----------")
            lines.main()
        else:
            print
            break;

def subscription():
    while(True):
        print("\n\t----------Please specify the subscription----------")
        command = raw_input("\t\tType 's' for subscribing notification service;\n\t\tType 'u' for unsubscribing notification service;\n\t\tType others to go back to the main menu;\n\t\t\tSpecify your command: ")
        if command == "s":
            print("\n\t----------Subscribe----------")
            subscribe.main()
        elif command == "u":
            print("\n\t----------Unsubscribe----------")
            unsubscribe.main()
        else:
            print
            break;

def interface():
    time_file = open("timerecord.txt","w")
    print("--------------------Welcome to GIT-Guard--------------------")
    print("-------------------- You have logged in --------------------")
    start_time = datetime.datetime.now()
    print("-------------------- " + str(start_time).split('.')[0] + " --------------------")
    time_file.write(str(start_time).split('.')[0])
    time_file.close()
    print
    print
    while(True):
        print("--------------------Please Specify your task--------------------")
        command = raw_input("\tType '1' for viewing visualizations of a GIT repositary;\n\tType '2' for subscribing notification service;\n\tType others to exit;\n\t\tSpecify your task: ")
        if command == "1":
            print("\n--------------------Visualization--------------------")
            visualization()
        elif command == "2":
            print("\n--------------------Subscribe--------------------")
            subscription()
        else:
            print("\n--------------------Exit--------------------")
            break;
    return
    
interface()
