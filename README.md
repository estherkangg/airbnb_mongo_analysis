# AirBnB MongoDB Analysis  
  
## Data Set Details:  
The data set I am working with for this assignment comes from Airbnb's public data [records](http://insideairbnb.com/get-the-data/). I chose one of my favorite cities, Amsterdam, to analyze the Airbnb listings data for March 9, 2023.  
The format for the original data file was a compressed CSV file that I then decompressed and munged to a clean CSV file.  
  
Here are the first 20 rows of the ***raw*** data:  
  

|id                |listing_url                                    |scrape_id     |last_scraped|source         |name                         |description                                                                        |neighborhood_overview        |picture_url                                                                                                                   |host_id  |host_url                                   |host_name                        |host_since|host_location                          |host_about   |host_response_time|host_response_rate|host_acceptance_rate|host_is_superhost|host_thumbnail_url                                                                                        |host_picture_url                                                                                             |host_neighbourhood                 |host_listings_count|host_total_listings_count|host_verifications                |host_has_profile_pic|host_identity_verified|neighbourhood                                              |neighbourhood_cleansed                |neighbourhood_group_cleansed|latitude          |longitude         |property_type                     |room_type      |accommodates|bathrooms|bathrooms_text   |bedrooms|beds|amenities     |price    |minimum_nights|maximum_nights|minimum_minimum_nights|maximum_minimum_nights|minimum_maximum_nights|maximum_maximum_nights|minimum_nights_avg_ntm|maximum_nights_avg_ntm|calendar_updated|has_availability|availability_30|availability_60|availability_90|availability_365|calendar_last_scraped|number_of_reviews|number_of_reviews_ltm|number_of_reviews_l30d|first_review|last_review|review_scores_rating|review_scores_accuracy|review_scores_cleanliness|review_scores_checkin|review_scores_communication|review_scores_location|review_scores_value|license                 |instant_bookable|calculated_host_listings_count|calculated_host_listings_count_entire_homes|calculated_host_listings_count_private_rooms|calculated_host_listings_count_shared_rooms|reviews_per_month|
|------------------|-----------------------------------------------|--------------|------------|---------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------|-------------------------------------------|---------------------------------|----------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------|--------------------|-----------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------|-------------------|-------------------------|----------------------------------|--------------------|----------------------|-----------------------------------------------------------|--------------------------------------|----------------------------|------------------|------------------|----------------------------------|---------------|------------|---------|-----------------|--------|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------------|--------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------|----------------|---------------|---------------|---------------|----------------|---------------------|-----------------|---------------------|----------------------|------------|-----------|--------------------|----------------------|-------------------------|---------------------|---------------------------|----------------------|-------------------|------------------------|----------------|------------------------------|-------------------------------------------|--------------------------------------------|-------------------------------------------|-----------------|
|2818              |https://www.airbnb.com/rooms/2818              |20230309202119|2023-03-09  |city scrape    |Quiet Garden View Room & Super Fast Wi-Fi                                  |Quiet Garden View Room...        |Indische Buurt...   |https://a0.muscache.com/pictures/10272854/8dcca016_original.jpg                                                               |3159     |https://www.airbnb.com/users/show/3159     |Daniel                           |2008-09-24|Amsterdam, Netherlands                 |Upon arriving...                                                                            |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/users/3159/profile_pic/1259095323/original.jpg?aki_policy=profile_small        |https://a0.muscache.com/im/users/3159/profile_pic/1259095323/original.jpg?aki_policy=profile_x_medium        |Indische Buurt   |1                  |1                        |['email', 'phone']                |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Oostelijk Havengebied - Indische Buurt|                            |52.36435          |4.94358           |Private room in rental unit       |Private room   |2           |         |1.5 shared baths |1       |2   |["Drying rack...  |$69.00   |3             |28            |3                     |5                     |10                    |1125                  |3.0                   |1094.7                |                |t               |4              |8              |18             |44              |2023-03-09           |322              |37                   |3                     |2009-03-30  |2023-02-28 |4.89                |4.93                  |4.99                     |4.97                 |4.98                       |4.69                  |4.81               |0363 5F3A 5684 6750 D14D|f               |1                             |0                                          |1                                           |0                                          |1.90             |
|311124            |https://www.airbnb.com/rooms/311124            |20230309202119|2023-03-10  |city scrape    |*historic centre* *bright* *canal view* *jordaan*  |> Please be...    |Perfect location in the lively centre. All historic high lights, shopping, eating and drinking out options in walking distance.  |https://a0.muscache.com/pictures/5208672/5bb6091f_original.jpg                                                                |1600010  |https://www.airbnb.com/users/show/1600010  |Anke & Robert                    |2012-01-12|Amsterdam, Netherlands                 |We love cycling...           |within a few hours|100%              |68%                 |f                |https://a0.muscache.com/im/users/1600010/profile_pic/1364046747/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1600010/profile_pic/1364046747/original.jpg?aki_policy=profile_x_medium     |Jordaan                            |1                  |1                        |['email', 'phone', 'work_email']  |t                   |f                     |Amsterdam, North Holland, Netherlands                      |Centrum-West                          |                            |52.37104          |4.87713           |Entire rental unit                |Entire home/apt|2           |         |1 bath           |1       |1   |["Drying rack... |$325.00  |5             |15            |5                     |5                     |8                     |8                     |5.0                   |8.0                   |                |t               |23             |41             |71             |346             |2023-03-10           |87               |3                    |0                     |2012-05-01  |2023-01-01 |4.76                |4.72                  |4.79                     |4.9                  |4.92                       |4.93                  |4.6                |0363 59D8 7D30 6CFA DC81|f               |1                             |1                                          |0                                           |0                                          |0.66             |
|319985            |https://www.airbnb.com/rooms/319985            |20230309202119|2023-03-10  |city scrape    |Elegant Appartement Central Location.                                      |From December 26...    |Bij aankomst vertel ik mijn gasten graag over de omgeving.                                   |https://a0.muscache.com/pictures/3b76222e-ed0a-4a78-8b8a-c64f19fa00c4.jpg                                                     |1640702  |https://www.airbnb.com/users/show/1640702  |J                                |2012-01-23|Amsterdam, Netherlands                 |I like to welcome guests who take good care of my property, and inform them about Amsterdam.  |within a day      |93%               |89%                 |t                |https://a0.muscache.com/im/pictures/user/0564f251-382c-44a0-bd2d-ce009ad22357.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/0564f251-382c-44a0-bd2d-ce009ad22357.jpg?aki_policy=profile_x_medium|De Pijp                            |2                  |3                        |['email', 'phone']                |t                   |t                     |De Pijp, North Holland, Netherlands                        |De Pijp - Rivierenbuurt               |                            |52.35669          |4.90187           |Entire rental unit                |Entire home/apt|4           |         |1 bath           |1       |2   |["Building staff"...       |$244.00  |1             |90            |1                     |2                     |90                    |90                    |1.3                   |90.0                  |                |t               |8              |13             |32             |41              |2023-03-10           |492              |88                   |5                     |2012-05-06  |2023-02-21 |4.75                |4.83                  |4.69                     |4.86                 |4.78                       |4.85                  |4.62               |0363 7D88 E1E8 F521 9A10|f               |2                             |1                                          |1                                           |0                                          |3.73             |
|327285            |https://www.airbnb.com/rooms/327285            |20230309202119|2023-03-10  |city scrape    |beautiful designed ap.+bikes+garden         |Cosy and comfortable...       |'De Pijp'... |https://a0.muscache.com/pictures/4283713/63eaa97f_original.jpg                                                                |1672823  |https://www.airbnb.com/users/show/1672823  |Ester                            |2012-01-30|Amsterdam, Netherlands                 |We are the...   |within an hour    |100%              |100%                |f                |https://a0.muscache.com/im/pictures/user/cf563489-9f1e-44c1-9377-a9996eaed3ac.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/cf563489-9f1e-44c1-9377-a9996eaed3ac.jpg?aki_policy=profile_x_medium|De Pijp                            |3                  |4                        |['phone']                         |t                   |t                     |Amsterdam, North Holland, Netherlands                      |De Pijp - Rivierenbuurt               |                            |52.35625          |4.89323           |Private room in home              |Private room   |4           |         |1.5 baths        |1       |6   |["Board games"...    |$244.00  |2             |30            |1                     |5                     |30                    |30                    |2.7                   |30.0                  |                |t               |1              |3              |5              |13              |2023-03-10           |561              |26                   |8                     |2012-03-12  |2023-03-04 |4.94                |4.91                  |4.92                     |4.98                 |4.99                       |4.91                  |4.84               |0363 8A88 B129 62B5 BD4E|t               |2                             |0                                          |2                                           |0                                          |4.19             |
|331946            |https://www.airbnb.com/rooms/331946            |20230309202119|2023-03-10  |previous scrape|Lovely FAMILY house near Vondelpark                                        |* Our house...  |                                                                 |https://a0.muscache.com/pictures/b73c16af-4e31-4b61-a948-4a68cdfe3501.jpg                                                     |1687595  |https://www.airbnb.com/users/show/1687595  |Sebastiaan                       |2012-02-02|Amsterdam, Netherlands                 |Welcome guests...  |https://a0.muscache.com/im/users/1687595/profile_pic/1328270894/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1687595/profile_pic/1328270894/original.jpg?aki_policy=profile_x_medium     |Oud-West                           |1                  |1                        |['email', 'phone']                |t                   |t                     |                                                           |De Baarsjes - Oud-West                |                            |52.3606           |4.85739           |Entire loft                       |Entire home/apt|4           |         |1 bath           |4       |4   |["Host greets... |$220.00  |2             |14            |2                     |2                     |14                    |14                    |2.0                   |14.0                  |                |t               |0              |0              |0              |0               |2023-03-10           |27               |0                    |0                     |2013-10-21  |2019-07-21 |4.88                |4.88                  |4.64                     |4.92                 |4.88                       |4.79                  |4.75               |0363 A942 21DC C431 1AD1|f               |1                             |1                                          |0                                           |0                                          |0.24             |
|343094            |https://www.airbnb.com/rooms/343094            |20230309202119|2023-03-09  |city scrape    |Amstel Nest - an urban retreat for two                                     |Amstel Nest...     |From our place...  |https://a0.muscache.com/pictures/4703255/285aabad_original.jpg                                                                |1740785  |https://www.airbnb.com/users/show/1740785  |Rob & Fang                       |2012-02-12|Amsterdam, Netherlands                 |We are...  |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/pictures/user/1b70958a-abe7-47f8-995c-391afcea7310.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/1b70958a-abe7-47f8-995c-391afcea7310.jpg?aki_policy=profile_x_medium|Oosterparkbuurt                    |1                  |3                        |['email', 'phone']                |t                   |t                     |Watergraafsmeer, North Holland, Netherlands                |Oud-Oost                              |                            |52.35715          |4.90926           |Private room in townhouse         |Private room   |2           |         |1 private bath   |1       |1   |["Lock on...   |$108.00  |3             |30            |1                     |7                     |4                     |1125                  |3.8                   |816.6                 |                |t               |1              |1              |7              |116             |2023-03-09           |462              |56                   |2                     |2012-05-02  |2023-02-20 |4.89                |4.88                  |4.88                     |4.97                 |4.97                       |4.88                  |4.74               |0363 FC71 F7DB 3AB4 3C42|t               |1                             |0                                          |1                                           |0                                          |3.50             |
|20168             |https://www.airbnb.com/rooms/20168             |20230309202119|2023-03-10  |previous scrape|Studio with...        |Located just...    |https://a0.muscache.com/pictures/69979628/fd6a3a80_original.jpg                                                               |59484    |https://www.airbnb.com/users/show/59484    |Alexander                        |2009-12-02|Amsterdam, Netherlands                 |+ (Phone number hidden by Airbnb)                                                                           |within an hour    |100%              |98%                 |f                |https://a0.muscache.com/im/pictures/user/65092142-62d7-48a9-9479-ad5a24d99a77.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/65092142-62d7-48a9-9479-ad5a24d99a77.jpg?aki_policy=profile_x_medium|Grachtengordel                     |5                  |5                        |['email', 'phone']                |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Centrum-Oost                          |                            |52.36407          |4.89393           |Private room in townhouse         |Private room   |2           |         |1 private bath   |1       |1   |["Carbon monoxide alarm", "Host greets you", "Wifi", "Long term stays allowed", "Hangers", "TV", "Paid parking off premises", "Refrigerator", "Free street parking", "Hair dryer", "Hot water", "Heating", "Bed linens", "Fire extinguisher", "Essentials", "Smoke alarm"]   |$106.00  |1             |365           |1                     |1                     |1125                  |1125                  |1.0                   |1125.0                |                |t               |0              |0              |0              |0               |2023-03-10           |339              |0                    |0                     |2010-03-02  |2020-04-09 |4.44                |4.69                  |4.79                     |4.63                 |4.62                       |4.87                  |4.49               |0363 CBB3 2C10 0C2A 1E29|t               |2                             |0                                          |2                                           |0                                          |2.14             |
|350271            |https://www.airbnb.com/rooms/350271            |20230309202119|2023-03-10  |previous scrape|Luxe boat AMSTERDAM IJBURG!!!    |28 december 2016...             |The boat is...   |https://a0.muscache.com/pictures/63320748/1c472b04_original.jpg       |1775032  |https://www.airbnb.com/users/show/1775032  |Agustina                         |2012-02-19|Amsterdam, Netherlands                 |Welcome to...  |N/A               |N/A               |50%                 |f                |https://a0.muscache.com/im/users/1775032/profile_pic/1329676993/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1775032/profile_pic/1329676993/original.jpg?aki_policy=profile_x_medium     |Oost                               |1                  |3                        |['email', 'phone']                |t                   |t                     |Amsterdam, Noord-Holland, Netherlands                      |IJburg - Zeeburgereiland              |                            |52.36129          |4.98845           |Boat                              |Entire home/apt|4           |         |1 bath           |3       |3   |["Host greets you"...    |$395.00  |7             |365           |7                     |7                     |365                   |365                   |7.0                   |365.0                 |                |t               |0              |0              |0              |0               |2023-03-10           |4                |1                    |0                     |2015-07-29  |2022-08-15 |4.33                |5.0                   |4.67                     |5.0                  |5.0                        |5.0                   |4.33               |0363 6334 AD6B 47DF B32A|f               |1                             |1                                          |0                                           |0                                          |0.04             |
|357980            |https://www.airbnb.com/rooms/357980            |20230309202119|2023-03-10  |city scrape    |★ STYLISH FAMILY HOME - CITY CENTER                                        |Welcome to...      |THE NEIGHBORHOOD:... |https://a0.muscache.com/pictures/miso/Hosting-357980/original/3e3a9a36-afd3-4f4d-853b-afd82e3e7e16.jpeg                       |1811745  |https://www.airbnb.com/users/show/1811745  |Marre    |2012-02-26|Amsterdam, Netherlands    |I am a...    |within a few hours|100%              |54%                 |f                |https://a0.muscache.com/im/pictures/user/0d48c5ff-55bd-4d42-b452-9b73528b1d54.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/0d48c5ff-55bd-4d42-b452-9b73528b1d54.jpg?aki_policy=profile_x_medium|Oud-West                           |1                  |1                        |['email', 'phone', 'work_email']  |t                   |t                     |Amsterdam, North Holland, Netherlands                      |De Baarsjes - Oud-West                |                            |52.36348          |4.87648           |Entire townhouse                  |Entire home/apt|4           |         |1.5 baths        |4       |4   |["Board games"...     |$245.00  |2             |1125          |2                     |2                     |1125                  |1125                  |2.0                   |1125.0                |                |t               |1              |1              |1              |17              |2023-03-10           |121              |24                   |2                     |2012-04-12  |2023-03-03 |4.88                |4.89                  |4.83                     |4.93                 |4.97                       |4.95                  |4.75               |0363 799F 0610 C059 F9F4|f               |1                             |1                                          |0                                           |0                                          |0.91             |
|366438            |https://www.airbnb.com/rooms/366438            |20230309202119|2023-03-09  |city scrape    |Amsterdam@ city centre & canal view                                        |Your own apartment...    |https://a0.muscache.com/pictures/7cc382a6-37ee-446a-a16f-769dce0498fd.jpg                                                     |1849988  |https://www.airbnb.com/users/show/1849988  |Nicolet                          |2012-03-03|Amsterdam, Netherlands                 |Hai,  I am Nicolette...    |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/users/1849988/profile_pic/1333540992/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1849988/profile_pic/1333540992/original.jpg?aki_policy=profile_x_medium     |Amsterdam Centrum                  |1                  |2                        |['email', 'phone']                |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Centrum-Oost                          |                            |52.367377549542454|4.896707133551012 |Private room in condo             |Private room   |2           |         |1.5 baths        |1       |1   |["Board games"...  |$170.00  |3             |60            |2                     |3                     |60                    |60                    |2.8                   |60.0                  |                |t               |12             |14             |22             |162             |2023-03-09           |463              |42                   |2                     |2012-04-10  |2023-02-26 |4.74                |4.82                  |4.74                     |4.84                 |4.88                       |4.92                  |4.63               |0363 BD40 0F80 50E7 8478|f               |1                             |0              |1          |0           |3.48             |
|367107            |https://www.airbnb.com/rooms/367107            |20230309202119|2023-03-10  |city scrape    |IN HISTORIC CENTRE, NEXT TO AMSTEL, PEACEFUL HOME                          |HIGHLIGHTS:...  |https://a0.muscache.com/pictures/fea384a1-134b-4d53-8129-e306fc15dbfb.jpg                                                     |1853421  |https://www.airbnb.com/users/show/1853421  |Marijn                           |2012-03-04|Amsterdam, Netherlands                 |Hi, I am Marijn...       |within a day      |89%               |29%                 |f                |https://a0.muscache.com/im/users/1853421/profile_pic/1330861212/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1853421/profile_pic/1330861212/original.jpg?aki_policy=profile_x_medium     |Grachtengordel                     |1                  |1                        |['email', 'phone']                |t                   |t                     |Amsterdam, Noord-Holland, Netherlands                      |Centrum-Oost                          |                            |52.36263          |4.90216           |Entire condo                      |Entire home/apt|2           |         |1.5 baths        |1       |1   |["Drying rack for clothing"...   |$214.00  |5             |30            |5                     |5                     |30                    |30                    |5.0                   |30.0                  |                |t               |13             |19             |28             |45              |2023-03-10           |15               |4                    |0                     |2015-07-18  |2022-10-18 |5.0                 |4.93                  |4.87                     |4.93                 |5.0                        |5.0                   |4.73               |0363 1761 5C93 2C93 93FE|f               |1                             |1                                          |0                                           |0                                          |0.16             |
|27886             |https://www.airbnb.com/rooms/27886             |20230309202119|2023-03-10  |city scrape    |Romantic, stylish...     |Central, quiet, safe, clean and beautiful.  |https://a0.muscache.com/pictures/02c2da9d-660e-451d-8a51-2f7a17469df7.jpg                                                     |97647    |https://www.airbnb.com/users/show/97647    |Flip                             |2010-03-23|Amsterdam, Netherlands                 |Marjan works...                           |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/users/97647/profile_pic/1273275077/original.jpg?aki_policy=profile_small       |https://a0.muscache.com/im/users/97647/profile_pic/1273275077/original.jpg?aki_policy=profile_x_medium       |Westelijke Eilanden                |1                  |1                        |['email', 'phone']                |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Centrum-West                          |                            |52.38761          |4.89188           |Private room in houseboat         |Private room   |2           |         |1.5 baths        |1       |1   |["Harbor view"...   |$143.00  |3             |356           |3                     |3                     |1125                  |1125                  |3.0                   |1125.0                |                |t               |0              |0              |0              |14              |2023-03-10           |248              |20                   |2                     |2012-01-09  |2023-02-26 |4.94                |4.92                  |4.95                     |4.95                 |4.92                       |4.89                  |4.79               |0363 974D 4986 7411 88D8|f               |1                             |0                                          |1                                           |0                                          |1.82             |
|28871             |https://www.airbnb.com/rooms/28871             |20230309202119|2023-03-10  |city scrape    |Comfortable double room    |In a monumental house...   |Flower market , Leidseplein , Rembrantsplein                                                                                         |https://a0.muscache.com/pictures/160889/362340f7_original.jpg                                                                 |124245   |https://www.airbnb.com/users/show/124245   |Edwin                            |2010-05-13|Amsterdam, Netherlands                 |Hi                                                                                           |within an hour    |100%              |99%                 |t                |https://a0.muscache.com/im/pictures/user/9986bbdb-632f-42b5-a866-8e3307184977.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/9986bbdb-632f-42b5-a866-8e3307184977.jpg?aki_policy=profile_x_medium|Amsterdam Centrum                  |2                  |2                        |['email', 'phone']                |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Centrum-West                          |                            |52.36775          |4.89092           |Private room in rental unit       |Private room   |2           |         |1 shared bath    |1       |1   |["Paid dryer                                     |$76.00   |2             |1825          |1                     |2                     |1825                  |1825                  |1.7                   |1825.0                |                |t               |0              |0              |0              |79              |2023-03-10           |476              |97                   |7                     |2010-08-22  |2023-02-28 |4.87                |4.92                  |4.88                     |4.95                 |4.94                       |4.96                  |4.82               |0363 607B EA74 0BD8 2F6F|f               |2                             |0                                          |2                                           |0                                          |3.12             |
|367491            |https://www.airbnb.com/rooms/367491            |20230309202119|2023-03-10  |previous scrape|Charming,  bright and quiet home center Amsterdam                          |! discount in...  |Oud-West is central and quiet, a village in a village kinda vibe.                                                                                                                                                         |https://a0.muscache.com/pictures/ef2d713d-c448-4e11-ae04-9c11cc3b088e.jpg                                                     |1855417  |https://www.airbnb.com/users/show/1855417  |Maarten                          |2012-03-04|Amsterdam, Netherlands                 |          |within a few hours|100%              |94%                 |t                |https://a0.muscache.com/im/pictures/user/d9b6709a-5d9b-4a1c-b3c1-c0b1aece5cc8.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/d9b6709a-5d9b-4a1c-b3c1-c0b1aece5cc8.jpg?aki_policy=profile_x_medium|Oud-West                           |1                  |1                        |['email', 'phone']                |t                   |t                     |Amsterdam, Noord-Holland, Netherlands                      |De Baarsjes - Oud-West                |                            |52.364            |4.87814           |Entire rental unit                |Entire home/apt|2           |         |1.5 baths        |1       |1   |["Washer"...                                  |$189.00  |3             |19            |3                     |3                     |19                    |19                    |3.0                   |19.0                  |                |t               |0              |1              |2              |2               |2023-03-10           |77               |5                    |0                     |2012-03-25  |2023-01-29 |4.9                 |4.89                  |4.76                     |4.95                 |4.96                       |4.92                  |4.72               |0363 7096 B559 45DB 421C|f               |1                             |1                   |0                |0                                          |0.58             |
|29051             |https://www.airbnb.com/rooms/29051             |20230309202119|2023-03-10  |city scrape    |Comfortable single room                                                    |This room... |the street is quite lively especially on weekends when the weather is good                                                                                               |https://a0.muscache.com/pictures/162009/bd6be2f8_original.jpg                                                                 |124245   |https://www.airbnb.com/users/show/124245   |Edwin                            |2010-05-13|Amsterdam, Netherlands                 |Hi                                                                                                           |within an hour    |100%              |99%                 |t                |https://a0.muscache.com/im/pictures/user/9986bbdb-632f-42b5-a866-8e3307184977.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/9986bbdb-632f-42b5-a866-8e3307184977.jpg?aki_policy=profile_x_medium|Amsterdam Centrum                  |2                  |2                        |['email', 'phone']                |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Centrum-Oost                          |                            |52.36584          |4.89111           |Private room in rental unit       |Private room   |2           |         |1 shared bath    |1       |1   |["Carbon monoxide alarm"...     |$56.00   |2             |730           |1                     |2                     |730                   |730                   |1.7                   |730.0                 |                |t               |0              |0              |0              |69              |2023-03-10           |618              |85                   |7                     |2011-03-16  |2023-03-03 |4.8                 |4.88                  |4.85                     |4.91                 |4.91                       |4.88                  |4.78               |0363 607B EA74 0BD8 2F6F|f               |2                             |0                                          |2                                           |0                                          |4.23             |
|44391             |https://www.airbnb.com/rooms/44391             |20230309202119|2023-03-10  |previous scrape|Quiet 2-bedroom Amsterdam city centre apartment                            |Guests greatly...       |The appartment... |https://a0.muscache.com/pictures/97741545/39000c13_original.jpg                                                               |194779   |https://www.airbnb.com/users/show/194779   |Jan                              |2010-08-08|Amsterdam, Netherlands                 |Love to travel while hosting and to host while travelling! |N/A               |N/A               |100%                |f                |https://a0.muscache.com/im/users/194779/profile_pic/1436464796/original.jpg?aki_policy=profile_small      |https://a0.muscache.com/im/users/194779/profile_pic/1436464796/original.jpg?aki_policy=profile_x_medium      |Oostelijke Eilanden en Kadijken    |1                  |1                        |['email', 'phone']                |t                   |t                     |Amsterdam, Noord-Holland, Netherlands                      |Centrum-Oost                          |                            |52.37168          |4.91471           |Entire rental unit                |Entire home/apt|4           |         |1.5 baths        |2       |2   |["Host greets you", "Wifi"...  |$240.00  |3             |730           |3                     |3                     |730                   |730                   |3.0                   |730.0                 |                |t               |0              |0              |0              |0               |2023-03-10           |44               |3                    |0                     |2010-09-16  |2022-08-20 |4.72                |4.68                  |4.45                     |4.95                 |4.9                        |4.68                  |4.5                |0363 E76E F06A C1DD 172C|f               |1                             |1                                          |0                                           |0                                          |0.29             |
|378523            |https://www.airbnb.com/rooms/378523            |20230309202119|2023-03-10  |city scrape    |Freedom on the water!                                                      |Registration:...  |Close to museums...  |https://a0.muscache.com/pictures/6819792/45010ffb_original.jpg        |1901477  |https://www.airbnb.com/users/show/1901477  |Caroline   |2012-03-11|Amsterdam, Netherlands                 |Registration number...  |within an hour    |100%              |100%                |f                |https://a0.muscache.com/im/pictures/user/935f2959-7a9f-4801-9b5c-9f5b78d4319c.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/935f2959-7a9f-4801-9b5c-9f5b78d4319c.jpg?aki_policy=profile_x_medium|Nieuwmarkt en Lastage              |1                  |1                        |['email', 'phone']                |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Centrum-Oost                          |                            |52.3742           |4.90401           |Boat                              |Entire home/apt|2           |         |1.5 baths        |1       |1   |["Drying rack for clothing"...|$337.00  |4             |8             |4                     |4                     |1125                  |1125                  |4.0                   |1125.0                |                |t               |0              |6              |26             |41              |2023-03-10           |115              |5                    |0                     |2012-09-04  |2022-06-20 |4.94                |4.95                  |4.92                     |4.99                 |4.97                       |4.93                  |4.81               |0363 0D10 7FFD B425 1553|f               |1                             |1                                          |0                                           |0                                          |0.90             |
|49552             |https://www.airbnb.com/rooms/49552             |20230309202119|2023-03-10  |city scrape    |Multatuli Luxury Guest Suite in top location                               |Stylish & spacious...  |You will find...|https://a0.muscache.com/pictures/a6d6d2ee-3196-4e3b-b0ec-d26b71d598ec.jpg                                                     |225987   |https://www.airbnb.com/users/show/225987   |Joanna & MP                      |2010-09-06|Amsterdam, Netherlands                 |Joanna is from...            |within a few hours|100%              |91%                 |t                |https://a0.muscache.com/im/pictures/user/a0545607-d4b4-407a-9a4e-f946b459f691.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/a0545607-d4b4-407a-9a4e-f946b459f691.jpg?aki_policy=profile_x_medium|Grachtengordel                     |1                  |2                        |['email', 'phone', 'work_email']  |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Centrum-West                          |                            |52.38028          |4.89089           |Entire guest suite                |Entire home/apt|3           |         |1 bath           |2       |2   |["Board games"...           |$257.00  |3             |1125          |1                     |4                     |1125                  |1125                  |3.0                   |1125.0                |                |t               |3              |3              |11             |134             |2023-03-10           |462              |64                   |3                     |2010-10-29  |2023-02-23 |4.92                |4.92                  |4.91                     |4.95                 |4.97                       |4.98                  |4.79               |0363 576A D827 5085 6B83|f               |1                             |1                                          |0                                           |0                                          |3.07             |
|379885            |https://www.airbnb.com/rooms/379885            |20230309202119|2023-03-09  |city scrape    |Private Studio Houseboat *BEST VIEW* @Amstel                               |This is...   |The Ark...    |https://a0.muscache.com/pictures/e66b13a8-57b5-45ea-a006-fdf4caddbfa8.jpg                                                     |1907015  |https://www.airbnb.com/users/show/1907015  |Masha                            |2012-03-12|Amsterdam, Netherlands                 |I am...  |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/users/1907015/profile_pic/1363287021/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1907015/profile_pic/1363287021/original.jpg?aki_policy=profile_x_medium     |                                   |1                  |4                        |['email', 'phone', 'work_email']  |t                   |t                     |Watergraafsmeer, North Holland, Netherlands                |De Pijp - Rivierenbuurt               |                            |52.35465          |4.9061            |Private room in houseboat         |Private room   |2           |         |1 private bath   |1       |1   |["Wifi", "Hair dryer", "Bed linens"...|$217.00  |3             |360           |3                     |3                     |1125                  |1125                  |3.0                   |1125.0                |                |t               |5              |8              |18             |203             |2023-03-09           |92               |10                   |1                     |2012-05-20  |2023-02-20 |4.69                |4.68                  |4.54                     |4.76                 |4.62                       |4.85                  |4.48               |0363 3FE4 07B5 85AA 55F8|t               |1                             |0                                          |1                                           |0                                          |0.70             |
|402353            |https://www.airbnb.com/rooms/402353            |20230309202119|2023-03-09  |city scrape    |Comfortable design apartment with roof terrace                             |Our apartment offers...   |     |https://a0.muscache.com/pictures/6611343/57afccf2_original.jpg                                                                |2008330  |https://www.airbnb.com/users/show/2008330  |Lidy                             |2012-03-26|Amsterdam, Netherlands                 |For more than...    |within an hour    |100%              |95%                 |t                |https://a0.muscache.com/im/users/2008330/profile_pic/1343472579/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/2008330/profile_pic/1343472579/original.jpg?aki_policy=profile_x_medium     |Watergraafsmeer                    |1                  |1                        |['email', 'phone']                |t                   |t                     |                                                           |Watergraafsmeer                       |                            |52.35338          |4.93407           |Private room in loft              |Private room   |2           |         |1.5 baths        |1       |1   |["Board games"... |$154.00  |2             |1125          |2                     |2                     |1125                  |1125                  |2.0                   |1125.0                |                |t               |0              |0              |0              |67              |2023-03-09           |249              |34                   |1                     |2012-07-13  |2023-02-12 |4.85                |4.83                  |4.94                     |4.92                 |4.91                       |4.74                  |4.72               |0363 12D8 9BB2 949E 3227|t               |1                             |0                                          |1                                           |0                                          |1.92             |
|50263             |https://www.airbnb.com/rooms/50263             |20230309202119|2023-03-09  |city scrape    |Cent Adam Lux 2bed(4p) apt 125 sqm                                         |A beautiful...   |The house is... |https://a0.muscache.com/pictures/677876/7cb949b4_original.jpg                                                                 |230246   |https://www.airbnb.com/users/show/230246   |Donald                           |2010-09-10|Amsterdam, Netherlands                 |An independent...   |within a few hours|100%              |100%                |f                |https://a0.muscache.com/im/users/230246/profile_pic/1285857268/original.jpg?aki_policy=profile_small      |https://a0.muscache.com/im/users/230246/profile_pic/1285857268/original.jpg?aki_policy=profile_x_medium      |Oostelijke Eilanden en Kadijken    |1                  |1                        |['email', 'phone']                |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Centrum-Oost                          |                            |52.37118          |4.93146           |Entire condo                      |Entire home/apt|4           |         |1.5 baths        |2       |3   |["Wifi", "Washer"...|$395.00  |4             |30            |4                     |5                     |30                    |30                    |4.0                   |30.0                  |                |t               |17             |43             |66             |341             |2023-03-09           |163              |0                    |0                     |2010-10-13  |2016-05-03 |4.86                |4.93                  |4.8                      |4.82                 |4.75                       |4.64                  |4.75               |0363 7F3D 0BAE 28C8 C7D2|f               |1                             |1                                          |0                                           |0                                          |1.08             |
|415619            |https://www.airbnb.com/rooms/415619            |20230309202119|2023-03-09  |city scrape    |Sunny Amsterdam East Harbor View                                           |Lofty, sunny... |https://a0.muscache.com/pictures/5123687/f30d1f05_original.jpg                                                                |1336633  |https://www.airbnb.com/users/show/1336633  |Stephan                          |2011-10-26|Amsterdam, Netherlands                 |Sharing your home and... |within a few hours|100%              |35%                 |f                |https://a0.muscache.com/im/users/1336633/profile_pic/1328463417/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1336633/profile_pic/1328463417/original.jpg?aki_policy=profile_x_medium     |Zeeburg                            |1                  |1                        |['email', 'phone']                |t                   |t                     |Zeeburg, North Holland, Netherlands                        |Oostelijk Havengebied - Indische Buurt|                            |52.36905          |4.93528           |Entire rental unit                |Entire home/apt|3           |         |1 bath           |1       |1   |["Board games"... |$148.00  |2             |30            |2                     |2                     |30                    |30                    |2.0                   |30.0                  |                |t               |0              |1              |3              |70              |2023-03-09           |78               |7                    |0                     |2012-05-21  |2023-01-09 |4.87                |4.92                  |4.77                     |4.99                 |4.97                       |4.8                   |4.73               |0363 09A6 8FFA 6EC4 805F|f               |1                             |1                                          |0            |0                                          |0.59             |
|50523             |https://www.airbnb.com/rooms/50523             |20230309202119|2023-03-10  |city scrape    |B & B de 9 Straatjes (city center)                                         |B & B... | |https://a0.muscache.com/pictures/290179/a6be901e_original.jpg          |231946   |https://www.airbnb.com/users/show/231946   |Raymond                          |2010-09-12|Amsterdam, Netherlands                 |Hallo I am Raymond... |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/pictures/user/00f9d4e7-a503-46b6-9f1e-c04e8c4bccd2.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/00f9d4e7-a503-46b6-9f1e-c04e8c4bccd2.jpg?aki_policy=profile_x_medium|Grachtengordel                     |1                  |2                        |['email', 'phone']                |t                   |t                     |                                                           |Centrum-West                          |                            |52.36811          |4.88262           |Private room in bed and breakfast |Private room   |2           |         |1 private bath   |1       |1   |["Smoke alarm"... |$133.00  |2             |365           |2                     |2                     |365                   |365                   |2.0                   |365.0                 |                |t               |2              |6              |8              |175             |2023-03-10           |385              |71                   |3                     |2011-01-04  |2023-02-22 |4.87                |4.91                  |4.87                     |4.88                 |4.85                       |4.94                  |4.83               |0363 22DC 0E52 B70B 0FB8|f               |1                             |0                                          |1                                           |0                                          |2.60             |
|55709             |https://www.airbnb.com/rooms/55709             |20230309202119|2023-03-10  |city scrape    |Bright Loft in Centre Amsterdam                                            |The space...  |The apartment is... |https://a0.muscache.com/pictures/14896636/c2667327_original.jpg                                                               |263233   |https://www.airbnb.com/users/show/263233   |Jan-Willem                       |2010-10-16|Amsterdam, Netherlands                 |Enthusiastic and helpful... |N/A               |N/A               |50%                 |f                |https://a0.muscache.com/im/users/263233/profile_pic/1287239267/original.jpg?aki_policy=profile_small      |https://a0.muscache.com/im/users/263233/profile_pic/1287239267/original.jpg?aki_policy=profile_x_medium      |Grachtengordel                     |2                  |4                        |['email', 'phone']                |t                   |t                     |Amsterdam, North Holland, Netherlands                      |Centrum-Oost                          |                            |52.358112         |4.897637          |Entire loft                       |Entire home/apt|2           |         |1.5 baths        |1       |1   |["Drying rack for clothing"...                          |$150.00  |3             |3             |2                     |3                     |3                     |3                     |3.0                   |3.0                   |                |t               |2              |2              |2              |2               |2023-03-10           |65               |3                    |0                     |2010-12-06  |2022-10-16 |4.95                |4.89                  |4.92                     |4.94                 |4.98                       |4.92                  |4.8                |0363 E295 7D15 8420 343E|f               |1                             |1                                          |0                                           |0                                          |0.44             |
|432233            |https://www.airbnb.com/rooms/432233            |20230309202119|2023-03-10  |previous scrape|Beautiful apartment @ true center                                          |NOTE:...  |  |https://a0.muscache.com/pictures/27900848/b8ee2813_original.jpg                                                               |2144360  |https://www.airbnb.com/users/show/2144360  |Feiko                            |2012-04-15|Amsterdam, Netherlands                 |I provide tech education                                                                                                                                             |N/A               |N/A               |12%                 |f                |https://a0.muscache.com/im/pictures/user/c12c6886-f0d4-44f9-bd4a-a74f44825430.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/c12c6886-f0d4-44f9-bd4a-a74f44825430.jpg?aki_policy=profile_x_medium|Grachtengordel                     |1                  |1                        |['email', 'phone', 'work_email']  |t                   |t                     |                                                           |Centrum-Oost                          |                            |52.3609619140625  |4.88822603225708  |Entire rental unit                |Entire home/apt|2           |         |1 bath           |1       |1   |["Carbon monoxide alarm"... |$250.00  |5             |100           |5                     |5                     |100                   |100                   |5.0                   |100.0                 |                |t               |0              |0              |0              |0               |2023-03-10           |27               |3                    |0                     |2012-05-01  |2022-09-25 |4.8                 |4.62                  |4.65                     |4.73                 |4.88                       |4.88                  |4.62               |0363 DA8F B298 31AF FE9B|f               |1                             |1                                          |0                                           |0                                          |0.20             |  
  
  

