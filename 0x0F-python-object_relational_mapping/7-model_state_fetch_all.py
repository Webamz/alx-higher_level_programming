#!/usr/bin/python3
"""Lists all state objects in the database
"""

if __name__ == '__main__':
    import sys
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print(f'{state.id}: {state.name}')

    session.close()
