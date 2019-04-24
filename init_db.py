from main import db, Fighter

# Create all the tables
db.create_all()

# create fighters
#csk = Fighter(name='CSK')
#srh = Fighter(name='SRH')
#mi = Fighter(name='MI')
#kxip = Fighter(name='KXIP')
#dc = Fighter(name='DC')
rr = Fighter(name='RR')
#rcb = Fighter(name='RCB')
kkr = Fighter(name='KKR')


# add fighters to session
""" db.session.add(csk)
db.session.add(srh)
db.session.add(mi) """
#db.session.add(kxip)
#db.session.add(dc)
db.session.add(rr)
#db.session.add(rcb)
db.session.add(kkr)


# commit the fighters to database
db.session.commit()