### Some Problems Encountered/Scrubbing:  
  
Firstly, I found the original dataset to be unecessarily long and redundant. Because of this the file size was massive and it made things run slower. Therefore, I used ***Microsoft Excel*** to drop columns that I felt unecessary to analyzing Amsterdam's listings for the month of March. For example, columns like picture_url, amenities, scrape_id, miminimum_maximum_nights were dropped alongside many others for their lack of contribution to the overall dataset. I also dropped columns with blank fields like neighborhood_group_cleansed or calendar_updated because they did not change any meaning to other values in the dataset. This allowed for a much more workable dataset that was smaller in size to import with ease. I have also attached the Excel spreadsheet in the data directory. (Note: I did not upload this to i6 because I did not see much significiance in doing so.) I then converted this spreadsheet to a CSV file called 'listings_cleaned.csv' that is uploaded onto i6 and can also be referenced in the data directory of this assignment.  
  
## Analysis  
  

1. Show exactly two documents from the `listings` collection in any order:  
  
```
db.listings.find().limit(2)
```  
  
Output:  

>[
  {
    _id: ObjectId("6436c07924ed498386cbb842"),
    id: 2818,
    listing_url: 'https://www.airbnb.com/rooms/2818',
    name: 'Quiet Garden View Room & Super Fast Wi-Fi',
    neighborhood_overview: `Indische Buurt ("Indies Neighborhood") is a neighbourhood in the eastern portion of the city of Amsterdam, in the Dutch province of Noord-Holland. The name dates from the early 20th century and is derived from the fact that the neighbourhood's streets are named after islands and other geographical concepts in the former Dutch colony of the Dutch East Indies. The first street was named in 1902. In 2003, there were around 23,357 inhabitants. The neighbourhood is bounded on the west by the railroad Amsterdam - Hilversum (with the Muiderpoort Station), on the east side by Flevopark, on the north side by Zeeburgerdijk and on the south side by the Ringvaart Watergraafsmeer. Indische Buurt is the oldest part of the Zeeburg district and is very ethnically diverse, and a high percentage of the population is of immigrant origin (for Zeeburg this is already high at 55%, but higher in the Indische Buurt) and there are an estimated 100 languages spoken.`,
    host_id: 3159,
    host_name: 'Daniel',
    host_since: '9/24/2008',
    host_location: 'Amsterdam, Netherlands',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 't',
    host_neighbourhood: 'Indische Buurt',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_identity_verified: 't',
    neighbourhood: 'Amsterdam, North Holland, Netherlands',
    neighbourhood_cleansed: 'Oostelijk Havengebied - Indische Buurt',
    property_type: 'Private room in rental unit',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms_text: '1.5 shared baths',
    bedrooms: 1,
    beds: 2,
    price: '$69.00',
    has_availability: 't',
    number_of_reviews: 322,
    review_scores_rating: 4.89,
    review_scores_accuracy: 4.93,
    review_scores_cleanliness: 4.99,
    review_scores_checkin: 4.97,
    review_scores_communication: 4.98,
    review_scores_location: 4.69,
    review_scores_value: 4.81,
    license: '0363 5F3A 5684 6750 D14D',
    instant_bookable: 'f',
    reviews_per_month: 1.9
  },
  {
    _id: ObjectId("6436c07924ed498386cbb843"),
    id: 311124,
    listing_url: 'https://www.airbnb.com/rooms/311124',
    name: '*historic centre* *bright* *canal view* *jordaan*',
    neighborhood_overview: 'Perfect location in the lively centre. All historic high lights, shopping, eating and drinking out options in walking distance.',
    host_id: 1600010,
    host_name: 'Anke & Robert',
    host_since: '1/12/2012',
    host_location: 'Amsterdam, Netherlands',
    host_response_time: 'within a few hours',
    host_response_rate: '100%',
    host_acceptance_rate: '68%',
    host_is_superhost: 'f',
    host_neighbourhood: 'Jordaan',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone', 'work_email']",
    host_identity_verified: 'f',
    neighbourhood: 'Amsterdam, North Holland, Netherlands',
    neighbourhood_cleansed: 'Centrum-West',
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 1,
    price: '$325.00',
    has_availability: 't',
    number_of_reviews: 87,
    review_scores_rating: 4.76,
    review_scores_accuracy: 4.72,
    review_scores_cleanliness: 4.79,
    review_scores_checkin: 4.9,
    review_scores_communication: 4.92,
    review_scores_location: 4.93,
    review_scores_value: 4.6,
    license: '0363 59D8 7D30 6CFA DC81',
    instant_bookable: 'f',
    reviews_per_month: 0.66
  }
>]  
   
