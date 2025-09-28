#!/usr/bin/env python3
"""
COMP3104 Group 3 Assignment - Hello World Example
Author: Group 3 Members
Description: Simple Python script demonstrating collaborative development
"""

def main():
    """Main function that demonstrates basic functionality"""
    print("Hello from COMP3104 Group 3!")
    print("This is our collaborative assignment.")
    
    # Group member contributions can be added here
    print("\nGroup Members:")
    print("- Student 1: [Name to be added]")
    print("- Student 2: [Name to be added]")
    print("- Student 3: [Name to be added]")
    print("- Student 4: [Name to be added]")

def get_group_info():
    """Returns group information as a dictionary"""
    return {
        "course": "COMP3104",
        "group_number": 3,
        "assignment": "Group Assignment",
        "institution": "George Brown College"
    }

if __name__ == "__main__":
    main()
    info = get_group_info()
    print(f"\nCourse: {info['course']}")
    print(f"Group: {info['group_number']}")