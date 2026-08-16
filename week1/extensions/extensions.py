input_user = input("File name: ").strip()

extension = ''
check = False
for index,i in enumerate(input_user):
    if i == '.':
        extension = input_user[index+1:].lower()
        
match extension:
    case "jpeg" | "jpg":
        print("image/jpeg")
    case "png":
        print(f"image/{extension}")
    case "gif":
        print(f"image/{extension}")
    case "pdf":
        print(f"application/{extension}")
    case "zip":
        print(f"application/{extension}")
    case "txt":
        print(f"text/plain")
    case _:
        print("application/octet-stream")