**Insights:**  
What this output shows in comparison to someone jsut viewing the raw data is exactly just the necessary information for any two listings. Unecessary information is gone, therefore making it easier to find information that may be useful when searching for an Airbnb and not getting lost in the excess information. For example, a person is more likely to want to know the amount of beds in the listing as opposed to the longitude and latitude of the listing.  
  

 2. Show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the `pretty()` function.  
   
```
db.listings.find().limit(10).pretty()
```  
  
Output:  

>[
  {
    _id: ObjectId("6436c07924ed498386cbb842"),
    id: 2818,
    listing_url: 'https://www.airbnb.com/rooms/2818',
    name: 'Quiet Garden View Room & Super Fast Wi-Fi',
    neighborhood_overview: `Indische Buurt ("Indies Neighborhood") is a neighbourhood in the eastern portion of the city of Amsterdam, in the Dutch province of Noord-Holland. The name dates from the early 20th century and is derived from the fact that the neighbourhood's streets are named after islands and other geographical concepts in the former Dutch colony of the Dutch East Indies. The first street was named in 1902. In 2003, there were around 23,357 inhabitants. The neighbourhood is bounded on the west by the railroad Amsterdam - Hilversum (with the Muiderpoort Station), on the east side by Flevopark, on the north side by Zeeburgerdijk and on the south side by the Ringvaart Watergraafsmeer. Indische Buurt is the oldest part of the Zeeburg district and is very ethnically diverse, and a high percentage of the population is of immigrant origin (for Zeeburg this is already high at 55%, but higher in the Indische Buurt) and there are an estimated 100 languages spoken.`,
    host_id: 3159,
    host_name: 'Daniel',
    host_since: '9/24/2008',
    host_location: 'Amsterdam, Netherlands',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 't',
    host_neighbourhood: 'Indische Buurt',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_identity_verified: 't',
    neighbourhood: 'Amsterdam, North Holland, Netherlands',
    neighbourhood_cleansed: 'Oostelijk Havengebied - Indische Buurt',
    property_type: 'Private room in rental unit',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms_text: '1.5 shared baths',
    bedrooms: 1,
    beds: 2,
    price: '$69.00',
    has_availability: 't',
    number_of_reviews: 322,
    review_scores_rating: 4.89,
    review_scores_accuracy: 4.93,
    review_scores_cleanliness: 4.99,
    review_scores_checkin: 4.97,
    review_scores_communication: 4.98,
    review_scores_location: 4.69,
    review_scores_value: 4.81,
    license: '0363 5F3A 5684 6750 D14D',
    instant_bookable: 'f',
    reviews_per_month: 1.9
  },
  {
    _id: ObjectId("6436c07924ed498386cbb843"),
    id: 311124,
    listing_url: 'https://www.airbnb.com/rooms/311124',
    name: '*historic centre* *bright* *canal view* *jordaan*',
    neighborhood_overview: 'Perfect location in the lively centre. All historic high lights, shopping, eating and drinking out options in walking distance.',
    host_id: 1600010,
    host_name: 'Anke & Robert',
    host_since: '1/12/2012',
    host_location: 'Amsterdam, Netherlands',
    host_response_time: 'within a few hours',
    host_response_rate: '100%',
    host_acceptance_rate: '68%',
    host_is_superhost: 'f',
    host_neighbourhood: 'Jordaan',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone', 'work_email']",
    host_identity_verified: 'f',
    neighbourhood: 'Amsterdam, North Holland, Netherlands',
    neighbourhood_cleansed: 'Centrum-West',
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 1,
    price: '$325.00',
    has_availability: 't',
    number_of_reviews: 87,
    review_scores_rating: 4.76,
    review_scores_accuracy: 4.72,
    review_scores_cleanliness: 4.79,
    review_scores_checkin: 4.9,
    review_scores_communication: 4.92,
    review_scores_location: 4.93,
    review_scores_value: 4.6,
    license: '0363 59D8 7D30 6CFA DC81',
    instant_bookable: 'f',
    reviews_per_month: 0.66
  },
  {
    _id: ObjectId("6436c07924ed498386cbb844"),
    id: 319985,
    listing_url: 'https://www.airbnb.com/rooms/319985',
    name: 'Elegant Appartement Central Location.',
    neighborhood_overview: 'Bij aankomst vertel ik mijn gasten graag over de omgeving.',
    host_id: 1640702,
    host_name: 'J',
    host_since: '1/23/2012',
    host_location: 'Amsterdam, Netherlands',
    host_response_time: 'within a day',
    host_response_rate: '93%',
    host_acceptance_rate: '89%',
    host_is_superhost: 't',
    host_neighbourhood: 'De Pijp',
    host_listings_count: 2,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone']",
    host_identity_verified: 't',
    neighbourhood: 'De Pijp, North Holland, Netherlands',
    neighbourhood_cleansed: 'De Pijp - Rivierenbuurt',
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 4,
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 2,
    price: '$244.00',
    has_availability: 't',
    number_of_reviews: 492,
    review_scores_rating: 4.75,
    review_scores_accuracy: 4.83,
    review_scores_cleanliness: 4.69,
    review_scores_checkin: 4.86,
    review_scores_communication: 4.78,
    review_scores_location: 4.85,
    review_scores_value: 4.62,
    license: '0363 7D88 E1E8 F521 9A10',
    instant_bookable: 'f',
    reviews_per_month: 3.73
  }
>]  
  
