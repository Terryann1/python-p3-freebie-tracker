from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, ForeignKeyConstraint,Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


# #Association table

companies_devs = Table(
    'companies_devs', Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', Integer, ForeignKey('devs.id'), primary_key=True)
)


class Company(Base):
    __tablename__ = 'companies'

    #one-to-many relationship
    freebie=relationship('Freebie',backref='company')


    # Many-to-many relationship with Dev
    devs = relationship("Dev", secondary=companies_devs, back_populates="companies")
    

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def __init__(self, name, founding_year):
        self.name = name
        self.founding_year = founding_year
        self.freebies = []  # To store all freebies associated with this company


    # Method to give a freebie to a developer
    def give_freebie(self, dev, item_name, value):    
        freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        self.freebies.append(freebie) 
        return freebie 
     
    
    # Method to return all freebies given by this company
    def get_freebies(self):  
        return self.freebies
    

      # Method to return all developers who have collected freebies from this company
    def devs(self):
        return set(freebie.dev for freebie in self.freebies)
    
      # Class method to get the oldest company
    @classmethod
    def oldest_company(cls, companies):
        #Find and return the company with the earliest founding year
        return min(companies, key=lambda company: company.founding_year)

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'
    
#one-to-many relationship
    freebies=relationship('Freebie',backref='dev')


    # Many-to-many relationship with Company
    companies = relationship("Company", secondary=companies_devs, back_populates="devs")
    

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __init__(self, name):
        self.name = name
        self.freebies=[]

     # Method to check if the dev has received a specific freebie item
    def received_one(self, item_name):
     # Check if any freebie associated with this dev has the given item_name
        return any(freebie.item_name == item_name for freebie in self.freebies)   



    def give_away(self,dev,freebie):
          if freebie.dev == self:
            # If the freebie belongs to the current developer, change its ownership
            freebie.dev = dev
            dev.freebies.append(freebie)  # Add the freebie to the new dev's list
            # remove the freebie from the current dev's list
            if freebie in self.freebies:
                self.freebies.remove(freebie) 
            return True 
          return False
    
    
    
    # Method to return all the companies that gave freebies to this developer
    def companies(self):
        return set(freebie.company for freebie in self.freebies)

    def __repr__(self):
        return f'<Dev {self.name}>'
    
class Freebie(Base):
    __tablename__='freebies'
    id=Column(Integer(),primary_key=True)
    item_name=Column(String(255)) 
    value=Column(Integer) 


#foriegnkey to dev and company
    dev_id=Column(Integer,ForeignKey('devs.id'))
    company_id=Column(Integer,ForeignKey('companies.id')) 

    def __init__(self, item_name, value, dev, company):
        self.item_name = item_name
        self.value = value
        self.dev = dev
        self.company = company

    def print_details(self):
        # Format and return the string as specified
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."



    def __repr__(self):
        return f"<Freebie(item_name={self.item_name}, value={self.value})>"
    
