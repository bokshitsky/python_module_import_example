import json

print(f"imported json in {__name__}, module json is {json}\r\n")


def try_use_json():
    print(f"call try_use_json() in {__name__}. Module json is {json}")
    print(f'trying to use json: {json.dumps({"example": "yes"})}')
    print("")