**Insights**  
Similar to the question above, this gives a person more options in choosing a listing without all the redudancy. For the assignment purposes, I have only show the first three results. This question takes what people may not be able to easily find while looking at the raw data a step further by giving more options with a "pretty" format applied that organizes Urls and text as a cleaner look.  
  

3. Choose two hosts (by reffering to their `host_id` values) who are superhosts (available in the `host_is_superhost` field), and show all of the listings offered by both of the two hosts
   - only show the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result

```
db.listings.find({
...   host_is_superhost: "t"
... }).count()
```  
Output:  
>1382  
  

```
db.listings.distinct("host_id", { host_is_superhost: "t" })

```  
  
Output:  

>[
     3159,   61977,   70163,
      ...more items
>]
  

```
db.listings.find({
...   $and: [
...     { host_id: { $in: [3159, 70163] } },
...     { host_is_superhost: "t" }
...   ]
... }, {
...   name: 1,
...   price: 1,
...   neighbourhood: 1,
...   host_name: 1,
...   host_is_superhost: 1,
...   _id: 0
... })
```  
  
Output:  


>[
  {
    name: 'Quiet Garden View Room & Super Fast Wi-Fi',
    host_name: 'Daniel',
    host_is_superhost: 't',
    neighbourhood: 'Amsterdam, North Holland, Netherlands',
    price: '$69.00'
  },
  {
    name: 'Brilliant, Bright and Bohemian in de Pijp',
    host_name: 'T & R',
    host_is_superhost: 't',
    neighbourhood: 'Amsterdam, Noord-Holland, Netherlands',
    price: '$407.00'
  }
>]
 
