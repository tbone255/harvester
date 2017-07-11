from datetime import datetime

from sqlalchemy import create_engine, MetaData
from sqlalchemy import select
from sqlalchemy import Table, Column
from sqlalchemy.types import Integer, String
from sqlalchemy import ForeignKey, DateTime


metadata = MetaData()

class DBUtil(object):
    '''
    Harvester Database Utility
    '''
    
    def __init__(self, db_uri=None):
        self.engine = create_engine(db_uri, pool_recycle=600)


    def get_connection(self):
        return self.engine.connect()


    def get_tables(self):
        '''
        Return list of tables
        '''
        return metadata.tables.keys()


    def _execute_select(self, query):
        '''
        Given SQLAlchemy core query, execute select statement
        '''
        conn = self.get_connection()
        result = conn.execute(query).fetchall()
        conn.close()
        result = [dict(row.items()) for row in result]
        return result


    def _execute_insert(self, query):
        '''
        Given SQLAlchemy core query, execute insert statement
        '''
        conn = self.get_connection()
        result = conn.execute(query).last_inserted_ids()
        conn.close()
        result = [dict(row.items()) for row in result]
        return result

    ##################
    # SELECT Queries #
    ##################
    
    def get_event_by_id(self, event_id):
        '''
        Return event given event_id
        '''
        query = select([event_table]).where(
            event_table.c.event_id == event_id
        )
        result = self._execute_select(query)
        return result


    def get_plant_by_id(self, plant_id):
        '''
        Return plant given plant_id
        '''
        query = select([plant_table]).where(
            plant_table.c.plant_id == plant_id
        )
        result = self._execute_select(query)
        return result


    def get_event_log_by_id(self, event_log_id):
        '''
        Return event log given event_log_id
        '''
        query = select([event_log_table]).where(
            event_log_table.c.event_log_id == event_log_id
        )
        result = self._execute_select(query)
        return result
      
    def get_plant_event_log(self, plant_id):
        '''
        Return event log of plant given plant_id
        '''
        query = select([event_log_table]).where(
            event_log_table.c.plant_id == plant_id
        )
        result = self._execute_select(query)
        return result
        
    def get_water_schedule_of_plant_by_date(self, plant_id, start_date, end_date):
        '''
        Return all dates of which a plant was watered given a date range
        '''
        datetime_start_object = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        datetime_end_object = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

        query = select([event_log_table]).where(
            event_log_table.c.timestamp >= datetime_start_object).where(
            event_log_table.c.timestamp <= datetime_end_object).where(
            event_log_table.c.plant_id == plant_id).where(
            event_log_table.c.event_id == 2
        )
        result = self._execute_select(query)
        return result

    def get_plants_in_planter(self, planter_id):
        '''
        Return all plants (plant_id) within a given planter
        '''
        query = select([event_log_table]).where(
            event_log_table.c.planter_id == planter_id).where(
            event_log_table.c.plant_id != None
        )
        result = self._execute_select(query)
        return result

    def get_fertilize_schedule_of_plant_by_date(self, plant_id, start_date, end_date):
        '''
        Return all dates of which a plant was fertilized given a date range
        '''
        datetime_start_object = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        datetime_end_object = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

        query = select([event_log_table]).where(
            event_log_table.c.timestamp >= datetime_start_object).where(
            event_log_table.c.timestamp <= datetime_end_object).where(
            event_log_table.c.plant_id == plant_id).where(
            event_log_table.c.event_id == 3
        )
        result = self._execute_select(query)
        return result
    
    def get_fertilizers(self):
        '''
        Return a list of all fertizilers
        '''
        query = select([nutrition_table.c.brand, nutrition_table.c.type])
        result = self._execute_select(query)
        return result

    def get_events(self):
        '''
        Return a list of all events available
        '''
        query = select([event_table.c.event_type])
        result = self._execute_select(query)
        return result

    def get_plants(self):
        '''
        Return a list of plants available
        '''
        query = select([plant_table.c.type])
        result = self._execute_select(query)
        return result

    def get_planters(self):
        '''
        Return a list of all planters available
        '''
        query = select([planter_table.c.planter_id])
        result = self._execute_select(query)
        return result

    def get_nutrition_for_plant(self, plant_id):
        '''
        Return a list every type of nutrition a plant has been given
        '''
        query = select([nutrition_table.c.brand, nutrition_table.c.type]).where(
            nutrition_table.c.nutrition_id.in_(select([event_log_table.c.nutrition_id]))).where(
            event_log_table.c.plant_id == plant_id
        ).distinct()
        result = self._execute_select(query)
        return result
    
    # TODO once harvest weight is added
    # 1. get harvest amount (in lbs) of a plant
    # 2. get harvest from a planter (all plants) in lbs
    # 3. get harvest from a plant type in lbs.
       
    ##################
    # INSERT Queries #
    ##################
     
    def add_nutrition(self, brand, nutr_type, description):
        '''
        Insert nutrition row
        
        Args:
            brand - brand of nutrition
            type - type of nutrition
            description - text description of the nutrition
        '''
        data = {
            'brand': brand,
            'type': nutr_type,
            'description': description
        }
        query = nutrition_table.insert().values(data)
        result = self._execute_insert(query)
        return result
        
        
    def add_planter(self, length, width, x=None, y=None):
        '''
        Insert a planter
        
        Args:
            x - x coordinate
            y - y coordinate
            length - length of planter
            width - width of planter
            
        Assumptions:
            Planters exist on an XY plane (flat)
            Planters are rectangular 2X + 2Y sides
        '''
        data = {
            'x_coordinate': x,
            'y_coordinate': y,
            'length': length,
            'width': width
        }
        query = planter_table.insert().values(data)
        result = self._execute_insert(query)
        return result
        
        
    def add_plant(self, plant_type, scientific_name, description):
        '''
        Insert a plant
        
        Args:
            plant - plant type
            name - scientific name
            description - text description of event
        '''
        data = {
            'type': plant_type,
            'scientific_name': scientific_name,
            'description': description
        }
        query = plant_table.insert().values(data)
        result = self._execute_insert(query)
        return result
      
      
    def add_event_log(self, event, description, plant=None, planter=None, nutrition=None):
        '''
        Insert an event to the event log
        
        Args:
            event - event type
            plant - plant id (default: None)
            planter - planter id (default: None)
            nutrition - fertlizier (default: None)
            description - text description of event 
        '''
        data = {
            'event_id': event,
            'plant_id': plant,
            'planter_id': planter,
            'nutrition_id': nutrition,
            'timestamp': datetime.utcnow(),
            'description': description
        }
        query = event_log_table.insert().values(data)
        result = self._execute_insert(query)
        return result
        

    def add_event(self, event_type, description):
        '''
        Insert new event type
        
        Args:
            event - event type
            description - text description of event
        '''
        data = {
            'event_type': event_type,
            'description': description
        }
        query = event_table.insert().values(data)
        result = self._execute_insert(query)
        return result
      
      
      
