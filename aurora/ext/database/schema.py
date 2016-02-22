import peewee as pee

db = pee.SqliteDatabase("_database.sqlite")


class ModelloBase(pee.Model):
	class Meta:
		database = db


class Software(ModelloBase):
	title = pee.TextField()
	year = pee.CharField(max_length=4)
	publisher = pee.TextField()
	country = pee.CharField(max_length=2)
	hash = pee.TextField(primary_key=True)


class Preview(ModelloBase):
	base = pee.TextField(primary_key=True)
	picture = pee.BlobField()


class Manual(ModelloBase):
	base = pee.TextField(primary_key=True)
	description = pee.TextField()


def connetti():
	global db
	db.connect()


def chiudi():
	global db
	db.close()


connetti()