# python_module_import_example

## main_with_global_import.py - fails

```
imported json in example_package, module json is <module 'json' from '/Users/boksh/.pyenv/versions/3.9.1/lib/python3.9/json/__init__.py'>

call try_use_json() in example_package. Module json is <module 'json' from '/Users/boksh/.pyenv/versions/3.9.1/lib/python3.9/json/__init__.py'>
trying to use json: {"example": "yes"}

call try_use_json() in example_package. Module json is <module 'example_package.json' from '/Users/boksh/Boksh-Development/python_module_import_example/example_package/json.py'>
Traceback (most recent call last):
  File "/Users/boksh/Boksh-Development/python_module_import_example/main_with_global_import.py", line 8, in <module>
    ap.try_use_json()
  File "/Users/boksh/Boksh-Development/python_module_import_example/example_package/__init__.py", line 8, in try_use_json
    print(f'trying to use json: {json.dumps({"example": "yes"})}')
AttributeError: module 'example_package.json' has no attribute 'dumps'
```


## main_with_another_module.py - works

```
imported json in example_package, module json is <module 'json' from '/Users/boksh/.pyenv/versions/3.9.1/lib/python3.9/json/__init__.py'>

imported json in example_package.another_module, module json is <module 'json' from '/Users/boksh/.pyenv/versions/3.9.1/lib/python3.9/json/__init__.py'>

call try_use_json() in example_package.another_module. Module json is <module 'json' from '/Users/boksh/.pyenv/versions/3.9.1/lib/python3.9/json/__init__.py'>
trying to use json: {"example": "yes"}

call try_use_json() in example_package.another_module. Module json is <module 'json' from '/Users/boksh/.pyenv/versions/3.9.1/lib/python3.9/json/__init__.py'>
trying to use json: {"example": "yes"}
```

## main_with_global_import.py - works

```
imported json in example_package_with_local_import
call try_use_json() in example_package_with_local_import. Module json is <module 'json' from '/Users/boksh/.pyenv/versions/3.9.1/lib/python3.9/json/__init__.py'>
trying to use json: {"example": "yes"}

call try_use_json() in example_package_with_local_import. Module json is <module 'json' from '/Users/boksh/.pyenv/versions/3.9.1/lib/python3.9/json/__init__.py'>
trying to use json: {"example": "yes"}
```
