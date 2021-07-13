if __name__ == '__main__':
    import example_package_with_local_import as ep

    ep.try_use_json()
    import example_package_with_local_import.json

    ep.try_use_json()
