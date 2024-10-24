from werkzeug.exceptions import BadRequest

from db_init import app
from flask import jsonify, request
import function
from function import login
from models import movie
import logging
logging.basicConfig(level=logging.DEBUG)
userid=None
city=""


def init_routes(app):

    @app.route('/login', methods=['POST'])
    def login_route():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Missing username or password'}), 400

        result = function.login(username, password)

        if result:
            global userid
            userid=function.get_uid(username)
            logging.debug(f"userid:{userid}")
            return jsonify({'success': True,'user':username})
            
            
        else:
            return jsonify({'success': False,'user':username}), 401
        
    @app.route('/register', methods=['POST'])
    def register_route():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        uid=data.get('uid')
        if not username or not password:
            return jsonify({'error': 'Missing username or password'}), 400

        result = function.register(username, password)

        if result == 1:
            return jsonify({'success':False})
        elif result == 0:
            return jsonify({'success':True})
        else :
            return jsonify({'error':'插入失败'})
        
    @app.route('/Home.rate', methods=['GET'])
    def get_top5_movie():
        result = function.get_top5_movie()
        return jsonify(result), 201

    @app.route('/Home', methods=['GET'])
    def home():
        movies=function.first_page_show()
        #movies=[{"name":'aaa',"poster":'http://p1.meituan.net/movie/f013c57e9506cd2e7c609397c8da04d9213647.jpg@464w_644h_1e_1c',"mid":1}]
        return movies
    
    #获取城市
    @app.route('/city', methods=['POST'])
    def get_city():
        data = request.get_json()  # Parse JSON from request body
        city = data.get('cityName')  # Get the city name from the JSON object
        # city=str(city_name)
        logging.debug(f"Received city: {city}")
        # Do something with city_name
        return jsonify({'success': True}), 200
    
    #电影界面
    @app.route('/all_movies', methods=['GET'])
    def get_movies():
        city_name = request.args.get('city')
        logging.debug(f"Received city2: {city_name}")
        movies=function.get_all_movies(city_name)
        return movies

    #我的订单
    @app.route('/myfilm', methods=['GET'])
    def get_myfilm():
        global userid
        logging.debug(f"second_userid{userid}")
        information=function.get_my_film(userid)
        return information
        # return [{"name": 'aaa', "address": 'aaa',"room":'row[2]',"date":'row[3]',
        #                 "seat":'row+排+col+座',"cinema":'row[5]'},{"name": 'aaa', "address": 'aaa',"room":'row[2]',"date":'row[3]',
        #                 "seat":'row+排+col+座',"cinema":'row[5]'}]
    
    
   
    
    @app.route('/all_movies_search', methods=['POST'])
    def get_movies_search():
        
        data=request.get_json()
        search=data.get('searchname')
        city = data.get('city')
        movies=function.get_movies_search(city,search)
        logging.debug(f"Received city3: {city}")
        return movies
    
    #电影院订票
    @app.route('/cinema_ticket', methods=['POST'])
    def get_cinema_ticket():
        data = request.get_json()  # Parse JSON from request body
        movieid = data.get('mid')  # Get the city name from the JSON object
        show_date=data.get('show_date')
        city = data.get('city')
        mid=int(movieid)
        movies=function.get_all_cinema(city,mid,show_date)
        logging.debug(f"Received city4: {city}")
        return movies
        #return [{"name": "row[0]", "address":" row[1]","show_date":"row[2]", "show_time": "row[3]","price": "row[4]","sid":0}]
   

    # get_seat前端传入sid搜索
    @app.route('/get_seat', methods=['GET'])
    def get_seat():
        sid = request.args.get('sid')
        # data = request.get_json()
        # sid = data.get('sid')
        result = function.get_seat(sid)
        return jsonify(result)
    
    # 删除fid
    @app.route('/delete_order', methods=['POST'])
    def order_delete():
        data=request.get_json()
        fid=data.get('fid')
        date=data.get('date')
        time=data.get('time')
        logging.debug(f"{date}")
        logging.debug(f"{time}")
        result = function.delete_o(fid)
        return jsonify(result)
    
    #前端传入arrlist来更新座位表
    @app.route('/update_seat', methods=['POST'])
    def update_seat():
        data = request.get_json()
        res=data.get('list')
        sid=data.get('sid')
        ret=''
        rett=''
        for item in res:
            isCheck = item.get('isCheck')
            status=item.get('status')
            if isCheck== True:
                ret+='1'
                rett+='1'
            else:
                rett+='0'
                if status=='N':
                    ret+='1'
                else:
                    ret+='0'
        logging.debug(f"{ret}")
        result = function.update_seat(sid,ret,userid,rett)
        return jsonify(result)
  
if __name__ == '__main__':
    
    init_routes(app)
    app.run(debug=True)