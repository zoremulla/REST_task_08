1. Setup a virtual environment.
2. Fork the repository for [Django REST Task 8](https://github.com/JoinCODED/REST_task_08/) in JoinCODED’s Github and Clone it.
3. Install the packages from the requirements file.
4. A new model `Profile` have been added with a view `ProfileDetails` that retrieves the profile of the logged in user. Modify the `ProfileSerializer` so that it return the following:
   * Show the following information about the `User`:
      * `first_name`
      * `last_name`
   * `miles`
   * `past_bookings`: A **list** of `Booking` objects belonging to the logged in user that have passed.
      * Serialize them using the `BookingSerializer`.
   * `tier`: specify which tier the user have reached according to his miles.
      * 0 - 9999 : `Blue`
      * 10,000 - 59,999 : `Silver`
      * 60,000 - 99,999 : `Gold`
      * 100,000 ~ : `Platinum`
5. Modify the `BookingDetailsSerializer` so that it returns the following:
   * `total`: which is the total cost of the flight for all passengers.
   * `flight`: Use the `FlightSerializer` to display the flight info. 
   * `date`.
   * `id`.
   * `passengers`.
6. Modify the `BookingSerializer` so that it returns the following:
   * `flight`: Show the destination instead of the flight id using [SlugRelatedField](https://www.django-rest-framework.org/api-guide/relations/#slugrelatedfield).
   * `date`
   * `id`  
7. Push your code
