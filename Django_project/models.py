from db_init import db
from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, text


class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True,nullable=False, autoincrement=True)
    password = db.Column(db.String(255), nullable=False, comment='密码')
    phone = db.Column(db.String(255), nullable=True, comment='手机号码')
    username = db.Column(db.String(255), nullable=False, comment='用户名')
    type = db.Column(db.String(2),nullable=False,comment='(0-用户,1-管理员)')

    def as_dict(self):
        """将对象转换为字典"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Film_order(db.Model):
    __tablename__ = 'film_order'

    fid = db.Column(Integer, primary_key=True, comment='电影ID')
    sid= db.Column(Integer,nullable=False ,  comment='放映ID')
    seat=db.Column(db.String(255), nullable=False, comment='座位')
    uid=db.Column(Integer,nullable=False,  comment='用户Id')

    def as_dict(self):
        """将对象转换为字典"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class movie(db.Model):
    __tablename__ = 'movie'

    mid = db.Column(db.Integer, primary_key=True,nullable=False, comment='电影ID')
    chinese_name  = db.Column(db.String(255), comment='中文名')
    english_name = db.Column(db.String(255), comment='英文名')
    img_url = db.Column(db.String(255), comment='图片地址')
    type = db.Column(db.String(2), comment='类型')
    length = db.Column(db.String(255), comment='片长')
    release_date = db.Column(db.Date, comment='上映时间')
    introduction =db.Column(db.String(1000), comment='简介')
    rating =db.Column(db.String(45), comment='评分')
    country =db.Column(db.String(45), comment='国家')
    actors =db.Column(db.String(45), comment='演员')
    director =db.Column(db.String(45), comment='导演')
    showing =db.Column(db.String(2), comment='是否上架')

    def as_dict(self):
        """将对象转换为字典"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class screen(db.Model):
    __tablename__ = 'screen'

    sid = db.Column(db.Integer, primary_key=True, comment='放映ID')
    cid = db.Column(db.Integer, comment='影院ID')
    mid = db.Column(db.Integer, comment='电影ID')
    language = db.Column(db.String(255), comment='语言')
    price = db.Column(db.Integer, comment='价格')
    room = db.Column(db.Integer, comment='放映厅')
    show_date = db.Column(db.String(255), comment='放映日期')
    show_time = db.Column(db.String(255), comment='放映时间')
    seat = db.Column(db.String(255), comment='座位')

    def as_dict(self):
        """将对象转换为字典"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# class slick(db.Model):
#     __tablename__ = 'slick'

#     id = db.Column(db.Integer,  comment='序号')
#     name = db.Column(db.String(255), comment='电影名')
#     imageUrl = db.Column(db.String(765),  comment='图片链接')
#     box_office = db.Column(db.String(255), comment='票房')

#     def as_dict(self):
#         """将对象转换为字典"""
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Cinema(db.Model):
    __tablename__ = 'cinema'

    cid = db.Column(db.Integer, primary_key=True, comment='电影ID')
    name = db.Column(db.String(255),  comment='电影院名')
    address = db.Column(db.String(1000),  comment='电影地址')
    phone = db.Column(db.String(45),  comment='联系电话')
    city = db.Column(db.String(45),  comment='城市')


    def as_dict(self):
        """将对象转换为字典"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


