from warnings import warn
from typing import Union, List, Tuple


code = []

taskIds = []


taskId = 0
def _task_name():
    global taskId
    taskId += 1
    return taskId


class Task:
    def __init__(self, name: str, start, end, type: Union[int,List[int],Tuple[int,...]] = None,customId: str = None):
        self.name = name
        self.start = start
        self.end = end
        self.type = type

        if customId in taskIds:
            warn(...)
            exit()

        self.customId = customId
        taskIds.append(customId)
    def _add(self):
        types = ["done","active","crit","milestone"]
        if type(self.type) in [list,tuple]:
            for ind,obj in self.type:
                self.type[ind] = types[obj]
        else:
            self.type = types[self.type]
        if type(self.type) in [list,tuple]:
            self.type = ", ".join(self.type)



        code.append(f"{self.name} :")
class Group:
    def __init__(self, name: str):
        self._id = name
        self._canBeCalled = False
        self._times = 0

    def __enter__(self):
        self._canBeCalled = True
        code.append(f"subgraph {self._id}")

        return self

    def __exit__(self, *_):
        self._canBeCalled = False
        # if it's empty

        code.append("end")
        if self._times == 0:
            warn("User added empty group or forget to use Group().add()", Warning, 3)
            while code[-1][0:8] != "subgraph":
                code.pop(-1)
            code.pop(-1)

    def add(self, arg):
        self._times += 1
        if not self._canBeCalled:
            warn("Links or nodes can be added only inside the group", Warning, 2)
            exit()
        if self._id in code[-1]:
            warn("Unable to link group to itself", Warning, 2)
            exit()
