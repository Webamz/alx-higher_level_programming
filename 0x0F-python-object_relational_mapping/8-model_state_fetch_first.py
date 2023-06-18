#!/usr/bin/python3
"""Prints first state object
"""

if __name__ == '__main__':
    import sys
    import sqlalchemy
    from model_state import State, Base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))
    
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if state:
        print(f'{state.id}: {state.name}')
    else:
        print("Nothing")

    session.close()