**Analysis**  
For this question, I took a longer route by first performing a query that allowed me to count the amount of superhosts in the dataset to see what I was working with. After finding the total number of superhosts showcased by the data, I performed a query that displayed host id's that held the superhost condition to "true" or in this case, "t". That allowed me to choose two host id's of my choosing to perform my final query that gave me the listings for those two selected hosts. I only wanted to display name, price, neighbourhood, host_name, and if they were a superhost or not so I included some conditions in the query that would allow me to find this.  
  
Someone looking at the raw data would not be able to find this as easy and would have to scroll and swipe to match the conditions manually and it would not display this information in a readable format. Thus, without these queries, the subject is more likely for human error and not finding an accurate listing they are looking for.  
  

4. Find all the unique `host_name` values (see [the docs](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/))

```
db.listings.distinct("host_name")
```  
Output:  

>[
  NaN,
  '(Email hidden by Airbnb)',
  '23 SouS',
  'A.C.',
  'Aafje',
  'Aafke',
  ...more items
>]  
  
**Analysis**  
This query returned all the unique host names in the dataset. Following the host names that start with an A, the list was also arranged in alphabetical order for easier viewing. Someone viewing the raw dataset would simply not have the human capability to gain the entire list of host names if needed. This allows a user to find a listing through host name if they wish to find a place this way.  
  

