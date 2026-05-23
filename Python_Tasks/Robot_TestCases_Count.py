import os
import pandas as pd
from robot.api import TestSuiteBuilder

def count_test_cases_in_robot(file_path):
    try:
        suite = TestSuiteBuilder().build(file_path)
        return len(suite.tests)  # Count number of test cases
    except:
        return 0  # If the file is not a valid Robot file, return 0

def scan_robot_files(directory):
    data = []
    total_test_count = 0
    folder_test_counts = {}
    
    for root, dirs, files in os.walk(directory):
        parent_folder = os.path.basename(root)
        test_count = 0
        
        for file in files:
            if file.endswith(".robot"):
                file_path = os.path.join(root, file)
                test_count += count_test_cases_in_robot(file_path)
        
        if parent_folder in folder_test_counts:
            folder_test_counts[parent_folder] += test_count
        else:
            folder_test_counts[parent_folder] = test_count
    
    for folder, count in folder_test_counts.items():
        data.append([folder, count])
        total_test_count += count
    
    data.append(["Total", total_test_count])  # Add total test count
    return data

def save_to_excel(data, output_file):
    df = pd.DataFrame(data, columns=["Folder Name", "Test Case Count"])
    output_path = os.path.join(folder_path, output_file)  # Save in the same directory
    df.to_excel(output_path, index=False)
    print(f"Results saved to {output_path}")

# Specify the folder path
folder_path = r"C:\\Users\\MaheshVanaparthi\\Downloads\\robot_scripts"
output_file = "robot_test_cases.xlsx"

data = scan_robot_files(folder_path)
save_to_excel(data, output_file)
