# main code
def main_code():
    while True:
        User_name = input("Enter your name please: ").strip()
        Language = input("What is your favorite programming language: ").strip()
        Saved_data = {'Names': User_name,
                      'Programming language': Language}
        if User_name == '' or Language == '':
            print("Both fields must be completed.")
        else:
            print(f"Hello {Saved_data['Names']} welcome to Arcion Systems! It's great to see another {Saved_data['Programming language']} developer here!")
            break

if __name__ == "__main__":
    main_code()