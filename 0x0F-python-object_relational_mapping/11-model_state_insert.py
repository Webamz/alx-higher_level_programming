#!/usr/bin/python3
"""Add state with name 'Louisiana
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))

    Base.metadata.create_all(engine)

    session = Session(engine)
    new = State(name='Louisiana')
    session.add(new)
    state = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()

    print(f'{state.id}')
    session.close()