event_table = Table('event', metadata,
    Column('event_id', Integer, primary_key=True),
    Column('event_type', String(32), nullable=False),
    Column('description', String(128), nullable=False)
)

plant_table = Table('plant', metadata,
    Column('plant_id', Integer, primary_key=True),
    Column('type', String(32), nullable=False),
    Column('scientific_name', String(128), nullable=False),
    Column('description', String(512), nullable=False)
)

nutrition_table = Table('nutrition', metadata,
    Column('nutrition_id', Integer, primary_key=True),
    Column('brand', String(32)),
    Column('type', String(32), nullable=False),
    Column('description', String(128), nullable=False)
)

planter_table = Table('planter', metadata,
    Column('planter_id', Integer, primary_key=True),
    Column('x_coordinate', Integer),
    Column('y_coordinate', Integer),
    Column('length', Integer, nullable=False),
    Column('width', Integer, nullable=False)
)

event_log_table = Table('event_log', metadata,
    Column('event_log_id', Integer, primary_key=True),
    Column('event_id', Integer, ForeignKey('event.event_id')),
    Column('plant_id', Integer, ForeignKey('plant.plant')),
    Column('planter_id', Integer, ForeignKey('planter.planter_id')),
    Column('nutrition_id', Integer, ForeignKey('nutrition.nutrition_id')),
    Column('timestamp', DateTime),
    Column('description', String(256)),
)