#!/usr/bin/env python
import nox


@nox.session(python=["3.9"])
def tests(session: nox.Session) -> None:
    """"""
    session.install("pytest")
    session.run("pytest", "tests")
