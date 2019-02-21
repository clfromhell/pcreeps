from dbinterface import DBI as db
import hashlib


class User:
    def __init__(self):
        self._uid = ""
        self._nick = ""
        self._pwh = ""
        self._h = hashlib.sha256()

    def new_user(self, nick, pw):
        if not db.check_nick_avail(nick):
            self._nick = nick
            self._h.update(pw)
            self._pwh = self._h.hexdigest()

            db.create_user(self._nick, self._pwh)

            return db.get_user_id(self._nick)

        else:

            return 0

    def logon(self, nick, pw):
        if db.check_nick_avail(nick):
            self._nick = nick
            self._h.update(pw)
            self._pwh = self._h.hexdigest()

            if db.check_logon_info(self._nick, self._pwh):
                return True
            else:
                return False
