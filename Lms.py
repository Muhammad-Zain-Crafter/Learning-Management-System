# LEARNING MANAGEMENT SYSTEM (LMS):
# Course Management: The LMS should allow adding, updating, and deleting courses.
# Student Management: Add, update, and delete student profiles.
# Enrollment System: Enroll students in courses and allow listing all students in a specific course.

from numpy import array

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):  
        temp = arr[i]
        ptr = i - 1
        while ptr >= 0 and temp < arr[ptr]:  
            arr[ptr + 1] = arr[ptr]
            ptr -= 1
        arr[ptr + 1] = temp  
def binary_search(arr, target):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return "found at index ",mid+1
        elif target > arr[mid]:
            start = mid + 1 
        elif target < arr[mid]:
            end = mid - 1
    return "not found"
def Add_Entity(arr, entity):
    n = len(arr)
    new_arr = [0] * (n + 1)
    for i in range(n): 
        new_arr[i] = arr[i] 
    new_arr[n] = entity 
    return new_arr
def Update_Entity(arr, index, new_id):
    if 0 <= index < len(arr):
        arr[index] = new_id
        print("Updated successfully!")
    else:
        print("Invalid index...")
    return arr
def Delete_Entity(arr, index):
    n = len(arr)
    if 1 <= index <= n:  
        arr_list = list(arr)
        del arr_list[index - 1]
        return array(arr_list) 
    else:
        print("Invalid index...")
        return arr

def add_student_in_specific_course(enrollments, course, student_id):
    if 0 <= course < len(enrollments):
        enrollments[course].append(student_id)
    else:
        print("Invalid course index...")
def delete_student_from_specific_course(enrollments, course, student_id):
    if 0 <= course < len(enrollments):
        if student_id in enrollments[course]:
            enrollments[course].remove(student_id)
        else:
            print("Student not found in course...")
    else:
        print("Invalid course index...")

def List_Students(enrollments, course_index):
    if 0 <= course_index < len(enrollments):
        print(f"Students in course {course_index + 1}: {enrollments[course_index]}")
    else:
        print("Invalid course index...")

