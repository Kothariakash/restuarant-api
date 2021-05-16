# restaurant-api 
An api, that help a restaurant with sort orders of food for tables.     This api should have :  
·      Ability to place orders  
·      Ability to provide menu  
·      Book tables  
·      Find out booked tables   

## Installation
Before we begin, kindly install following on your system:-

python.x

Virtualenv
## How to Run the App?

cd path/to/workspace

python -m venv env

env/Scripts/activate

pip install -r requirements.txt

python manage.py runserver

Everything should be ready. In your browser open http://127.0.0.1:8000/



## Endpoints -
### API 1 - Getting the Menu of the restaurant
### http://127.0.0.1:8000/api/v1.0/menu/ 
![menu_api](https://user-images.githubusercontent.com/53464861/118398485-82b18400-b676-11eb-85de-38975418369e.JPG)

### API 2 - Getting Restuarant Table details
### http://127.0.0.1:8000/api/v1.0/tabledetails/
![table-details-api](https://user-images.githubusercontent.com/53464861/118398566-d4f2a500-b676-11eb-8194-d99e95234078.JPG)

### API 3 - Booking Table
### http://127.0.0.1:8000/api/v1.0/booktable/
![table-booking](https://user-images.githubusercontent.com/53464861/118398634-197e4080-b677-11eb-8c7d-2f1ec2653880.JPG)

![table-booking-result](https://user-images.githubusercontent.com/53464861/118398648-26029900-b677-11eb-8680-64a282a1b65a.JPG)

### API 4 - Booking food order
### http://127.0.0.1:8000/api/v1.0/orderfood/
![order-food](https://user-images.githubusercontent.com/53464861/118398675-51858380-b677-11eb-89d4-b12df1c0bd45.JPG)

![order-food-result](https://user-images.githubusercontent.com/53464861/118398696-66621700-b677-11eb-8026-d69fa21535ad.JPG)


### Test case
![Test cases](https://user-images.githubusercontent.com/53464861/118398744-a1fce100-b677-11eb-8bbe-deac9511433b.JPG)
