from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Resource, Api
from models import db, User, Car, Rent
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wheels4rent.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.json.compact = False

db.init_app(app)

migrate = Migrate(app, db)
api = Api(app)


# User Registration
class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")


        if not name or not email or not password:
            return {"error": "Username, email, and password are required."}, 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {"error": "Email already in use."}, 400

        new_user = User(
            name=name,
            email=email,
            password=password,
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "id":"new_user.id",
            "username":"new_user.username",
            
        })

api.add_resource(UserRegister, "/user/register")



class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = str(data.get("password"))

        user = User.query.filter_by(email=email).first()

        if user :
            return jsonify({
            "id": user.id,
            "email": user.email,
             })
        else:
            return {"error": "Invalid email or password"}, 400

        # if user is None:
        #     return jsonify({'error': 'Unauthorized'}), 401

        # if not bcrypt.check_password_hash(user.password, password):
        #     return jsonify({'error': 'Unauthorized, incorrect password'}), 401

api.add_resource(UserLogin, "/user/login")




# Fetch All Users
class Users(Resource):
    def get(self):
        users = User.query.all()
        return make_response(jsonify([user.to_dict() for user in users]), 200)

api.add_resource(Users, "/users")



class UserByID(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            return make_response(jsonify(user.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "User not found"}), 404)

    def patch(self, id):
        data = request.get_json()
        user = User.query.filter(User.id == id).first()

        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        for attr in data:
            setattr(user, attr, data.get(attr))

        db.session.add(user)
        db.session.commit()

        return make_response(user.to_dict(), 200)

    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response("", 204)
        else:
            return make_response(jsonify({"error": "User not found"}), 404)

api.add_resource(UserByID, "/users/<int:id>")





class Cars(Resource):
    def get(self):
        # cars = Car.query.all()
        cars = Car.query.filter_by(is_available=True).all()
        return make_response(jsonify([car.to_dict(only=("id", "name", "price", "image_url", "type", "seats", "fuel_type", "transmission")) for car in cars]), 200)



    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        name = data.get("name")
        price = data.get("price")
        image_url = data.get("image_url")
        is_available = data.get("is_available", True)
        type = data.get("type")
        seats = data.get("seats")
        fuel_type = data.get("fuel_type")
        transmission = data.get("transmission")

        new_car = Car(user_id=user_id, name=name, price=price, image_url=image_url, is_available=is_available, type=type, seats=seats, fuel_type=fuel_type, transmission=transmission)

        db.session.add(new_car)
        db.session.commit()

        # return make_response(jsonify(new_car.to_dict()), 201)
        return make_response(new_car.to_dict(only=("user_id","name","price","image_url", "is_available", "type", "seats", "fuel_type", "transmission")),201)


class CarByID(Resource):
    def get(self, id):
        car = Car.query.filter(Car.id == id).first()
        if car:
            return make_response(jsonify(car.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "car not found"}), 404)


    def patch(self, id):
        data = request.get_json()
        car = Car.query.filter(Car.id == id).first()

        if car:
            for attr, value in data.items():
                setattr(car, attr, value)

            db.session.commit()
            return make_response(car.to_dict(only=("id","name","price","image_url", "type", "seats", "fuel_type", "transmission")),200) 
    
        else:
            return make_response(jsonify({"error": "car not found"}), 404)
    
    def delete(self, id):
        car = Car.query.filter(Car.id == id).first()

        if car:
            db.session.delete(car)
            db.session.commit()
            return make_response("", 204)
        else:
            return make_response(jsonify({"error": "car not found"}), 404)


api.add_resource(Cars, "/cars")
api.add_resource(CarByID, "/cars/<int:id>")




# class CarsByUserID(Resource):
#     def get(self, user_id):
#         cars = Car.query.filter(Car.user_id == user_id).all()
#         if cars:
#             return make_response(jsonify([car.to_dict(only=("id", "name", "price", "image_url", "type")) for car in cars]), 200)
#         else:
#             return make_response(jsonify({"error": "No cars found for this user"}), 404)
        
