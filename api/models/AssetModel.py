from . import db, ma


class AssetModel(db.Model):
    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    serial_number = db.Column(db.String(100), nullable=False, unique=True)
    model = db.Column(db.String(80))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())



    @classmethod
    def get_by_id(cls, asset_id):
        return cls.query.filter_by(id=asset_id).first()
    #
    # @classmethod
    # def get_by_email(cls, email):
    #     return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


class AssetSchema(ma.Schema):
    # class Meta(ModelSchema.Meta):
    #   sqla_session = db.session
    class Meta:
        fields = ('id', 'name', 'serial_number', 'category', 'model', 'created_at', 'updated_at')
