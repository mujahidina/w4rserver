# from app import db, app
# from models import Car

# def seed_data():
#     with app.app_context():

#         print('Deleting existing cars...')
#         Car.query.delete()

#         print('Creating cars...')
        
#         user_id = 1  

#         # SUV cars
#         suv1 = Car(name='Toyota RAV4', price=300, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQneQP6onwUiYbqsF9BnTDVbrjFBJHXL91iGQ&s', type='SUV', is_available=True, user_id=user_id)
#         suv2 = Car(name='Honda CR-V', price=320, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqcm-gWcgoSzldNdRG6yWtdacQtoEkoGrn5A&s', type='SUV', is_available=True, user_id=user_id)
#         suv3 = Car(name='Ford Escape', price=310, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-zCLwSHg2bspCcVUfCAJa208U8rD5FFfJXg&s', type='SUV', is_available=True, user_id=user_id)
#         suv4 = Car(name='Chevrolet Equinox', price=350, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRum5hbuwxzz8SVAsdOVYlVuT2DYSaPRbD00A&s', type='SUV', is_available=True, user_id=user_id)
#         suv5 = Car(name='Nissan Rogue', price=340, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYOOmUMYnUAijSu7mMvZzAe4KwgyLC6wN9VA&s', type='SUV', is_available=True, user_id=user_id)
#         suv6 = Car(name='Mazda CX-5', price=330, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyHgDNQBbCcZg-gigVR-M_O7NxzAikST_s4w&s', type='SUV', is_available=True, user_id=user_id)
#         suv7 = Car(name='Hyundai Tucson', price=315, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3dL5iP1WAiNxF62x0FseD-MS5Ifm-jmmA4w&s', type='SUV', is_available=True, user_id=user_id)
#         suv8 = Car(name='Subaru Forester', price=325, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQx5hQC18QnIb6pHkim5fsohFads9F3yFriJg&s', type='SUV', is_available=True, user_id=user_id)
#         suv9 = Car(name='Kia Sportage', price=345, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBSkdswmX9zLoO6kehiftt5_Uxgl6lvgw2Zw&s', type='SUV', is_available=True, user_id=user_id)
#         suv10 = Car(name='BMW X5-', price=600, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8Hmek5zmSRAF1ita-6RSGNjLaE68GOXu8KA&s', type='SUV', is_available=True, user_id=user_id)
#         suv11 = Car(name='Audi Q5', price=650, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNTYLxVgFl9n8H4F3-AOh4x07n3YzQJXzhgg&s', type='SUV', is_available=True, user_id=user_id)

#         # Hatchback cars
#         hatchback1 = Car(name='Volkswagen Golf', price=250, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT__StcQ78exUKHzniC-oaWNEVX5pLS5uPiBw&s', type='Hatchback', is_available=True, user_id=user_id)
#         hatchback2 = Car(name='Honda Fit', price=220, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGJ1HlFFEmCTLhaGIupFBTfYCtJt6QC6QV8A&s', type='Hatchback', is_available=True, user_id=user_id)
#         hatchback3 = Car(name='Ford Fiesta', price=210, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu08XTUUCQJwWcvOARzSe7O9sE74Rhs_gn-A&s', type='Hatchback', is_available=True, user_id=user_id)
#         hatchback4 = Car(name='Toyota Yaris', price=230, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzyW7srRlNwnuDkoCIpbPXzgMpWNLiQfylLg&s', type='Hatchback', is_available=True, user_id=user_id)
#         hatchback5 = Car(name='Chevrolet Spark', price=200, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLRzjDXwjlXT7WtzQP0xLC8RgKY3ZOJkHxBw&s', type='Hatchback', is_available=True, user_id=user_id)
#         hatchback6 = Car(name='Hyundai Elantra GT', price=240, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtduBmn0batcDHqba7fGscz4QCuC6H4QsnIw&s', type='Hatchback', is_available=True, user_id=user_id)
#         hatchback7 = Car(name='Mazda3 Hatchback', price=270, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZmvwYpy11E_WgR0BXg4QoFIRo-07YwftsqA&s', type='Hatchback', is_available=True, user_id=user_id)
#         hatchback8 = Car(name='Kia Rio', price=220, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_H3OsKMCII4J7hGnaBvQpnDn7q320bVuvBA&s', type='Hatchback', is_available=True, user_id=user_id)
#         hatchback9 = Car(name='Nissan Versa', price=210, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlUtkSLIph3JtjokElVCq5WEADUUSi5h-3sw&s', type='Hatchback', is_available=True, user_id=user_id)

