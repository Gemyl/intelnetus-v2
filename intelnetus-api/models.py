from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Publication_Db_Model(db.Model):
    __tablename__ = "publications"
    id = db.Column(db.String(40), primary_key = True)
    doi = db.Column(db.String(50), unique = True)
    year = db.Column(db.String(4))
    title = db.Column(db.String(100))
    journal = db.Column(db.String(100))
    abstract = db.Column(db.String(100))
    keywords = db.Column(db.String(100))
    fields = db.Column(db.String(100))
    fields_abbreviations = db.Column(db.String(100))
    citations_count = db.Column(db.String(100))
    authors_number = db.Column(db.Integer)
    organizations_number = db.Column(db.Integer)

class Author_Db_Model(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.String(40), primary_key = True)
    scopus_id = db.Column(db.String(15), unique = True)
    orcid_id = db.Column(db.String(20))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    study_fields = db.Column(db.String(100))
    affiliations = db.Column(db.String(100))
    h_index = db.Column(db.Integer)
    citations_count = db.Column(db.Integer)

class Organization_Db_Model(db.Model):
    __tablename__ = "organizations"
    id = db.Column(db.String(40), primary_key = True)
    scopus_id = db.Column(db.String(15), unique = True)
    name = db.Column(db.String(100))
    primary_type = db.Column(db.String(15))
    secondary_type = db.Column(db.String(25))
    address = db.Column(db.String(100))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))

class Publication_Author_Db_Model(db.Model):
    __tablename__ = "publications_authors"
    publication_id = db.Column(db.String(40), db.ForeignKey('publications.id'), primary_key = True)
    author_id = db.Column(db.String(40), db.ForeignKey('authors.id'), primary_key = True)

class Publication_Organization_Db_Model(db.Model):
    __tablename__ = "publications_organizations"
    publication_id = db.Column(db.String(40), db.ForeignKey('publications.id'), primary_key = True)
    organization_id = db.Column(db.String(40), db.ForeignKey('organizations.id'), primary_key = True)

class Author_Organization_Db_Model(db.Model):
    __tablename__ = "authors_organizations"
    author_id = db.Column(db.String(40), db.ForeignKey('authors.id'), primary_key = True)
    organization_id = db.Column(db.String(40), db.ForeignKey('organizations.id'), primary_key = True)
    year = db.Column(db.String(4), primary_key = True)

class Publication_Variant_Db_Model(db.Model):
    __tablename__ = "publications_variants"
    first_variant_id = db.Column(db.String(40), db.ForeignKey('publications.id'), primary_key = True)
    second_variant_id = db.Column(db.String(40), db.ForeignKey('publications.id'), primary_key = True)

class Author_Variant_Db_Model(db.Model):
    __tablename__ = "authors_variants"
    first_variant_id = db.Column(db.String(40), db.ForeignKey('authors.id'), primary_key = True)
    second_variant_id = db.Column(db.String(40), db.ForeignKey('authors.id'), primary_key = True)

class Organization_Variant_Db_Model(db.Model):
    __tablename__ = "organizations_variants"
    first_variant_id = db.Column(db.String(40), db.ForeignKey('organizations.id'), primary_key = True)
    second_variant_id = db.Column(db.String(40), db.ForeignKey('organizations.id'), primary_key = True)