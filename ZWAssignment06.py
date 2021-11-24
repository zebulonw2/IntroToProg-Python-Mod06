# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each 'row' of data
#              in 'ToDoToDoList.txt' into a python Dictionary.
#              Add the each dictionary 'row' to a python list 'table'
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# Zeb W., 22Nov2021,Modified code to complete assignment 6
# Zeb W., 23Nov2021, Added error handling
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = 'ToDoList.txt'  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ''  # Captures the user option selection
strTask = ''  # Captures the user task data
strPriority = ''  # Captures the user priority data
strStatus = ''  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        ''' Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        '''
        list_of_rows.clear()  # clear current data
        file = open(file_name, 'r')
        for line in file:
            task, priority = line.split(',')
            row = {'Task': task.strip(), 'Priority': priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success!'
    print()

    @staticmethod
    def add_data_to_list(list_of_rows, task_to_add, priority):
        '''Add new row to list

        :param list_of_rows: (list) of dictionary rows
        :param task_to_add: (string) task name
        :param priority: (string) task priority
        '''
        row = {'Task': str(task_to_add).strip(), 'Priority': str(priority).strip()}
        list_of_rows.append(row)
        return list_of_rows, 'Success! \n'

    @staticmethod
    def remove_data_from_list(list_of_rows, task_to_remove, row_removed=None, status=''):
        '''Remove row from list

        :param list_of_rows: (list) of dictionary rows
        :param task_to_remove: (string) task to remove
        :param row_removed: (boolean) determine if row was removed
        :param status: (string) status of task removal
        '''
        for row in list_of_rows:
            if row["Task"].lower() == task_to_remove.lower():
                lstTable.remove(row)
                row_removed = True
            if row_removed == True:
                status = 'Success!\n'
            else:
                status = 'Task not found in list\nIf you want to remove and item, select "2" from the menu,\nAnd enter the task name\n'
        return list_of_rows, status
    print()

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        '''write new list into .txt file

        :param file_name: (string) name of text file
        :param list_of_rows: (list) rows of dictionary items to write into file
        '''
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        return list_of_rows, 'Success!'
    print()

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    ''' Performs Input and Output tasks '''

    @staticmethod
    def print_menu_Tasks():
        '''  Display a menu of choices to the user

        :return: nothing
        '''
        print()
        print('Menu of Options')
        print('1) Add a new Task')
        print('2) Remove an existing Task')
        print('3) Save Data to File')
        print('4) Reload Data from File')
        print('5) Exit Program')
        print()

    @staticmethod
    def input_menu_choice():
        ''' Gets the menu choice from a user

        :return: string
        '''
        choice = str(input('Which option would you like to perform? [1 to 5]: ')).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        ''' Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        '''
        print()
        print('======= The current Tasks ToDo are: =======')
        for row in list_of_rows:
            print(row['Task'] + ' (' + row['Priority'] + ')')
        print('============================================')

    @staticmethod
    def input_yes_no_choice(message):
        ''' Gets a yes or no choice from the user

        :return: string
        '''
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        ''' Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        '''
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        task_to_add = str(input("What is the task?: ")).strip()
        priority = str(input("What is the priority?: ")).strip()
        print()
        return task_to_add, priority

    @staticmethod
    def input_task_to_remove():
        task = str(input("Which task would you like to remove?: ")).strip()
        print()
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data


# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # if 1) Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority() # gets task name and priority from user
        lstTable, strStatus = Processor.add_data_to_list(lstTable, strTask, strPriority) # adds user input to list
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strTask = IO.input_task_to_remove() # gets name of task to remove from user
        lstTable, strStatus = Processor.remove_data_from_list(lstTable, strTask)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice('Save this data to file? (y/n): ')
        if strChoice.lower() == 'y':
            print()
            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus + '\n')
        elif strChoice.lower() == 'n':
            print()
            IO.input_press_to_continue('Save Cancelled!\n')
        else:
            print()
            print('That is not a choice!')
            print('If you want to save, select "3" from the menu,')
            print('And enter either "y" or "n"')
            IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print('Warning: Unsaved Data Will Be Lost!')
        print()
        strChoice = IO.input_yes_no_choice('Are you sure you want to reload data from file? (y/n): ')
        if strChoice.lower() == 'y':
            print()
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus + '\n')
        elif strChoice.lower() == 'n':
            print()
            IO.input_press_to_continue('File Reload Cancelled! \n')
        else:
            print()
            print('That is not a choice!')
            print('If you want to reload the file, select "4" from the menu,')
            print('And enter either "y" or "n"')
            IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        strChoice = IO.input_yes_no_choice('Are you sure you want to exit? (y/n): ')
        if strChoice.lower() == 'y':
            print()
            print('Goodbye!')
            break  # and Exit
        elif strChoice.lower() == 'n':
            print()
            IO.input_press_to_continue('Exit Cancelled! \n')
        else:
            print()
            print('That is not a choice!')
            print('If you want to exit the program, select "5" from the menu,')
            print('And enter either "y" or "n"')
            IO.input_press_to_continue()
        continue

    else:
        print('That is not a choice!')