a=input("enter the file extension:")
match a:
    case'py':print('python file')
    case'c':print('c file')
    case 'c++':print('c++ file')
    case'html':print('HTML FILE')
    case'jpg':print('image file')
    case'_':print('unknown file type')