#         # Pickup cars
#         pickup1 = Car(name='Ford F-150', price=400, image_url='https://img.freepik.com/free-psd/view-crossroad-car_23-2151780818.jpg?t=st=1737031551~exp=1737035151~hmac=618a56dbe5fea0ac82f236bc45fa0d73a2aed70d318e41def1f37ff82eb912eb&w=900', type='Pickup', is_available=True, user_id=user_id)
#         pickup2 = Car(name='Chevrolet Silverado', price=450, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7rkK0VeDjG25P5e_cavx-eYfTsa6-xiYWaw&s', type='Pickup', is_available=True, user_id=user_id)
#         pickup3 = Car(name='Ram 1500', price=460, image_url='https://img.freepik.com/premium-photo/close-up-silver-ram-truck-white-background-generative-ai_927978-85662.jpg?ga=GA1.1.1686556981.1737030429&semt=ais_hybrid', type='Pickup', is_available=True, user_id=user_id)
#         pickup4 = Car(name='Toyota Tundra', price=480, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOdtYh4Lnaxnqm4shhNWelNaNKl2efrQPAVA&s', type='Pickup', is_available=True, user_id=user_id)
#         pickup7 = Car(name='Honda Ridgeline', price=420, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQu6F687049MMY7yl7cKoKNT9yQjXqv_DZoQ&s', type='Pickup', is_available=True, user_id=user_id)
#         pickup9 = Car(name='Chevrolet Colorado', price=440, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdJcJPDCvRmVkVqVXnDLJ8idM0WY66gPlyog&s', type='Pickup', is_available=True, user_id=user_id)
#         pickup10 = Car(name='Toyota Tacoma', price=450, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxXgG7Cb_kgCpfVMmp7hrCT2zGMsD2LnQiqA&s', type='Pickup', is_available=True, user_id=user_id)
#         pickup11 = Car(name='Ram 2500', price=510, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQbYr6BhfGSq_YJ-G_GG1NNIp3Gg69m3mVNQ&s', type='Pickup', is_available=True, user_id=user_id)
#         pickup12 = Car(name='Nissan Frontier', price=460, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8yhOqJrmD6W7b_1he7Z0Zk0jnw7fLFMecHw&s', type='Pickup', is_available=True, user_id=user_id)
#         pickup13 = Car(name='Ford Super Duty F-350', price=550, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTpyMj6E3CGbjd3jU-MJYge_MzWpHvgmUyhA&s', type='Pickup', is_available=True, user_id=user_id)

        
     
#         # Sedan cars
#         sedan1 = Car(name='Toyota Camry', price=300, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVcPhd3F31GY-9146zX8dIxKD5IOjMNprRZQ&s', type='Sedan', is_available=True, user_id=user_id)
#         sedan2 = Car(name='Honda Accord', price=320, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd6tzVfDfzV3diVr4-UHU7PnvayFyacLcq-A&s', type='Sedan', is_available=True, user_id=user_id)
#         sedan3 = Car(name='BMW 3 Series', price=450, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS28QyiUIyMA_qjC8IECVJGnrsMhMtrxzBEMg&s', type='Sedan', is_available=True, user_id=user_id)
#         sedan4 = Car(name='Mercedes-Benz C-Class', price=500, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScMv9fyuoxVD1bSpLVPYlg4mCITSF-zjPFZw&s', type='Sedan', is_available=True, user_id=user_id)
#         sedan5 = Car(name='Audi A4', price=480, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtzsY0iTU0Zn7sVDS2VJoC4UzW5zT_oyXzmQ&s', type='Sedan', is_available=True, user_id=user_id)
#         sedan6 = Car(name='Ford Fusion', price=330, image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlpwUTd0jrwyAqfTi25W9ieuFCbMsYpd5OYg&s', type='Sedan', is_available=True, user_id=user_id)

        
     
#         cars = [
#             suv1, suv2, suv3, suv4, suv5, suv6, suv7, suv8, suv9, suv10, suv11, 
#             sedan1, sedan2, sedan3, sedan4, sedan5, sedan6,
#             pickup1, pickup2, pickup3, pickup4, pickup7, pickup9, pickup10, pickup11, pickup12, pickup13,
#             hatchback1, hatchback2, hatchback3, hatchback4, hatchback5, hatchback6, hatchback7, hatchback8, hatchback9
#         ]

