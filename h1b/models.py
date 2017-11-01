from h1b import db


class Cases(db.Model):

    id = db.Column(db.String(), primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
    nbr_immigrants = db.Column(db.Integer)

    job_title = db.Column(db.String(3))
    # In a perfect world this would be a foreign key to
    # job_code(codes), but there's a lot of job_codes in the cases
    # which aren't valid job codes

    begin_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    wage_rate = db.Column(db.Float)
    rate_per = db.Column(db.String())
    prevailing_wage = db.Column(db.Float)

    def __init__(self, id_, employer_id, nbr_immigrants, job_title,
                 begin_date, end_date, wage_rate, rate_per, prevailing_wage):
        self.id = id
        self.employer_id = employer_id
        self.nbr_immigrants = nbr_immigrants
        self.job_title = job_title
        self.begin_date = begin_date
        self.end_date = end_date
        self.wage_rate = wage_rate
        self.rate_per = rate_per
        self.prevailing_wage = prevailing_wage

    def __rep__(self):
        return 'Case id: {}'.format(self.id_)


class Employer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String(2))
    postal_code = db.Column(db.String())

    def __init__(self, id, name, city, state, postal_code):
        self.id = id
        self.name = name
        self.city = city
        self.state = state
        self.postal_code = postal_code

    def __rep__(self):
        return '{}'.format(self.name)
