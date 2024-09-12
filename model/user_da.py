import mysql.connector

from model.user import User


class UserDa:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="mft"
        )
        self.cursor= self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self,user):
        self.connect()
        self.cursor.execute("INSERT INTO user_tbl (username,password,name,family,is_active) VALUES (%s,%s,%s,%s,%s)",
                            [user.username, user.password, user.name, user.family, user.active])
        self.disconnect(True)

    def edit(self,user):
        self.connect()
        self.cursor.execute("UPDATE user_tbl SET password=%s,name=%s,family=%s,is_active=%s WHERE username=%s",
                            [user.password, user.name, user.family, user.active, user.username])
        self.disconnect(True)

    def remove(self,username):
        self.connect()
        self.cursor.execute("DELETE FROM user_tbl WHERE username=%s",[username])
        self.disconnect(True)

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM user_tbl")
        users_tuple = self.cursor.fetchall()
        if users_tuple:
            user_list = []
            for user in users_tuple:
                user_list.append(User(*user))
            self.disconnect()
            return user_list

    def find_all_active(self):
        self.connect()
        self.cursor.execute("SELECT * FROM user_tbl WHERE is_active=1")
        users_tuple = self.cursor.fetchall()
        if users_tuple:
            user_list = []
            for user in users_tuple:
                user_list.append(User(*user))
            self.disconnect()
            return user_list

    def find_by_username(self,username):
        self.connect()
        self.cursor.execute("SELECT * FROM user_tbl WHERE username=%s",[username])
        user_tuple = self.cursor.fetchone()
        if user_tuple:
            user = User(*user_tuple)
            self.disconnect()
            return user

    def find_by_username_and_password(self,username, password):
        self.connect()
        self.cursor.execute("SELECT * FROM user_tbl WHERE username=%s and password=%s",
                            [username, password])
        user_tuple = self.cursor.fetchone()
        if user_tuple:
            user = User(*user_tuple)
            self.disconnect()
            return user

    def enable_user(self, username):
        self.connect()
        self.cursor.execute("UPDATE user_tbl SET is_active=1 WHERE username=%s",
                            [username])
        self.disconnect(True)

    def disable_user(self,username):
        self.connect()
        self.cursor.execute("UPDATE user_tbl SET is_active=0 WHERE username=%s",
                            [username])
        self.disconnect(True)
