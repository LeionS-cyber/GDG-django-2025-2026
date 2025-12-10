FILE_NAME = "log.txt"
LOG_MESSAGE = "User logged in"

# 1. Write the log message to the file (appends if file exists, creates if not)
try:
    with open(FILE_NAME, 'a') as file:
        file.write(LOG_MESSAGE + "\n")
    print(f"'{LOG_MESSAGE}' written to {FILE_NAME}")

    # 2. Read the full log history from the file
    print("\n--- Full Log History ---")
    with open(FILE_NAME, 'r') as file:
        log_history = file.read()
        print(log_history.strip()) # .strip() removes trailing whitespace/newline

except IOError as e:
    print(f"An error occurred while handling the file: {e}")
