from typing import List, Dict



def mock_data_append(mocks: List[Dict]):
    def outer(func):
        def inner(self):
            return func(self, mocks)
        return inner
    return outer


def get_mock_for_wrong_title_and_body()->List[Dict]:
    return [
        {"title":"abcs"*2500, "body": "body"}, # too long title
        {"title":"title", "body": "body"*100000} # too long body
    ]