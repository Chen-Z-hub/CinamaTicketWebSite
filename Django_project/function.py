from datetime import datetime
import flask
from flask import jsonify
from sqlalchemy import func, distinct,delete

from sqlalchemy.sql import select, label
from db_init import db, app
from sqlalchemy import text
from models import User,Film_order,movie,screen,Cinema
from typing import Optional, Tuple
import logging

logging.basicConfig(level=logging.DEBUG)

def get_time():
    nowTime = datetime.now()
    return {
        'Task': 'Connect the frontend and the backend successfully!',
        'Date': nowTime,
        'Frontend': 'React',
        'Backend': 'Flask'
    }
# 登录
def login(user: str, password: str):
    with app.app_context():
        logging.debug(f"{user}{password}")
        query = text("SELECT * FROM user WHERE username = :username AND password = :password")
        try:
            result = db.session.execute(query, {'username': user, 'password': password}).fetchone()
            logging.debug(f"Query :{result}")
            if result:
                return True  # 返回User对象和成功标志1
            else:
                return False # 用户名密码不匹配或用户不存在，返回None和失败标志0
        except:
            #print(f"Database error occurred: {e}")
            return False  # 数据库错误，也返回None和失败标志0
        
def get_uid(username) :
    with app.app_context():
        query = text("SELECT uid FROM user WHERE username = :username")
        result = db.session.execute(query, {'username': username}).fetchone()
        logging.debug(f"get_uid:{result}")
        return result[0]
        

def first_page_show()-> flask.Response:
    with app.app_context():
        query = text("SELECT chinese_name,img_url,mid FROM movie WHERE mid<6")
        # 假设你的Session实例为session，执行查询
        result = db.session.execute(query).fetchall()
        i = 0
        ret = []
        # 遍历结果
        for row in result:
            ret.append({"name": row[0], "poster": row[1],"mid":row[2]})
        return jsonify(ret)      

#注册
def register(username:str,password)-> int:
    with app.app_context():
        #检查用户名是否已存在
        existing_user = db.session.execute(
            text("SELECT * FROM user WHERE username = :username"), {'username': username}
        ).fetchone()

        if existing_user:
            return 1

        # 插入新用户
        sql_query = text("""
        INSERT INTO user (username, password, type) VALUES (:username, :password, 0)
            """)

        # 使用 params 参数传递变量值
        results = db.session.execute(sql_query, {"username": username, "password": password})

        # 提交事务以保存更改
        db.session.commit()
        
        existing_user2 = db.session.execute(
            text("SELECT * FROM user WHERE username = :username"), {'username': username}
        )
        if existing_user2:
            return 0
        else:
            return 2
        
# 1
def get_top5_movie(): #得到票房最高的五部影片
    with app.app_context():
        query = select(
            movie.chinese_name.label('name'),
            movie.rating.label('rating')
        ).where(
            movie.rating != ''
        ).order_by(
            movie.rating.desc()
        ).limit(5)
        query = text("SELECT chinese_name,rating FROM movie WHERE rating!='暂无评分' Order by rating DESC LIMIT 5" )
        # 假设你的Session实例为session，执行查询
        result = db.session.execute(query).fetchall()
        ret=[]
        # 遍历结果
        for row in result:
            num=round(float(row[1])-5.0,1)
            ret.append({"name": row[0], "score":num})
        return ret
    