5. Find all of the places that have more than 2 `beds` in a neighborhood of your choice (referred to as either the `neighborhood` or `neighbourhood_group_cleansed` fields in the data file), ordered by `review_scores_rating` descending
   - only show the `name`, `beds`, `review_scores_rating`, and `price`
   - if your data set only has blanks for all the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to filter by - include an explanation and justification for this in your report.
   - if you run out of memory for this query, try filtering `review_scores_rating` that aren't empty (`$ne`); and lastly, if there's still an issue, you can set the `beds` to match exactly 2.  
     
```
db.listings.find({
...   $and: [
...     { beds: { $gt: 2 } },
...     { neighbourhood_cleansed: "Centrum-Oost" },
...     { review_scores_rating: { $ne: null } }
...   ]
... }, {
...   name: 1,
...   beds: 1,
...   review_scores_rating: 1,
...   price: 1,
...   _id: 0
... }).sort({ review_scores_rating: -1 })
```  
  
Output:  

>[
  {
    name: 'Lovely, Cosy@Canal-City Centre!',
    beds: 4,
    price: '$200.00',
    review_scores_rating: ''
  },
  {
    name: 'Canal View Apartment | Amsterdam Canal Suites',
    beds: 4,
    price: '$999.00',
    review_scores_rating: ''
  },
  {
    name: '8-person private room with private shower',
    beds: 5,
    price: '$200.00',
    review_scores_rating: ''
  },
  {
    name: 'Large family loft Amsterdam center private parking',
    beds: 3,
    price: '$350.00',
    review_scores_rating: 5
  },
>]  
  
