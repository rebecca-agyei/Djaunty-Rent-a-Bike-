# Djaunty-Rent-a-Bike-
Django Models and Databases Project


# Populating Database and Running Queries

python3 manage.py shell or python manage.py shell(for windows)

from BikeRentalApp.models import Bike, Renter, Rental

## Creating Bike Instances

bike1 = Bike(bike_type="ST", color="black")

bike1.save()

bike2 = Bike(bike_type="TA", color="green")

bike2.save()

bike3 = Bike(bike_type="EL", color="white")

bike3.save()

bike4 = Bike(bike_type="EL", color="red")

bike4.save()

bike5 = Bike(bike_type="TA", color="blue")

bike5.save()

## Creating Renter Instances

renter1 = Renter(first_name="John", last_name="Boo", phone="0236985471", vip_num=2)

renter1.save()

renter2 = Renter(first_name="Beck", last_name="Sam", phone="0243110022", vip_num=4)

renter2.save()

renter3 = Renter(first_name="Lee", last_name="Shim", phone="050698521")

renter3.save()

first_bike = Bike.objects.first()

last_bike = Bike.objects.last()

first_renter = Renter.objects.first()

last_renter = Renter.objects.last()

## Creating Rental Instances

rental1 = Rental(bike=last_bike, renter=first_renter)

rental1.save()

rental2 = Rental(bike=first_bike, renter=last_renter)

rental2.save()
