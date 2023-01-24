from . import db, ma


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    assets = db.relationship('AssetModel', backref='category')

    @classmethod
    def get_by_id(cls, category_id):
        return cls.query.filter_by(id=category_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class CategorySchema(ma.Schema):
    # class Meta(ModelSchema.Meta):
    #   sqla_session = db.session
    class Meta:
        fields = ('id', 'name', 'created_at', 'updated_at')