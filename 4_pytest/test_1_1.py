from collections import namedtuple
Task = namedtuple( 'Task' , [ 'summary' , 'owner' , 'done' , 'id' ])

# 1
# C:\> pip3 install -U virtualenv
# C:\> python3 -m virtualenv venv
# C:\> venv\Scripts\activate.bat
# (venv) C:\> pip install pytest
def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)



#