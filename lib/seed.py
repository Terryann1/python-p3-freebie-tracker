#!/usr/bin/env python3

# Script goes here!
from  models import Company,Dev,Freebie,Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///freebies.db')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#creating a session
session.query(Company).delete()
session.query(Dev).delete()
session.query(Freebie).delete()

#seed data to dev table
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
dev3 = Dev(name="Mary")
dev4 = Dev(name="James")
dev5 = Dev(name="Mark")

#seed data to company table
company1 = Company(name="Tech Corp", founding_year=2000)
company2 = Company(name="Code Masters", founding_year=2010)
company3 = Company(name="Flat Iron", founding_year=2009)
company4 = Company(name="Google", founding_year=2011)
company5 = Company(name="Microsoft", founding_year=2019)


#seed data to freebies table
freebie1 = Freebie(item_name="T-shirt", value=20, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Sticker Pack", value=5, dev=dev2, company=company2)
freebie3 = Freebie(item_name="Mug", value=25, dev=dev1, company=company3)
freebie4= Freebie(item_name="Book", value=30, dev=dev3, company=company2)
freebie5= Freebie(item_name="Pen", value=13, dev=dev3, company=company4)
freebie6 = Freebie(item_name="Watch", value=26, dev=dev2, company=company1)
freebie7 = Freebie(item_name="Bag", value=6, dev=dev4, company=company3)
freebie8 = Freebie(item_name="Mouse", value=19, dev=dev4, company=company5)
freebie9 = Freebie(item_name="Keyboard", value=28, dev=dev5, company=company5)
freebie10 = Freebie(item_name="File", value=17, dev=dev5, company=company4)


# Add Freebie instances to the session
session.add_all([freebie1, freebie2, freebie3, freebie4, freebie5, freebie6, freebie7, freebie8, freebie9, freebie10])

# Commit the Freebie objects to the database
session.commit()

#Add and commit the data
session.bulk_save_objects([dev1,dev2,dev3,dev4,dev5,company1,company2,company3,company4,company5,freebie1,freebie2,freebie3,
                 freebie4,freebie5,freebie6,freebie7,freebie8,freebie9,freebie10])


session.commit()


print("Devs:")
for dev in session.query(Dev).all():
    print(dev)

print("\nCompanies:")
for company in session.query(Company).all():
    print(f"{company.name} (Founded: {company.founding_year})")

print("\nFreebies:")
for freebie in session.query(Freebie).all():
    print(f"{freebie.item_name} (Value: {freebie.value})")
    print(f"  Dev: {freebie.dev.name}")
    print(f"  Company: {freebie.company.name}")


# Function of printing details
freebies = [freebie1, freebie2, freebie3, freebie4, freebie5, freebie6, freebie7, freebie8, freebie9, freebie10]

for freebie in freebies:
    print(freebie.print_details())


    
for freebie in freebies:
    print(freebie.print_details())

# Example of finding the oldest company
companies = [company1, company2, company3, company4, company5]
oldest = Company.oldest_company(companies)
print(f"The oldest company is {oldest.name}, founded in {oldest.founding_year}.")




