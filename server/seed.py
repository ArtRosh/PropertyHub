from random import randint, choice as rc


from faker import Faker
from config import bcrypt

from app import app
from models import db, Property, Review, Image, User, PropertyUser


if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Nuking the database....")
        
        
        # Delete all existing records from the tables
        db.session.query(Property).delete()
        db.session.query(Review).delete()
        db.session.query(Image).delete()
        db.session.query(User).delete()


        print("Starting seed...")


        #Create and seed the Properties
        print('Picking Properties...')

        properties = [
            Property(
                name = 'Phat Phish',
                location = 'Oak Island, North Carolina',
                description = "There's nothing better than having the ocean as your front yard, and that's exactly what you get at this ocean front oasis. The sound of the waves will drift you off to sleep. Take in the views from the ocean front deck, the beach is right dow the front steps!",
                amenities = "4 bedrooms One King bedroom, 2 full bedrooms, and one room with two twin beds. All rooms have TV and Roku, except the kids room. 2 full bathrooms, each with a tub Full kitchen with plenty of cookware and serving dishes. Blender, Kuerig, coffee maker, toaster, microwave. Dining table for 6 Nice living room with full ocean view right from the couch. Or the recliner! Decisions, decisions. Roku TV",
                availability = 'https://www.airbnb.com/calendar/ical/738948885345971986.ics?s=7dc124552a0de7b6db90111cf65ab513',
                image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/1c4bb929-c94e-4296-9a4a-9f3d0778f3d3.jpeg?im_w=1200',
                reservation = 'https://www.airbnb.com/rooms/738948885345971986?adults=1&children=0&enable_m3_private_room=true&infants=0&pets=0&check_in=2024-01-04&check_out=2024-01-09&source_impression_id=p3_1700483243_yI9KNk%2BHU2WhQZ4H&previous_page_section_name=1000&federated_search_id=e0ab65cc-4d28-4687-831a-648d00b4c9d0',
            ),

            Property(
                name = 'Slopesider 6',
                location = 'Sugar Mountain, North Carolina',
                description = 'With the ski slope out the front door it does not get much better than this. With ski-in /ski-out access this original Sugar Mountain slopesider cabin is a mountain dream escape. Watch the action on the slopes from the porch or inside with the floor to ceiling windows. There is even a cozy wood burning fire place. In the fall this is the perfect retreat to take in the autumnal colors while you spend your days sightseeing along the parkway. This circular treetop cabin has floor to ceiling windows and an open floorplan in the kitchen, living and dining room making you feel as if you are in a tree-top hideaway. There is a wood burning fireplace that is the heart of the home and a spiral staircase (and baby gate!) leading to the lower level with the laundry room, mudroom and ski slope access.  When there is snow on the roads you will need a 4WD vehicle to access the property.',
                amenities = 'Two Bedrooms, Two Bathrooms, living room, woodstove, a tv in each room, dining space with coffee station, fully equipped kitchen, Deck, Ski room with table and chairs, ski racks, ski in/out entrance from slope.',
                availability = 'https://www.airbnb.com/calendar/ical/731915024153813910.ics?s=bbaaa95eef6b88b7d6286b82d0745214',
                image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/da29b252-0507-452f-9dca-aec927354da4.jpeg?im_w=1200',
                reservation = 'https://www.airbnb.com/rooms/731915024153813910?adults=1&children=0&enable_m3_private_room=true&infants=0&pets=0&check_in=2023-12-01&check_out=2023-12-06&source_impression_id=p3_1700243377_rEWPco5lM%2BRc4NqV&previous_page_section_name=1000&federated_search_id=ea2c9ebc-3cc3-46e4-99c8-7291c98783dd',
            )

            
        ]


        db.session.add_all(properties)
        db.session.commit()


        reviews = [
            Review(
                name = 'Selena',
                email = 'N/A',
                rating = 5,
                comment = "Porter's instructions were super helpful and straight forward. Easy to find the place, key, surrounding places, recommendations, trash hut. Loved all the antiques. Very nice location with an even nicer view!",
                property_id = 2
            ),

            Review(
                name = 'Sarah',
                email = 'N/A',
                rating = 5,
                comment = "Super cute house! Very cozy and clean. We would definitely stay again!",
                property_id = 2
            ),

            Review(
                name ='Gary',
                email = 'N/A',
                rating = 5,
                comment = "Our stay was very nice. Would look forward to a ski season visit. Easy access to the ski slopes.",
                property_id = 2,
            ),

            Review(
                name = 'Caleb',
                email = 'N/A',
                rating = 5,
                comment = "Nice clean space",
                property_id = 2,
            ),
            
            Review(
                name = 'Felicia',
                email = 'N/A',
                rating = 4,
                comment = "If you love to ski, this house will be perfect for you! It is located right on a ski lift hill! The home is older but the host is in the process of updating. The home is quaint and cozy. The beds were very comfortable and bed linens high quality. The bathrooms are small but in line with the time when this home was designed. There are tvs in every room and a nice lower level for hanging out. The rental price of the home reflects it being older so that makes it a good deal because rentals in this area are HIGH. The house was very convenient to all the places we were exploring including Autumn At Oz on Beech Mountain, the Banner Elk Winery, Grandfather Mountain Winery, and Mast General Store. The host was a pleasure to work with and we would definitely work with her again!",
                property_id = 2,
            ),

            Review(
                name = 'Brittany',
                email = 'N/A',
                rating = 4,
                comment = "It was a great stay. I was nervous about bringing my 8 month old, as there were stairs, but there was a baby gate ziptied to the top. the view from the patio was amazing, and on the weekend, we got to watch the ski lift running for mountain bikers, as it's off-season.The pictures do seem brighter than it actually is, but we didn't mind. Wifi was great, and cell service was surprisingly not an issue at the location. We went in the middle of July, and the fans and open windows were adequate for cooling us. Beware - There are a couple of holes in the driveway that are not easily seen as they are covered in grass, and my husband hurt his ankle by stepping in one while carrying in our luggage. It wasn't sprained, but we had gone there so he could play golf and was in too much pain to do so. Overall, I was very happy with this this place!",
                property_id = 2,
            ),

            Review(
                name = 'Kendall',
                email = 'N/A',
                rating = 5,
                comment = "The only downfall was that the Hulu remote didn't work. Honestly, it is more of a me not reading the description and reviews fully. Either way, the house is right down the road from plenty of attractions and places to eat! The firework show we watched from the balcony was the icing on the cake.",
                property_id = 2,
            ),

            Review(
                name = 'Michele',
                email = 'N/A',
                rating = 3,
                comment = "I felt like the pictures had been edited, to be very white, bright. House needs to be updated. Was disappointed when I arrived, but all turned out to be good. Host responded very quickly. Loved the view. Got to see some wildlife outside of house. Overall, was a good weekend. It was a good house, would stay here again.",
                property_id = 2,
            ),

            Review(
                name = 'Heidi',
                email = 'N/A',
                rating = 5,
                comment = "The location was perfect for our planned hikes, and the kitchen had everything we needed to enjoy cooking during our stay.",
                property_id = 2,
            ),

            Review(
                name = 'Martin',
                email = 'N/A',
                rating = 4,
                comment = "Great ski in/out spot. About 30M from main Sugar Mountain Resort lift. Quiet area, and only 8 minutes away from a big supermarket. The house is well located and cozy, but needs a renewal and modernization (Netflix, better plugs, and proper heating devices are a must!).",
                property_id = 2,
            ),

            Review(
                name = 'Steven',
                email = 'N/A',
                rating = 5,
                comment = "The location was perfect, the cabin was cozy and well stocked. Thank you Porter.",
                property_id = 2,
            ),

            Review(
                name = 'Tyler',
                email = 'N/A',
                rating = 5,
                comment = "Perfect location for ski in ski out beautiful view of the slope and felt very cozy and just like home, definitely will be looking to stay at this location many more times",
                property_id = 2,
            ),

            Review(
                name = 'Robert',
                email = 'N/A',
                rating = 5,
                comment = "Great and cozy place with ski in/out access.",
                property_id = 2,
            ),

            Review(
                name = 'Yuanshan',
                email = 'N/A',
                rating = 5,
                comment = "Love the communications. Nice to ski at Sugar Mountain!",
                property_id = 2,
            ),

            Review(
                name = 'Martin',
                email = 'N/A',
                rating = 5,
                comment = "We had an excellent stay. Will definitely be back.",
                property_id = 2,
            ),

            Review(
                name = 'Kelly',
                email = 'N/A',
                rating = 5,
                comment = "The best host! You will have a great experience by staying in this cabin",
                property_id = 2,
            ),

            Review(
                name = 'Andre',
                email = 'N/A',
                rating = 5,
                comment = "Our stay was wonderful with beautiful location and scenery. Great place to stay during any season.",
                property_id = 2,
            ),

            Review(
                name = 'Anna',
                email = 'N/A',
                rating = 5,
                comment = "It was a great space and perfect for the weekend we had planned to go up to Grandfather mountain",
                property_id = 2,
            ),

            Review(
                name = 'Rhonda',
                email = 'N/A',
                rating = 5,
                comment = "A beautiful view!! Spent hours on the porch.",
                property_id = 1,
            ),

            Review(
                name = 'Laura',
                email = 'N/A',
                rating = 5,
                comment = "WONDERFUL TIME AS ALWAYS!!!!!!!!!!!!",
                property_id = 1,
            ),

            Review(
                name = 'Matthew',
                email = 'N/A',
                rating = 5,
                comment = "Great house enjoyed the stay will be back next year",
                property_id = 1,
            ),

            Review(
                name = 'Elyse',
                email = 'N/A',
                rating = 5,
                comment = "This is a great spot. Super comfy, great big windows for viewing the beach, close to restaurants/grocery store, and for us (with a toddler) having a one-story space was perfect. We had great weather, but for rainy days, there is a really cute hangout spot under the house that we definitely would have appreciated. The house is decorated in a very fun way, and my toddler had a really great time asking questions about EVERY SINGLE ITEM :) Thanks for the great stay!",
                property_id = 1,
            ),

            Review(
                name = 'Harriet',
                email = 'N/A',
                rating = 4,
                comment = "The house is older, yet full of personality. A very fun, retro vibe. The view cannot be beat. Period. And the house is right beside the roped access over the dunes. If you want a newly remodeled house full of granite, tile, etc...this is not that. If you like quaint places with a lot of spirit, and killer view, this is it. The house was clean. Well appointed with salt and pepper and coffee filter kinds of things. Nice enough towels and linens. Porter was great to work with.",
                property_id = 1,
            ),

            Review(
                name = 'Terri',
                email = 'N/A',
                rating = 5,
                comment = "My husband and I had a great stay at Phat Fish with our toddler. The ocean views were amazing and loved the convenience of just walking down the steps and out to the beach. The house could use a little TLC, but it was very clean and had everything we needed. We did find a couple cockroaches, but I think that is just a NC or southeast thing and not a cleanliness factor because the house was super clean. Porter is a great host as instructions and response time were clear and prompt. Made some great family memories during our stay!",
                property_id = 1,
            ),

            Review(
                name = 'Sarah',
                email = 'N/A',
                rating = 5,
                comment = "This area is AMAZING and this house worked great for our family of 7! Thank you Porter!",
                property_id = 1,
            ),

            Review(
                name = 'Allison',
                email = 'N/A',
                rating = 4,
                comment = "Absolutely amazing location! You literally step off the back steps onto the beach. The place was fine, but definitely in need of some TLC. Worth overlooking for the location though!",
                property_id = 1,
            ),

            Review(
                name = 'Sarah Beth',
                email = 'N/A',
                rating = 5,
                comment = "We really enjoyed our stay. Right on the beach and a beautiful view of the ocean. Perfect place for a relaxing vacation!",
                property_id = 1,
            ),

            Review(
                name = 'John',
                email = 'N/A',
                rating = 5,
                comment = "Absolutely nothing negative to say. Really quaint beach house nicely decorated and perfect for our family. We would definitely stay there again",
                property_id = 1,
            ),

            Review(
                name = 'Margot',
                email = 'N/A',
                rating = 5,
                comment = "Fabulous location right on the beach ! Charming older beach cottage with great eclectic decor! Felt really like a home and the location cannot be beat!",
                property_id = 1,
            ),

            Review(
                name = 'Annette',
                email = 'N/A',
                rating = 5,
                comment = "Nice and clean and had everything you need! Enjoyed our weekend with the beautiful view!!",
                property_id = 1,
            ),

            Review(
                name = 'Laura',
                email = 'N/A',
                rating = 5,
                comment = "Amazing wonderful Beach Front Cottage will be back for SURE!",
                property_id = 1,
            ),

            Review(
                name = 'Sarah',
                email = 'N/A',
                rating = 5,
                comment = "Location was amazing and the perfect stay for our family for the OI marathon! Porter provided great tips for things to do before/after!",
                property_id = 1,
            ),

            Review(
                name = 'Sean',
                email = 'N/A',
                rating = 5,
                comment = "Loved it, would go back!",
                property_id = 1,
            ),

            Review(
                name = 'Gregory',
                email = 'N/A',
                rating = 5,
                comment = "It was a lot of fun! Great trip!",
                property_id = 1,
            ),

            Review(
                name = 'Lonnie',
                email = 'N/A',
                rating = 5,
                comment = "This house is in a great location. The house was clean and stocked with everything needed. We enjoyed ourselves and will most definitely come back to stay here.",
                property_id = 1,
            ),

            Review(
                name = 'Brent',
                email = 'N/A',
                rating = 5,
                comment = "great location the rocking chairs on the porch were nice",
                property_id = 1,
            ),

            Review(
                name = 'Roz',
                email = 'N/A',
                rating = 5,
                comment = "Cute place, can't beat the location. South facing so you get both sunrise and sunset. We had a short stay but really enjoyed Oak Island",
                property_id = 1,
            ),

            Review(
                name = 'Nick',
                email = 'N/A',
                rating = 5,
                comment = "Such a cool beach house! Everything was clean and as described. Porter was quick to respond with any questions and made our stay great! I don’t think I have ever stayed so close to the beach. The view is beautiful!",
                property_id = 1,
            ),

            Review(
                name = 'Paul',
                email = 'N/A',
                rating = 5,
                comment = "We had a great time. The communication was super easy and quick and the place looks exactly like it does on the pictures. The neighborhood is very conveniently located. You can enjoy the beautiful sunrise colors and the sunset by the beach. Would absolutely recommend to stay there!",
                property_id = 1,
            ),

            Review(
                name = 'Wanda',
                email = 'N/A',
                rating = 5,
                comment = "All I all I enjoyed the stay Although the structure could use some better upkeep as far as lighting and electrical outlets that are coming out of the wall and sparking fire when you plug and unplug things. The back deck isn’t stable. It needs better upkeep",
                property_id = 1,
            ),
        ]



        db.session.add_all(reviews)
        db.session.commit()
        u1=   User(
                username = 'Porter13',
                role = 'Admin',
            )
        u1.password_hash = 'SkyWalker2015!'
        
        
            

        
        users = [u1]
            

        db.session.add_all(users)
        db.session.commit()

        



        images = [
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/1c4bb929-c94e-4296-9a4a-9f3d0778f3d3.jpeg?im_w=1200',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/777a2e8f-fb7b-4989-b5d8-dae3b108bfc2.png?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/9d59d7de-4a39-44a5-9275-71f0a04fe44e.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/6f43f7b3-a593-4a65-a057-44d6dc0554eb.jpeg?im_w=1200',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/912d03b3-73f2-4c15-aa45-42386986569a.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/5d58082d-ea18-40e0-a680-311e3aeeffda.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/e2376194-93c2-4dd1-8d5b-6fed974e546a.jpeg?im_w=1200',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/8f901ab2-7034-48ba-8e73-091b6dca6917.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/8f901ab2-7034-48ba-8e73-091b6dca6917.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/ccc92446-ecc1-443f-a088-3bf1bf396e3d.jpeg?im_w=1200',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/d5f01cae-03e0-44ba-bfed-289ba834d1a3.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/fd229e28-1967-4d58-a648-967cf1c2d931.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/8734f10b-afb6-4936-a386-946318836630.jpeg?im_w=1200',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/d18e09a1-e766-45d8-a0ba-1265d9f81fe2.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/d381a213-dafe-42c2-8e06-f1f6f68bbff5.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/4a87b581-8b78-4ca2-8494-35be07012474.jpeg?im_w=1200',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/ee45b9ea-f683-4dee-8195-dce50202a8c5.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/ab673001-0324-4991-8645-5a73fb3281cf.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/f48fa1da-4d95-47ea-a763-60019cbdc7b9.jpeg?im_w=1200',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/d622f347-d39f-47ff-a7d9-72b5e03aa454.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/7a21ebf3-f403-4dbc-9aa3-00b8adc5f6d7.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/7e5b93fd-82ad-4e94-ba7b-a458fe89d6bb.jpeg?im_w=1200',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/3ec5ec9e-8a35-4ca6-b8a8-2ba1913c5db0.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/86d1d5a8-6162-45e1-a993-78ccc3974d2d.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-738948885345971986/original/49c51f28-dde8-4870-92d3-3bf69b7af701.jpeg?im_w=720',
                  property_id = 1,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/da29b252-0507-452f-9dca-aec927354da4.jpeg?im_w=1200',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/0d14a5ca-2659-4e07-8e04-42e083b116d2.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/65e14f0f-bb4b-45d7-8629-d440fffa05fb.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/1a3ed2e6-d845-40c1-9180-9adc54131ca4.jpeg?im_w=1200',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/00d40837-03e3-441a-952c-24f592e58f83.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/ed1409df-2558-4d93-9b97-250a98e1f03a.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/e86c05bf-33cb-4bb7-9674-f8e840a0b05f.jpeg?im_w=1200',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/92054986-e173-487b-8ff1-cf4c1c2ce480.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/183a0341-169c-49bf-a151-b2a3b774462b.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/e55ee25e-69b5-43b5-9dbc-dec7a47994ba.jpeg?im_w=1200',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/650522d6-14ba-47b7-aee0-dcebcee1a025.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/5fa8e0ed-1849-44fc-8218-1b8d9dffb74f.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/f74e6544-41a6-4996-af43-aef400612cd5.jpeg?im_w=1200',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/21328577-b2ce-47dc-9f31-dfd7590beb90.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/5f8e2f95-1b7a-42f2-bbaa-2ffa3839a9d8.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/2a5b9f5e-49c7-47be-8aef-2c8d85adc662.jpeg?im_w=1200',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/4e24b177-6ab0-43fc-b3bf-da2cfb7aa803.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/fc02e0e1-6d8b-4219-a3ea-7450f83c5a05.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/eeed1d92-4edb-4caf-8bc0-6b20b62d7ebb.jpeg?im_w=1200',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/7d0e887a-3969-4b09-afdc-a59b143ebfd7.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/8f1695e6-9f47-4c92-9530-b8b159adf81b.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/02a90730-015c-40ac-93ee-b9c087725aed.jpeg?im_w=1200',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/e9392d49-d857-48d3-8e60-3fb8a135d57c.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/a3743afe-9a7b-42d9-bed4-8bcd3619adc6.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/7712fbf3-c44a-4072-bfe3-197c97a8612d.jpeg?im_w=1200',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/b65b03cc-79cb-4355-aa60-ffbc80263104.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/79bf0ee4-89b8-4d96-9634-ff1ced2be408.jpeg?im_w=720',
                  property_id = 2,
                  ),
            Image(image = 'https://a0.muscache.com/im/pictures/miso/Hosting-731915024153813910/original/70f0f91f-3f3b-447c-8da9-c1e9b744adfa.jpeg?im_w=1200',
                  property_id = 2,
                  ), 
        ]

        db.session.add_all(images)
        db.session.commit()




        property_users = [
            PropertyUser(
               property_id = 1,
               user_id = 2,
            ),

            PropertyUser(
                property_id = 2,
                user_id = 3,
            ),
        ]

        db.session.add_all(property_users)
        db.session.commit()

        

        