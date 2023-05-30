from typing import List, Dict



def mock_data_append(mocks: List[Dict]):
    def outer(func):
        def inner(self):
            return func(self, mocks)
        return inner
    return outer
