from typing import List, Dict



def mock_data_append(mocks: List[Dict]):
    def outer(func):
        def inner(self):
            return func(self, mocks)
        return inner
    return outer


def get_mock_for_wrong_password()->List[Dict]:
    return [
        {"email":"aaa@aaa.com", "password1": "12312312356", "password2": "12312312356"}, # no upper and lower case
        {"email":"aaa@aaa.com", "password1": "ndddddddddddddd", "password2": "ndddddddddddddd"}, # no uppercase
        {"email":"aaa@aaa.com", "password1": "DDDDDDDDDDDDDDDDD", "password2": "DDDDDDDDDDDDDDDDD"}, # no lower case
        {"email":"aaa@aaa.com", "password1": "DDDDDaaa", "password2": "DDDDDaaa"}, # less than 10 chars
        {"email":"aaa@aaa.com", "password1": "asdssssssssSSSSSSS", "password2": "asdsssSSSSS"} # not equal passwords
    ]