def check_permission(func):
    def wrapper(self):
        if self.username == 'admin':
            func(self)
        else:
            print('Only admin can log in')

    return wrapper

