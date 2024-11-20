# try:
#     num = int(input("Enter a numbere:\n"))
#     result = 10 / num
#
# except ZeroDivisionError:
#     print("Error: Division by Zero is not allowed.")
#
# except ValueError:
#     print("Error: Type the corrected value")
#
# except Exception as e:
#     print(f"Error: {str(e)}")
#
# else:
#     print("Result: ", result)
#
# finally:
#     print("Execution finished")
#
# try:
#     with open('example.txt','r') as file:
#         data = file.read()
# # except FileNotFoundError:
# except Exception as e:
#     print(f'Error: {e}')
#     # print("Error: File not found")
# else:
#     print(data)
# finally:
#     print("File operation completed")