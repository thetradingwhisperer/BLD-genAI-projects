from pydantic import BaseModel, ValidationError, EmailStr

class UserRegistration(BaseModel):
    name: str
    age: int
    email: EmailStr

def main():
    print('Welcom to User registration')
    user_data = {
        "name": input("Enter your name: "),
        "age": input("Enter your age: "),
        "email": input("Enter your email: ")
    }

    try:
        user = UserRegistration(**user_data)
        print("User registered successfully:", user)
    except ValidationError as e:  
        print("Error: ", e.json())

if __name__ == '__main__':
    main()