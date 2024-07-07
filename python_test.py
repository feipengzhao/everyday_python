def my_print(owner=None):
    def _print(*args, **kwargs):
        print(owner, *args, kwargs)

    return _print


personal_print = my_print(owner="Another: ")

personal_print("hello", name="Jack")