# #电影院订票界面
# def get_all_cinema(city,mid,show_date)-> flask.Response:
#     with app.app_context():
#         logging.debug(f"function Received city: {city}")
#         result = db.session.execute(text('''
#         SELECT cinema.name,cinema.address,screen.show_date,screen.show_time,screen.price,screen.sid
#         FROM Movie join screen
#         on Movie.mid=screen.mid
#         join cinema
#         on cinema.cid=screen.cid
#         where city=:city and movie.mid=:mid and screen.show_date=:show_date;'''),{'city':city,'mid':mid,'show_date':show_date}).fetchall()
#         i = 0
#         ret = []
#         # 遍历结果
#         for row in result:
#             ret.append({"name": row[0], "address": row[1],"show_date":row[2], "show_time": row[3],"price": row[4],"sid":row[5]})
#         return jsonify(ret)     
#电影院订票界面
def get_all_cinema(city, mid, show_date) -> flask.Response:
    with app.app_context():
        logging.debug(f"function Received city: {city}")
        result = db.session.execute(text('''
            SELECT cinema.name, cinema.address, screen.show_date, screen.show_time, screen.price, screen.sid
            FROM movie
            JOIN screen ON movie.mid = screen.mid
            JOIN cinema ON cinema.cid = screen.cid
            WHERE cinema.city = :city AND movie.mid = :mid AND screen.show_date = :show_date
            ORDER BY screen.show_time ASC;
        '''), {'city': city, 'mid': mid, 'show_date': show_date}).fetchall()
        
        ret = []
        
        
        current_time = datetime.now()
        
        for row in result:
            #logging.debug(f"function row: {row}")
            date = row[2]
            time = row[3][:5]
            date_string = f"{date} {time}:00"
            format_string = "%Y-%m-%d %H:%M:%S"
            dt_object = datetime.strptime(date_string, format_string)
            
            #logging.debug(f"电影时间 {dt_object}")
            #logging.debug(f"本地时间 {current_time}")
            
            #if dt_object > current_time:
            ret.append({"name": row[0], "address": row[1], "show_date": row[2], "show_time": row[3], "price": row[4], "sid": row[5]})
        
        return jsonify(ret)

#movie页面  
def get_all_movies(city)-> flask.Response:
    with app.app_context():
        logging.debug(f"function Received city: {city}")
        result = db.session.execute(text('''SELECT DISTINCT chinese_name,img_url,movie.mid
        FROM movie join screen
        on movie.mid=screen.mid
        join cinema
        on cinema.cid=screen.cid
        where city=:city;'''),{'city':city}).fetchall()
        i = 0
        ret = []
        # 遍历结果
        for row in result:
            if len(row[0])>5:
                namee=row[0][:5]+'..'
            else:
                namee=row[0]
            ret.append({"name": namee, "poster": row[1],"mid":row[2]})
        return jsonify(ret)     
    
#movie页面搜索框
def get_movies_search(city,search)-> flask.Response:
    with app.app_context():
        logging.debug(f"function Received city: {city}")
        result = db.session.execute(text('''SELECT DISTINCT chinese_name,img_url,movie.mid
        FROM movie join screen
        on movie.mid=screen.mid
        join cinema
        on cinema.cid=screen.cid
        where city=:city and chinese_name LIKE CONCAT('%', :movie_search, '%');'''),{'city':city,'movie_search':search}).fetchall()
        i = 0
        ret = []
        # 遍历结果
        for row in result:
            if len(row[0])>5:
                namee=row[0][:5]+'..'
            else:
                namee=row[0]
            ret.append({"name": namee, "poster": row[1],"mid":row[2]})
        return jsonify(ret)    


# 5
def movie_detail(mid_detail):
    with app.app_context():
        # 执行原生SQL查询
        results = db.session.execute(text("""
            select * from movie where mid=:mid_detail;
        """
        ),{"mid_detail":mid_detail})
        # 转换结果为字典列表
        ret = []
        for row in results:
            ret.append(dict({"mid": row[0], "chinese_name": row[1], "english_name": row[2], "img_url": row[3],
                             "type": row[4], "length": row[5],"release_date":row[6],"introduction":row[7],
                             "rating":row[8],"country":row[9],"actors":row[10],"director":row[11],"showing":row[12]}))
        
        return ret


# 5
# 事件状态统计
def buy_tickets(mid_detail,place):
    with app.app_context():
        results = db.session.execute(text("""
           SELECT
                m.mid,
                m.chinese_name,
                m.english_name,
                m.img_url,
                m.type,
                m.length,
                m.release_date,
                m.rating,
                m.country,
                s.show_date,
                s.price,
                c.name,
                c.address
                FROM
                movie m
                JOIN
                screen s ON m.mid = s.mid
                JOIN
                cinema c ON s.cid = c.cid
                WHERE
                m.mid = :mid_detail AND c.city = :place;
        """
        ),{"mid_detail": mid_detail,"place":place})
        # 转换结果为字典列表
        ret = []
        for row in results:
            ret.append(dict(
                {"courseTaskId": row[0], "start_count": row[1], "doing_count": row[2], "watching_count": row[3],
                 "finish_count": row[4]}))
        
        return ret