course_codes = array([116187, 116191, 116185, 115190, 114320])
courses = array(['PF', 'OOP', 'MVC', 'DSA', 'AI'])
std_ids = array([15865, 15849, 15972, 15841, 15690, 15674, 19150, 15925, 15430, 15980])
course_enrollments = [
    [15865, 15972, 15841, 15430, 15849],
    [15690, 15649, 15674, 15865, 15925],
    [15925, 15430, 15980, 15430, 15972],
    [15690, 15865, 19150, 15841, 15980],
    [15849, 15690, 19150, 15925, 15865]
]
print("\n<------------------------- LEARNING MANAGEMENT SYSTEM ------------------------->")
print("\nCourse_codes: ",course_codes)
print("courses name: ",courses)
print("Student Id's: ",std_ids)
print("Students in specific courses: ",course_enrollments)
while True:
    print("1--> Sort Data")
    print("2--> Search")
    print("3--> Add Entity")
    print("4--> Update Entity")
    print("5--> Delete Entity")
    print("6--> Manage Course Enrollments")
    print("7--> List Students in a Course")
    print("8--> Exit")
    
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        print("\nSorting Options:")
        print("1. Sort Course Codes")
        print("2. Sort Student IDs")
        print("3. Sort Courses Alphabetically")
        print("4. Sort Enrollments in Each Course")
        sort_choice = int(input("\nEnter your choice: "))
        
        if sort_choice == 1:
            bubble_sort(course_codes)
            print("Sorted Course Codes:", course_codes)
        elif sort_choice == 2:
            bubble_sort(std_ids)
            print("Sorted Student IDs:", std_ids)
        elif sort_choice == 3:
            insertion_sort(courses)
            print("Courses Sorted Alphabetically:", courses)
        elif sort_choice == 4:
            for enrollment in course_enrollments:
                selection_sort(enrollment)
            print("Enrollments Sorted in Each Course:", course_enrollments)
        else:
            print("Invalid choice...")
    
    elif choice == 2:
        print("\nSearch Options:")
        print("1. Search Course")
        print("2. Search Student")
        search_choice = int(input("\nEnter your choice: "))
        
        if search_choice == 1:
            course_id = int(input("Enter course_code you want to search: "))
            print(binary_search(course_codes, course_id))
        elif search_choice == 2:
            student_id = int(input("Enter student-Id you want to search: "))
            print(binary_search(std_ids, student_id))
        else:
            print("Invalid choice...")
    
    elif choice == 3:
        print("\nAdd Options:")
        print("1. Add Course Code")
        print("2. Add Course Name")
        print("3. Add Student ID")
        add_choice = int(input("\nEnter your choice: "))
        
        if add_choice == 1:
            new_code = int(input("Enter course code to add: "))
            course_codes = array(Add_Entity(course_codes, new_code))
            print("Updated Course Codes:", course_codes)
        elif add_choice == 2:
            new_name = input("Enter course name to add: ")
            courses = array(Add_Entity(courses, new_name))
            print("Updated Course Names:", courses)
        elif add_choice == 3:
            new_id = int(input("Enter student ID to add: "))
            std_ids = array(Add_Entity(std_ids, new_id))
            print("Updated Student IDs:", std_ids)
        else:
            print("Invalid choice...")
    
    elif choice == 4:
        print("\nUpdate Options:")
        print("1. Update Course Code")
        print("2. Update Student ID")
        update_choice = int(input("\nEnter your choice: "))
        
        if update_choice == 1:
            index = int(input("Enter index to update: ")) - 1
            new_code = int(input("Enter new course code: "))
            course_codes = Update_Entity(course_codes, index, new_code)
            print("Updated Course Codes:", course_codes)
        elif update_choice == 2:
            index = int(input("Enter index to update: ")) - 1
            new_id = int(input("Enter new student ID: "))
            std_ids = Update_Entity(std_ids, index, new_id)
            print("Updated Student IDs:", std_ids)
        else:
            print("Invalid choice...")
    
    elif choice == 5:
        print("\nDelete Options:")
        print("1. Delete Course Code")
        print("2. Delete Student ID")
        delete_choice = int(input("\nEnter your choice: "))
        if delete_choice == 1:
            id = int(input("Enter index of course_code you want to delete: "))
            cid = Delete_Entity(course_codes, id)
            print("Course IDs after deletion:", *cid)
        elif delete_choice == 2:
           id = int(input("Enter index of std_id you want to delete: "))
           sid = Delete_Entity(std_ids, id)
           print("Student IDs after deletion:", *sid)
        else:
            print("Invalid choice...")
    
    elif choice == 6:
        print("\nEnrollment Management:")
        print("1. Add Student to a Course")
        print("2. Remove Student from a Course")
        enrollment_choice = int(input("\nEnter your choice: "))
        
        if enrollment_choice == 1:
            course_index = int(input("Enter course index: "))
            student_id = int(input("Enter student ID to add: "))
            add_student_in_specific_course(course_enrollments, course_index, student_id)
            print(f"Updated Enrollments for Course {course_index + 1}:", course_enrollments[course_index])
        elif enrollment_choice == 2:
            course_index = int(input("Enter course index: "))
            student_id = int(input("Enter student ID to remove: "))
            delete_student_from_specific_course(course_enrollments, course_index, student_id)
            print(f"Updated Enrollments for Course {course_index + 1}:", course_enrollments[course_index])
        else:
            print("Invalid choice...")
    
    elif choice == 7:
        course_index = int(input("Enter course index: "))
        List_Students(course_enrollments, course_index)
    
    elif choice == 8:
        print("Exiting LMS.......")
        break
    else:
        print("Invalid choice.")