# api.add_resource(CarsByUserID, "/cars/user/<int:user_id>")





class CarsByUserID(Resource):
    def get(self, user_id):
        cars = Car.query.filter(Car.user_id == user_id).all()
        if cars:
            return make_response(
                jsonify([car.to_dict(only=("id", "name", "price", "image_url", "type", "seats", "fuel_type", "transmission")) for car in cars]),
                200
            )
        else:
            return make_response(jsonify([]), 200)
        
api.add_resource(CarsByUserID, "/cars/user/<int:user_id>")





class Rents(Resource):
    def get(self):
        rents = Rent.query.all()
        # return make_response(jsonify([rent.to_dict() for rent in rents]), 200)
        return make_response(jsonify([rent.to_dict(only=("id", "user_id", "car_id", "pickup_location", "dropoff_location",)) for rent in rents]), 200)

    def post(self):
        try:
            data = request.get_json()
            user_id = data.get("user_id")
            car_id = data.get("car_id")  
            pickup_location = data.get("pickup_location")
            dropoff_location = data.get("dropoff_location")
            duration = data.get("duration")

            car = Car.query.filter_by(id=car_id).first()
            if not car:
                return make_response(jsonify({"error": "Car not found"}), 404)

            if not car.is_available:
                return make_response(jsonify({"error": "Car is not available"}), 400)


            new_rent = Rent(user_id=user_id, car_id=car_id, pickup_location=pickup_location, dropoff_location=dropoff_location, duration=duration,)
            car.is_available = False  

            db.session.add(new_rent)
            db.session.commit()

            # return make_response(jsonify(new_rent.to_dict()), 201)
            return make_response(new_rent.to_dict(only=("user_id","car_id","pickup_location","dropoff_location", "duration")),201)


        except Exception as e:
            print("Error processing request:", e)
            return make_response(jsonify({"error": "Internal server error"}), 500)

api.add_resource(Rents, "/rents")






class RentByID(Resource):
    def get(self, id):
        rent = Rent.query.filter(Rent.id == id).first()
        if rent:
            return make_response(jsonify(rent.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "Rent not found"}), 404)


    def delete(self, id):
        rent = Rent.query.filter(Rent.id == id).first()
        if rent:
            car = Car.query.get(rent.car_id)
            car.is_available = True

            db.session.delete(rent)
            db.session.commit()
            return make_response("", 204)
        else:
            return make_response(jsonify({"error": "Rent not found"}), 404)

api.add_resource(RentByID, "/rents/<int:id>")


# class RentsByUserID(Resource):
#     def get(self, user_id):
#         rents = Rent.query.filter(Rent.user_id == user_id).all()
#         if rents:
#             return make_response(jsonify([rent.to_dict(only=("id", "user_id", "car_id", "pickup_location", "dropoff_location")) for rent in rents]), 200)
#         else:
#             return make_response(jsonify([]), 200)
class RentsByUserId(Resource):
    def get(self, user_id):
        rents = Rent.query.filter(Rent.user_id == user_id).all()
        if rents:
            # Include car details in the response
            return make_response(jsonify([
                {
                    "id": rent.id,
                    "user_id": rent.user_id,
                    "car_id": rent.car_id,
                    "pickup_location": rent.pickup_location,
                    "dropoff_location": rent.dropoff_location,
                    "duration": rent.duration,
                    "car": {
                        "id": rent.car.id,
                        "name": rent.car.name,
                        "price": rent.car.price,
                        "image_url": rent.car.image_url,
                        "type": rent.car.type,
                        "seats": rent.car.seats,
                        "fuel_type": rent.car.fuel_type,
                        "transmission": rent.car.transmission,
                    }
                } for rent in rents
            ]), 200)
        else:
            return make_response(jsonify([]), 200)
        
api.add_resource(RentsByUserId, "/rents/user/<int:user_id>")







if __name__ == "__main__":
    app.run(debug=True)