#get_seat前端传入sid搜索
def get_seat(screen_id):
    with app.app_context():
        results = db.session.execute(text("""
           SELECT
                s.seat
                FROM
                screen s
                WHERE
                s.sid=:screen_id;
        """
        ), {"screen_id": screen_id})
        # 转换结果为字典列表
        ret = []
        cnt=1
        for i in results:
            row=i[0]
        #logging.debug(f"{row}")
        for c in row:
            row=(cnt-1)//17+1
            col=(cnt-1)%17+1
            if c=='0':
                flag='Y'
            else:
                flag='N'
            ret.append(
                {"id": cnt, "seatNo": f"{row}排{col}座", "status": flag, "rowNo": str(row),
                 "colNo": str(col)})
            cnt+=1
        return ret
    
def update_seat(sid,ret,userid,rett):
    with app.app_context():
        s = screen.query.filter_by(sid=sid).first()
        if s:
            s.seat = ret
            db.session.commit()
            sql_query = text("""
        INSERT INTO film_order (sid,seat,uid) VALUES (:sid, :rett, :userid)
            """)

            # 使用 params 参数传递变量值
            results = db.session.execute(sql_query, {"sid": sid, "rett": rett,"userid":userid})
            db.session.commit()
            return {"success": True}
        else:
            return {"success": False}, 404
# 3
def get_my_film(uid)-> flask.Response:
    with app.app_context():
        result = db.session.execute(text('''select chinese_name, address, room, show_date, 
                film_order.seat, cinema.name,film_order.fid,show_time
                from film_order inner join screen 
                on film_order.sid=screen.sid 
                inner join movie 
                on screen.mid=movie.mid 
                inner join cinema 
                on screen.cid=cinema.cid 
                where film_order.uid=:user'''),{'user': uid})
        i = 0
        ret = []
        # 遍历结果
        for row in result:
            seat=''
            cnt=1
            seatnum=''
            for i in row[4]:
                if(i=='1'):
                    roww=str(int((cnt-1)/17)+1)
                    col=str((cnt-1)%17+1)
                    seatnum+=roww+'排'+col+'座  '
                cnt+=1
            ret.append({"name": row[0], "address": row[1],"room":row[2],"date":str(row[3]),
                        "seat":seatnum,"cinema":row[5],"fid":row[6],"time":row[7]})
        return jsonify(ret)     
    
#电影院订票界面
def delete_o(fid) -> flask.Response:
    with app.app_context():
        logging.debug(f"function Received fid: {fid}")
        result = db.session.execute(text('''
            SELECT seat,film_order.sid from film_order where fid=:fid;
        '''), {'fid':fid}).fetchall()
        
        ret = []
        sid=0
        seatl=''
        seatl2=''
        for i in result:
            seatl=i[0]
            sid=i[1]

        result2 = db.session.execute(text('''
            SELECT seat from screen where sid=:sid;
        '''), {'sid':sid}).fetchall()

        for i in result2:
            seatl2=i[0]
        seatl2_list = list(seatl2) 
        cnt=0
        for c in seatl:
            if(c=='1'):
                seatl2_list[cnt]='0'
            cnt+=1
        seatl2 = ''.join(seatl2_list) 

        s = screen.query.filter_by(sid=sid).first()
        if s:
            s.seat = seatl2
            db.session.commit()
        
        delete_statement = delete(Film_order).where(Film_order.fid == fid)
        db.session.execute(delete_statement)

        # 提交事务，确保更改生效
        db.session.commit()


        # for row in result:
        #     #logging.debug(f"function row: {row}")
        #     date = row[2]
        #     time = row[3][:5]
        #     date_string = f"{date} {time}:00"
        #     format_string = "%Y-%m-%d %H:%M:%S"
        #     dt_object = datetime.strptime(date_string, format_string)
            
        #     logging.debug(f"电影时间 {dt_object}")
        #     logging.debug(f"本地时间 {current_time}")
            
        #     if dt_object > current_time:
        #         ret.append({"name": row[0], "address": row[1], "show_date": row[2], "show_time": row[3], "price": row[4], "sid": row[5]})
        
        return {"success": True}
    