**Analysis**  
Following the question's instructions, I chose listings in Centrum-Oost area to find places that had more than 2 beds. It was also displayed in descending order based on their review scores rating. Note that the first three results show a null review scores rating due to their blank field so I have attached the next listing following this order to display that this query was able to indeed successfully display them in descending order. To someone viewing the raw data, this would be very helpful in selecting a listing based on bed and rating needs. The descending order definitely helps a lot so that the user does not have to waste time in looking at 2 beds without any reviews if they chose to do so.  

 
6. Show the number of listings per host.  
  
```
db.listings.aggregate([
...   {
...     $group: {
...       _id: "$host_id",
...       count: { $sum: 1 }
...     }
...   }
... ])
```  
  
Output:

>[
  { _id: 58158635, count: 1 },
  { _id: 3041589, count: 1 },
  { _id: 489588209, count: 1 },
>]  
  
**Analysis**  
This query was able to list out all the number of listings for each unique host id. This would give insight to any listing manager or someone who wanted to see how many listings an individual had. It is readable and query can also be modified by inputting only one host id. Therefore, providing far more information than somebody just viewing the raw data.  
  

7. Find the average `review_scores_rating` per neighborhood, and only show the ones above a `95`, sorted in descending order of rating (see [the docs](https://docs.mongodb.com/manual/reference/operator/aggregation/sort/))
   - if your data set only has blanks in the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to break down the listings by - include an explanation and justification for this in your report.  
     
```
db.listings.aggregate([
...   {
...     $match: {
...       review_scores_rating: { $gt: 0 }
...     }
...   },
...   {
...     $group: {
...       _id: "$neighbourhood_cleansed",
...       avg_rating: { $avg: "$review_scores_rating" }
...     }
...   },
...   {
...     $match: {
...       avg_rating: { $gt: 4.5 }
...     }
...   },
...   {
...     $sort: {
...       avg_rating: -1
...     }
...   }
... ])
```  

Output:  
>[
  { _id: 'Watergraafsmeer', avg_rating: 4.856722222222222 },
  { _id: 'IJburg - Zeeburgereiland', avg_rating: 4.851357142857143 },
  { _id: 'Noord-West', avg_rating: 4.848 },
>]  
  
**Analysis**  
This query took average ratings per neighborhood and displayed properties that had above a 4.5 rating. The directions called for above a 95 but unfortuantely, my dataset rated on a 5 point scale. Therefore, I deemed it suffice to say that 4.5 is equivalent to 95 and filtered it with an average rating of 4.5.   
  
For someone viewing the raw data, it would take a very long time to find the average rating per neighborhood given that this a very large dataset and are likely to be subject towards human error. This query reduces that drastically and allows somebody to go directly to listings to the neighborhood they wish to stay in and select from the highly rated places there.
  
  
## Extra Credit  
  
***Please refer to the 'mongo.py' document for my python code for the extra credit analyses.***  
  
#### Pymongo Output:  
  
>[
  {
    name: 'Lovely, Cosy@Canal-City Centre!',
    beds: 4,
    price: '$200.00',
    review_scores_rating: ''
  },
  {
    name: 'Canal View Apartment | Amsterdam Canal Suites',
    beds: 4,
    price: '$999.00',
    review_scores_rating: ''
  },
  {
    name: '8-person private room with private shower',
    beds: 5,
    price: '$200.00',
    review_scores_rating: ''
  },
  {
    name: 'Large family loft Amsterdam center private parking',
    beds: 3,
    price: '$350.00',
    review_scores_rating: 5
  },
>]  
  
I recreated one of my earlier queries using a pymongo code to find all of the places that have more than 2 beds in a Centrum-Oost, ordered by `review_scores_rating` descending. I only displayed the `name`, `beds`, `review_scores_rating`, and `price`. Sure enough, I was able to double confirm the valdiity of my output by getting the same descending order as my earlier query.  
  
I believe this assignment deserves extra credit because I was able to successfully run my pymongo code to match one of my earlier queries. Through this assignment, I also was able to gain insightful data on Amsterdam's Airbnb listings for the month of March that would not have been easy to gain by someone just looking at the raw data. I used multiple resources and research to get to this point, therefore I believe my efforts are on par with the elgibility for extra credit. 

