#!/usr/bin/python3
"""Adds state (California) with city(San Francisco)
"""

if __name__ == '__main__':
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))

    Base.metadata.create_all(engine)
    session = Session(engine)
    new_city = City(name='San Francisco')
    new_state = State(name='California')

    new_state.cities.append(new_city)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
