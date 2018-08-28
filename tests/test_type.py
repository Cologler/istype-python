# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Type, Any

from istype import isinstanceof

def test_type():
    class User:
        pass

    class BasicUser(User):
        pass

    class ProUser(User):
        pass

    class TeamUser(ProUser):
        pass

    assert isinstanceof(User, Type[User])
    assert isinstanceof(BasicUser, Type[User])
    assert isinstanceof(ProUser, Type[User])
    assert isinstanceof(TeamUser, Type[User])
    assert not isinstanceof(str, Type[User])
    assert isinstanceof(str, Type[Any])
