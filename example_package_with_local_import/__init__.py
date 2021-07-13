print(f"imported json in {__name__}")


def try_use_json():
    import json
    print(f"call try_use_json() in {__name__}. Module json is {json}")
    print(f'trying to use json: {json.dumps({"example": "yes"})}')
    print("")
