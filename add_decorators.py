from decorators import check_permission


class User:
    def __init__(self, username, password):
        super(User, self).__init__()
        self.username = username
        self.password = password

    @check_permission
    def admin_login(self):
        print(f'Welcome {self.username}!')


if __name__ == '__main__':
    user1 = User(username='admin', password='admin')
    user2 = User(username='ishaq', password='ishaq')
    user3 = User(username='niloy', password='niloy')

    user1.admin_login()
    user2.admin_login()
    user3.admin_login()



