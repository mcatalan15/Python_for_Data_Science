def NULL_not_found(object: any) -> int:
    match object:
        case bool() if object is False:
            print(f"Fake: False {type(object)}")
        case int() if object == 0:
            print(f"Zero: 0 {type(object)}")
        case float() if object != object:
            print(f"Garlic: nan {type(object)}")
        case str() if object == "":
            print(f"Empty: {type(object)}")    
        case None:
            print(f"Nothing: {object} {type(object)}")
        case _:
            print("Type not Found")
    return (1)