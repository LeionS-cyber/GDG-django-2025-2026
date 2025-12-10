# Assuming the goal is to calculate the total sales and handle bad data
FILE_NAME = "sales.txt"

# Create a sample sales.txt file for demonstration
file_content = """200
450
abc
700
100.5
"""
try:
    with open(FILE_NAME, 'w') as f:
        f.write(file_content)
    print(f"Sample file '{FILE_NAME}' created.")
except IOError:
    print(f"Could not create sample file '{FILE_NAME}'.")


total_sales = 0
valid_sales_count = 0
invalid_lines = []

try:
    with open(FILE_NAME, 'r') as file:
        for line_number, line in enumerate(file, 1):
            # Clean up the line (remove leading/trailing whitespace and newline)
            sales_entry = line.strip()

            if not sales_entry:
                continue # Skip empty lines

            try:
                # Attempt to convert the entry to a number (float or int)
                sale_value = float(sales_entry)
                total_sales += sale_value
                valid_sales_count += 1
            except ValueError:
                # Catch the error if conversion fails (e.g., 'abc')
                invalid_lines.append(f"Line {line_number}: '{sales_entry}'")

    print(f"\n--- Sales Report ---")
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Number of valid sales entries processed: {valid_sales_count}")

    if invalid_lines:
        print("\nData Errors Found:")
        for error in invalid_lines:
            print(f"- {error} is not a valid number and was skipped.")
    else:
        print("No data errors found.")

except FileNotFoundError:
    print(f"Error: The file {FILE_NAME} was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