#         db.session.add_all(cars)
#         db.session.commit()

#         print('Successfully created cars')

# if __name__ == '__main__':
#     seed_data()






from app import db, app
from models import Car



def seed_data():
    with app.app_context():

        print('Deleting existing cars...')
        Car.query.delete()

        print('Creating cars...')
        
        user_id = 1  # 

        # SUV cars
        suv1 = Car(
            name='Toyota RAV4', 
            price=300, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQneQP6onwUiYbqsF9BnTDVbrjFBJHXL91iGQ&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        suv2 = Car(
            name='Honda CR-V', 
            price=320, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqcm-gWcgoSzldNdRG6yWtdacQtoEkoGrn5A&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Hybrid', 
            seats=5, 
            transmission='CVT'
        )
        suv3 = Car(
            name='Ford Escape', 
            price=310, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-zCLwSHg2bspCcVUfCAJa208U8rD5FFfJXg&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        suv4 = Car(
            name='Chevrolet Equinox', 
            price=350, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRum5hbuwxzz8SVAsdOVYlVuT2DYSaPRbD00A&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        suv5 = Car(
            name='Nissan Rogue', 
            price=340, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYOOmUMYnUAijSu7mMvZzAe4KwgyLC6wN9VA&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        suv6 = Car(
            name='Mazda CX-5', 
            price=330, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyHgDNQBbCcZg-gigVR-M_O7NxzAikST_s4w&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        suv7 = Car(
            name='Hyundai Tucson', 
            price=315, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3dL5iP1WAiNxF62x0FseD-MS5Ifm-jmmA4w&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        suv8 = Car(
            name='Subaru Forester', 
            price=325, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQx5hQC18QnIb6pHkim5fsohFads9F3yFriJg&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='CVT'
        )
        suv9 = Car(
            name='Kia Sportage', 
            price=345, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBSkdswmX9zLoO6kehiftt5_Uxgl6lvgw2Zw&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        suv10 = Car(
            name='BMW X5', 
            price=600, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8Hmek5zmSRAF1ita-6RSGNjLaE68GOXu8KA&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        suv11 = Car(
            name='Audi Q5', 
            price=650, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNTYLxVgFl9n8H4F3-AOh4x07n3YzQJXzhgg&s', 
            type='SUV', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Diesel', 
            seats=5, 
            transmission='Automatic'
        )

        # Hatchback cars
        hatchback1 = Car(
            name='Volkswagen Golf', 
            price=250, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT__StcQ78exUKHzniC-oaWNEVX5pLS5uPiBw&s', 
            type='Hatchback', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Manual'
        )
        hatchback2 = Car(
            name='Honda Fit', 
            price=220, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGJ1HlFFEmCTLhaGIupFBTfYCtJt6QC6QV8A&s', 
            type='Hatchback', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        hatchback3 = Car(
            name='Ford Fiesta', 
            price=210, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu08XTUUCQJwWcvOARzSe7O9sE74Rhs_gn-A&s', 
            type='Hatchback', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Manual'
        )
        hatchback4 = Car(
            name='Toyota Yaris', 
            price=230, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzyW7srRlNwnuDkoCIpbPXzgMpWNLiQfylLg&s', 
            type='Hatchback', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        hatchback5 = Car(
            name='Chevrolet Spark', 
            price=200, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLRzjDXwjlXT7WtzQP0xLC8RgKY3ZOJkHxBw&s', 
            type='Hatchback', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=4, 
            transmission='Automatic'
        )
        hatchback6 = Car(
            name='Hyundai Elantra GT', 
            price=240, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtduBmn0batcDHqba7fGscz4QCuC6H4QsnIw&s', 
            type='Hatchback', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        hatchback7 = Car(
            name='Mazda3 Hatchback', 
            price=270, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZmvwYpy11E_WgR0BXg4QoFIRo-07YwftsqA&s', 
            type='Hatchback', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        hatchback8 = Car(
            name='Kia Rio', 
            price=220, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_H3OsKMCII4J7hGnaBvQpnDn7q320bVuvBA&s', 
            type='Hatchback', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Manual'
        )
        hatchback9 = Car(
            name='Nissan Versa', 
            price=210, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlUtkSLIph3JtjokElVCq5WEADUUSi5h-3sw&s', 
            type='Hatchback', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Manual'
        )

        # Pickup cars
        pickup1 = Car(
            name='Ford F-150', 
            price=400, 
            image_url='https://img.freepik.com/free-psd/view-crossroad-car_23-2151780818.jpg?t=st=1737031551~exp=1737035151~hmac=618a56dbe5fea0ac82f236bc45fa0d73a2aed70d318e41def1f37ff82eb912eb&w=900', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=6, 
            transmission='Automatic'
        )
        pickup2 = Car(
            name='Chevrolet Silverado', 
            price=450, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7rkK0VeDjG25P5e_cavx-eYfTsa6-xiYWaw&s', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Diesel', 
            seats=5, 
            transmission='Manual'
        )
        pickup3 = Car(
            name='Ram 1500', 
            price=460, 
            image_url='https://img.freepik.com/premium-photo/close-up-silver-ram-truck-white-background-generative-ai_927978-85662.jpg?ga=GA1.1.1686556981.1737030429&semt=ais_hybrid', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        pickup4 = Car(
            name='Toyota Tundra', 
            price=480, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOdtYh4Lnaxnqm4shhNWelNaNKl2efrQPAVA&s', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        pickup7 = Car(
            name='Honda Ridgeline', 
            price=420, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQu6F687049MMY7yl7cKoKNT9yQjXqv_DZoQ&s', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        pickup9 = Car(
            name='Chevrolet Colorado', 
            price=440, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdJcJPDCvRmVkVqVXnDLJ8idM0WY66gPlyog&s', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Manual'
        )
        pickup10 = Car(
            name='Toyota Tacoma', 
            price=450, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxXgG7Cb_kgCpfVMmp7hrCT2zGMsD2LnQiqA&s', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        pickup11 = Car(
            name='Ram 2500', 
            price=510, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQbYr6BhfGSq_YJ-G_GG1NNIp3Gg69m3mVNQ&s', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Diesel', 
            seats=5, 
            transmission='Automatic'
        )
        pickup12 = Car(
            name='Nissan Frontier', 
            price=460, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8yhOqJrmD6W7b_1he7Z0Zk0jnw7fLFMecHw&s', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        pickup13 = Car(
            name='Ford Super Duty F-350', 
            price=550, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTpyMj6E3CGbjd3jU-MJYge_MzWpHvgmUyhA&s', 
            type='Pickup', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Diesel', 
            seats=5, 
            transmission='Automatic'
        )

        # Sedan cars
        sedan1 = Car(
            name='Toyota Camry', 
            price=300, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVcPhd3F31GY-9146zX8dIxKD5IOjMNprRZQ&s', 
            type='Sedan', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        sedan2 = Car(
            name='Honda Accord', 
            price=320, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd6tzVfDfzV3diVr4-UHU7PnvayFyacLcq-A&s', 
            type='Sedan', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Hybrid', 
            seats=5, 
            transmission='CVT'
        )
        sedan3 = Car(
            name='BMW 3 Series', 
            price=350, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTy11UO5ZbApOBGQjFkCKh-LS6snRiv6hnz9Q&s', 
            type='Sedan', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        sedan4 = Car(
            name='Audi A4', 
            price=400, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRL_wLtPA5a2eAiPtkV6mT7jwFuq2TxTvbScA&s', 
            type='Sedan', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        sedan5 = Car(
            name='Mercedes-Benz C-Class', 
            price=450, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRypsFa6oF4K0Ot7InyiMmWz9t2k4F7po4mSQ&s', 
            type='Sedan', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )
        sedan6 = Car(
            name='Lexus IS', 
            price=470, 
            image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpXIJTcnre-N6trWSHM-5vzb-nNF-BGmEmdQ&s', 
            type='Sedan', 
            is_available=True, 
            user_id=user_id,
            fuel_type='Gasoline', 
            seats=5, 
            transmission='Automatic'
        )

        cars = [
            suv1, suv2, suv3, suv4, suv5, suv6, suv7, suv8, suv9, suv10, suv11,
            hatchback1, hatchback2, hatchback3, hatchback4, hatchback5, hatchback6, hatchback7, hatchback8, hatchback9,
            pickup1, pickup2, pickup3, pickup4, pickup7, pickup9, pickup10, pickup11, pickup12, pickup13,
            sedan1, sedan2, sedan3, sedan4, sedan5, sedan6
        ]

        db.session.add_all(cars)
        db.session.commit()

        print('Successfully created cars')

if __name__ == '__main__':
    seed_data()



